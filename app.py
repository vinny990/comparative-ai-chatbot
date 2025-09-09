# app.py
from flask import Flask, request, render_template
from api_utils import query_openai, query_claude, query_gemini

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        openai_response = query_openai(prompt)
        claude_response = query_claude(prompt)
        gemini_response = query_gemini(prompt)
        return render_template('index.html', prompt=prompt, 
                             openai=openai_response, 
claude=claude_response, 
                             gemini=gemini_response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
