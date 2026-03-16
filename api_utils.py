# api_utils.py
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

def call_openai(prompt):
    try:
        start = time.time()
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        elapsed = time.time() - start
        return response.json()['choices'][0]['message']['content'], elapsed
    except requests.RequestException as e:
        return f"Error querying OpenAI: {e.response.status_code if e.response is not None else 'connection error'}", 0


def call_claude(prompt):
    try:
        start = time.time()
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": os.getenv('ANTHROPIC_API_KEY'),
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        data = {
            "model": "claude-haiku-4-5-20251001",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        elapsed = time.time() - start
        return response.json()['content'][0]['text'], elapsed
    except requests.RequestException as e:
        return f"Error querying Claude: {e.response.status_code if e.response is not None else 'connection error'}", 0


def call_gemini(prompt):
    try:
        start = time.time()
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(
            f"{url}?key={os.getenv('GEMINI_API_KEY')}",
            json=data,
            headers=headers
        )
        response.raise_for_status()
        elapsed = time.time() - start
        return response.json()['candidates'][0]['content']['parts'][0]['text'], elapsed
    except requests.RequestException as e:
        return f"Error querying Gemini: {e.response.status_code if e.response is not None else 'connection error'}", 0
