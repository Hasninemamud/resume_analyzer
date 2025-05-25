import requests
import json

class ResumeAnalyzer:
    def __init__(self):
        self.api_key = "d3a24c9d609587cbd378ff3cc2e60fe87248ff6be088057112dfc8cffad62963"
        self.api_url = "https://api.together.ai/v1/chat/completions"
        
    def analyze_resume(self, resume_text, job_description):
        # Prepare the prompt for the AI
        prompt = f"""Analyze the following resume against the job description and provide:
        1. A match score (0-100)
        2. Key skills identified
        3. Detailed feedback on chances of being shortlisted
        4. Interview preparation suggestions

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        Please provide a structured analysis in JSON format with the following keys:
        - match_score (number)
        - skills (array of strings)
        - feedback (array of strings)
        - interview_prep (array of strings)
        """

        # Prepare the API request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # You can change the model as needed
            "messages": [
                {"role": "system", "content": "You are a professional resume analyzer and career coach."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        try:
            # Make the API request
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            
            # Parse the response
            result = response.json()
            analysis = json.loads(result['choices'][0]['message']['content'])
            
            return analysis
            
        except requests.exceptions.RequestException as e:
            return {
                'error': f"API request failed: {str(e)}",
                'match_score': 0,
                'skills': [],
                'feedback': ["Error analyzing resume. Please try again."],
                'interview_prep': []
            }
