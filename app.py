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

        client = InferenceClient(
            "mistralai/Mistral-Nemo-Instruct-2407",
            token=hf_token,
        )

        prompt_template = PromptTemplate(
            input_variables=["place", "category"],
            template="Briefly provide information about {category} in {place}. List 3 top options with short descriptions."
        )

        prompt = prompt_template.format(place=place, category=category)
        messages = [{"role": "user", "content": prompt}]
        
        print("Sending request to Hugging Face API", file=sys.stderr)
        try:
            # Set a timeout for the entire request
            response = requests.post(
                f"https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Instruct-2407",
                headers={"Authorization": f"Bearer {hf_token}"},
                json={"inputs": prompt},
                timeout=90  # 90-second timeout
            )
            response.raise_for_status()
            result = response.json()[0]['generated_text']
            print("Received response from Hugging Face API", file=sys.stderr)
            
            # Format the result
            formatted_result = f"{place} - {category}\n" + "\n".join([f"• {point.strip()}" for point in result.split('.') if point.strip()])
            
            return json.dumps({"information": formatted_result})
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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Invalid number of arguments"}))
        sys.exit(1)
    
    place = sys.argv[1]
    category = sys.argv[2]
    result = get_information(place, category)
    print(result)
    sys.stdout.flush()