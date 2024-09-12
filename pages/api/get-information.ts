import type { NextApiRequest, NextApiResponse } from 'next'
import { spawn } from 'child_process'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { place, category } = req.body
    console.log(`Received request for place: ${place}, category: ${category}`)

    const pythonProcess = spawn('python', ['app.py', place, category], {
      env: { ...process.env, PYTHONUNBUFFERED: '1' }
    })

    let result = ''
    let error = ''

    pythonProcess.stdout.on('data', (data) => {
      console.log(`Python stdout: ${data}`)
      result += data.toString()
    })

    pythonProcess.stderr.on('data', (data) => {
      console.error(`Python stderr: ${data}`)
      error += data.toString()
    })

    pythonProcess.on('error', (err) => {
      console.error(`Failed to start Python process: ${err}`)
      res.status(500).json({ error: 'Failed to start Python process', details: err.message })
    })

    pythonProcess.on('close', (code) => {
      console.log(`Python process exited with code ${code}`)
      if (code !== 0) {
        res.status(500).json({ error: 'Python script execution failed', details: error })
      } else {
        try {
          const jsonResult = JSON.parse(result)
          res.status(200).json(jsonResult)
        } catch (parseError) {
          console.error(`Failed to parse Python output: ${result}`)
          res.status(500).json({ error: 'Failed to parse Python script output', details: result })
        }
      }
    })

    // Increase the timeout to 2 minutes (120000 ms)
    const timeout = setTimeout(() => {
      if (!res.writableEnded) {
        console.error('Request timed out')
        pythonProcess.kill()
        res.status(504).json({ error: 'Request timeout' })
      }
    }, 120000) // 2 minutes timeout

    // Clear the timeout if the response has been sent
    res.on('finish', () => clearTimeout(timeout))
  } else {
    res.setHeader('Allow', ['POST'])
    res.status(405).end(`Method ${req.method} Not Allowed`)
  }
}