from flask import Flask, render_template, request, jsonify
from resume_analyzer import ResumeAnalyzer
import os

app = Flask(__name__)
analyzer = ResumeAnalyzer()

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/resume_analyzer')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_text = request.form.get('resume')
    job_description = request.form.get('job_description')
    
    if not resume_text or not job_description:
        return jsonify({'error': 'Please provide both resume and job description'})
    
    result = analyzer.analyze_resume(resume_text, job_description)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)