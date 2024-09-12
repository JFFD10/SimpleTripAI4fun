import streamlit as st
from huggingface_hub import InferenceClient
from langchain.prompts import PromptTemplate
import os

# Load the Hugging Face API token from Streamlit secrets
hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token

# Initialize a counter to track the number of API requests made in this session
if 'request_count' not in st.session_state:
    st.session_state.request_count = 0

# Set up the main title of the Streamlit app
st.title("Trip Advisor")

# Create a sidebar for debug information
st.sidebar.title("Debug Information")
st.sidebar.write(f"Token (first 5 chars): {hf_token[:5]}...")
st.sidebar.write(f"Requests made this session: {st.session_state.request_count}")

# Initialize the Hugging Face Inference Client with the specified model
client = InferenceClient(
    "mistralai/Mistral-Nemo-Instruct-2407",
    token=hf_token,
)

# Create a template for the prompt that will be sent to the AI model
prompt_template = PromptTemplate(
    input_variables=["place", "category"],
    template="Briefly provide information about {category} in {place}. List 3 top options with short descriptions."
)

# Create an input field for adding new places
new_place = st.text_input("Add a new place:")
if st.button("Add Place"):
    if new_place:
        # Add the new place to the session state
        st.session_state.places = st.session_state.get('places', []) + [new_place]
        st.success(f"Added {new_place} to your places!")
    else:
        st.warning("Please enter a place name.")

# Create dropdown menus for selecting a place and category
place = st.selectbox("Select a place:", st.session_state.get('places', []))
category = st.selectbox("Select a category:", ["Hotels", "Restaurants", "Things to do"])

# Create a button to generate information
if st.button("Get Information"):
    if place and category:
        try:
            with st.spinner("Generating information..."):
                # Format the prompt with the selected place and category
                prompt = prompt_template.format(place=place, category=category)
                messages = [{"role": "user", "content": prompt}]
                # Send the request to the AI model
                response = client.chat_completion(
                    messages=messages,
                    max_tokens=500,
                    stream=False
                )
                # Extract the generated text from the response
                result = response.choices[0].message.content
                # Increment the request counter
                st.session_state.request_count += 1
            # Display the generated information
            st.write(result)
            # Update the request count in the sidebar
            st.sidebar.write(f"Requests made this session: {st.session_state.request_count}")
        except Exception as e:
            # Handle any errors that occur during the API call
            st.error(f"An error occurred: {str(e)}")
            st.sidebar.error(f"Detailed error: {str(e)}")
    else:
        # Prompt the user to select both a place and category
        st.warning("Please select a place and category.")