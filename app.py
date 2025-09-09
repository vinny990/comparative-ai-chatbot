from flask import Flask, request, render_template
from api_utils import call_openai, call_claude, call_gemini
from database import init_db, save_response

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        openai_response, openai_time = call_openai(prompt)
        claude_response, claude_time = call_claude(prompt)
        gemini_response, gemini_time = call_gemini(prompt)
        save_response(prompt, openai_response, claude_response, 
gemini_response)
        return render_template("index.html",
                             prompt=prompt,
                             openai=openai_response,
                             claude=claude_response,
                             gemini=gemini_response,
                             times=[openai_time, claude_time, 
gemini_time])
    return render_template("index.html")
