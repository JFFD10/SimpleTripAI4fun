import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('HUGGING_FACE_API_KEY')

# Use the api_key in your code
# ...