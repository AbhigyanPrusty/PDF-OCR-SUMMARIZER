import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve Hugging Face API Key
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face model to use
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

# Function to summarize text using Hugging Face API
def summarize_text(text):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    # Optional: Check if model is available
    status_response = requests.get(API_URL, headers=headers)
    if status_response.status_code != 200:
        return f"Model not available (status: {status_response.status_code})"

    payload = {
        "inputs": text[:1024]
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()[0]["summary_text"]
        except (KeyError, IndexError):
            return "Error: Unexpected response format."
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
if __name__ == "__main__":
    text = "Hugging Face is a company focused on democratizing machine learning. They provide tools like the Transformers library and host models for inference."
    print(summarize_text(text))
