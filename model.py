import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://router.huggingface.co/fireworks-ai/inference/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
}

def cevap_olustur(ses_input):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": ses_input  
            }
        ],
        "model": "accounts/fireworks/models/llama-v3p1-8b-instruct"
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
