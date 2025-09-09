# Comparative AI Chatbot Dashboard

A web application that compares responses from OpenAI, Claude, and Gemini 
APIs for user-provided prompts, built to demonstrate proficiency in AI API 
integration and web development.

## Features
- Submit a text prompt and view side-by-side responses from three AI 
models.
- Responsive UI built with Flask and Bootstrap.
- Secure API key management with python-dotenv.

## Screenshots
![Web Interface](screenshots/interface.png)

## Setup
1. Clone the repository: `git clone 
https://github.com/your-username/comparative-ai-chatbot`
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your API keys:

OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GEMINI_API_KEY=your_key

4. Run the app: `python app.py`
5. Open `http://localhost:5000` in your browser.

## Technologies
- Languages: Python, HTML, CSS
- APIs: OpenAI (ChatGPT), Anthropic (Claude), Google Gemini
- Frameworks/Libraries: Flask, requests, python-dotenv
