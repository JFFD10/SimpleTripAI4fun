import sys
from huggingface_hub import InferenceClient
from langchain.prompts import PromptTemplate
import os
import json
import traceback
import requests
from requests.exceptions import Timeout

def get_information(place, category):
    try:
        print(f"Processing request for place: {place}, category: {category}", file=sys.stderr)
        
        hf_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
        if not hf_token:
            print("HUGGINGFACEHUB_API_TOKEN not set", file=sys.stderr)
            return json.dumps({"error": "HUGGINGFACEHUB_API_TOKEN not set"})

        prompt_template = PromptTemplate(
            input_variables=["place", "category"],
            template="Provide information about the top 3 {category} in {place}. For each, include the name and a brief description."
        )

        prompt = prompt_template.format(place=place, category=category)
        
        print("Sending request to Hugging Face API", file=sys.stderr)
        try:
            response = requests.post(
                f"https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Instruct-2407",
                headers={"Authorization": f"Bearer {hf_token}"},
                json={"inputs": prompt},
                timeout=90
            )
            response.raise_for_status()
            result = response.json()[0]['generated_text']
            print(f"Raw response from Hugging Face API: {result}", file=sys.stderr)
            
            relevant_info = extract_relevant_info(result)
            if not relevant_info.strip():
                return json.dumps({"error": f"No information found for {category} in {place}"})
            return json.dumps({"information": relevant_info})
        except Timeout:
            print("Hugging Face API request timed out", file=sys.stderr)
            return json.dumps({"error": "Hugging Face API request timed out"})
        except requests.RequestException as api_error:
            print(f"Error in Hugging Face API call: {str(api_error)}", file=sys.stderr)
            return json.dumps({"error": f"Hugging Face API error: {str(api_error)}"})
    except Exception as e:
        print(f"Error occurred: {str(e)}", file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        return json.dumps({"error": str(e)})

def extract_relevant_info(text):
    lines = text.split('\n')
    relevant_lines = [line.strip() for line in lines if line.strip() and not line.lower().startswith("provide information")]
    return '\n'.join(relevant_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Invalid number of arguments"}))
        sys.exit(1)
    
    place = sys.argv[1]
    category = sys.argv[2]
    result = get_information(place, category)
    print(result)
    sys.stdout.flush()