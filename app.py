# app.py
import logging
import time
from flask import Flask, request, render_template
from api_utils import call_openai, call_claude, call_gemini
from database import init_db, save_response
from analysis import analyze_responses

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

try:
    init_db()
except Exception as e:
    logging.error(f"Failed to initialize database: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            prompt = request.form["prompt"]
            logging.debug(f"Received prompt: {prompt}")

            openai_response, openai_time = call_openai(prompt)
            claude_response, claude_time = call_claude(prompt)
            gemini_response, gemini_time = call_gemini(prompt)

            save_response(prompt, openai_response, claude_response, gemini_response)
            analysis = analyze_responses()

            return render_template(
                "index.html",
                prompt=prompt,
                openai=openai_response,
                claude=claude_response,
                gemini=gemini_response,
                times=[openai_time, claude_time, gemini_time],
                analysis=analysis
            )
        return render_template("index.html")
    except Exception as e:
        logging.error(f"Error in index route: {e}")
        return "Internal Server Error", 500

@app.route("/analysis")
def analysis():
    try:
        results = analyze_responses()
        return render_template("analysis.html", analysis=results)
    except Exception as e:
        logging.error(f"Error in analysis route: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
