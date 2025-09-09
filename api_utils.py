# api_utils.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def query_openai(prompt):
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer 
{os.getenv('OPENAI_API_KEY')}", "Content-Type": "application/json"}
        data = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", 
"content": prompt}], "max_tokens": 150}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.RequestException as e:
        return f"Error querying OpenAI: {str(e)}"

def query_claude(prompt):
    try:
        url = "https://api.anthropic.com/v1/messages"
        headers = {"x-api-key": os.getenv('ANTHROPIC_API_KEY'), 
"Content-Type": "application/json"}
        data = {"model": "claude-3-sonnet-20240229", "messages": [{"role": 
"user", "content": prompt}], "max_tokens": 150}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()['content'][0]['text']
    except requests.RequestException as e:
        return f"Error querying Claude: {str(e)}"

def query_gemini(prompt):
    try:
        url = 
"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        response = 
requests.post(f"{url}?key={os.getenv('GEMINI_API_KEY')}", json=data, 
headers=headers)
        response.raise_for_status()
        return 
response.json()['candidates'][0]['content']['parts'][0]['text']
    except requests.RequestException as e:
        return f"Error querying Gemini: {str(e)}"
