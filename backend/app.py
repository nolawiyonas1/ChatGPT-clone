from flask import Flask, jsonify, request
# CORS is a security feature implemented by web browsers to prevent web pages from making requests to a different domain than the one that served the web page
from flask_cors import CORS
import os
from openai import OpenAI  # Updated import for OpenAI
from dotenv import load_dotenv, find_dotenv

# DOTENV
load_dotenv(find_dotenv()) 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Updated API initialization

# FLASK 
app = Flask(__name__)
CORS(app) # prevent web pages from making requests to a different domain than the one that served the web page

@app.route('/api', methods=['POST'])
def gpt3(): # This function will be executed whenever a POST request is made to the /api endpoint.
    data = request.get_json() # request.get_json() is a Flask method that parses the incoming JSON request data and converts it into a Python dictionary
    message = data['message']
    
    response = client.chat.completions.create( # Updated call for chat models
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],  # Chat API uses messages
        max_tokens=3000,
        temperature=0.9, # controls the randomness of the output. Higher values like 0.9 make the output more random, while lower values make it more focused and deterministic
    )
    
    print(response.choices[0].message.content) # print response to the terminal
    return jsonify({ # returns the response from the OpenAI API as a JSON object (convert python dictionary to JSON object)
        "message": response.choices[0].message.content  # Access the 'message' key for chat model responses
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True) # starts the Flask server
