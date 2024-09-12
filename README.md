# AI-Powered Trip Advisor

## Description
This AI-powered Trip Advisor is a Streamlit web application with a Next.js frontend that uses the Mistral-Nemo-Instruct-2407 language model to provide personalized travel recommendations. Users can add places and get information about hotels, restaurants, and things to do in those locations.

## Features
- Add and store multiple travel destinations
- Get AI-generated recommendations for hotels, restaurants, and activities
- User-friendly interface built with Next.js and Streamlit
- Utilizes the powerful Mistral-Nemo-Instruct-2407 language model
- Tracks API usage within the app

## Technologies Used
- Python
- Streamlit
- Next.js
- React
- Hugging Face Inference API
- LangChain

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-trip-advisor.git
   cd ai-trip-advisor
   ```

2. Create a Python virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Node.js dependencies:
   ```bash
   npm install
   ```

5. Set up your environment variables:
   - Copy the `.env.template` file to `.env`:
     ```bash
     cp .env.template .env
     ```
   - Edit the `.env` file and replace `your_api_key_here` with your actual Hugging Face API token:
     ```bash
     HUGGING_FACE_API_KEY=your_actual_api_key_here
     ```

6. Set up your Streamlit secrets:
   - Create a `.streamlit/secrets.toml` file in the project root
   - Add your Hugging Face API token to the file:
     ```toml
     HUGGINGFACEHUB_API_TOKEN = "your-huggingface-api-token"
     ```

## Usage
1. Start the Next.js development server:
   ```bash
   npm run dev
   ```

2. In a separate terminal, run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to the URL provided by Next.js (usually `http://localhost:3000`)

4. Use the interface to:
   - Add new places
   - Select a place and category (Hotels, Restaurants, Things to do)
   - Get AI-generated recommendations

## Contributing
Contributions to improve the AI Trip Advisor are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Next.js](https://nextjs.org/)
- [React](https://reactjs.org/)
- [Hugging Face](https://huggingface.co/)
- [LangChain](https://langchain.com/)
- [Mistral AI](https://mistral.ai/)

## Setup

1. Clone the repository
2. Copy `.env.template` to `.env`
3. Replace `your_api_key_here` in `.env` with your actual Hugging Face API key
4. Install dependencies: `pip install -r requirements.txt`
5. Run the project: `python main.py`