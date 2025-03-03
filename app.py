from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# OpenAI API configuration
API_URL = "https://api.openai.com/v1/images/generations"
API_KEY = os.getenv('OPENAI_API_KEY')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Generate image route
@app.route('/generate', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    size = request.form.get('size', '1024x1024')  # Default size

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "n": 1,
        "size": size
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        image_url = response.json()['data'][0]['url']
        return render_template('result.html', image_url=image_url)
    except requests.exceptions.RequestException as e:
        return f"Error generating image: {e}", 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)￼Enter
