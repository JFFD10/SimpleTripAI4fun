# AI-Powered Trip Advisor

## Description
This AI-powered Trip Advisor is a Streamlit web application that uses the Mistral-Nemo-Instruct-2407 language model to provide personalized travel recommendations. Users can add places and get information about hotels, restaurants, and things to do in those locations.

## Features
- Add and store multiple travel destinations
- Get AI-generated recommendations for hotels, restaurants, and activities
- User-friendly interface built with Streamlit
- Utilizes the powerful Mistral-Nemo-Instruct-2407 language model
- Tracks API usage within the app

## Technologies Used
- Python
- Streamlit
- Hugging Face Inference API
- LangChain

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-trip-advisor.git
   cd ai-trip-advisor
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Hugging Face API token:
   - Create a `.streamlit/secrets.toml` file in the project root
   - Add your Hugging Face API token to the file:
     ```toml
     HUGGINGFACEHUB_API_TOKEN = "your-huggingface-api-token"
     ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`)

3. Use the interface to:
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
- [Hugging Face](https://huggingface.co/)
- [LangChain](https://langchain.com/)
- [Mistral AI](https://mistral.ai/)