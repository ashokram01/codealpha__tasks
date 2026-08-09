from flask import Flask, render_template, request, jsonify
import json
import random
import re

app = Flask(__name__)

# Load Predefined Patterns (intents.json)
with open('intents.json', 'r') as file:
    intents = json.load(file)

def get_chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Pattern matching logic
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # Search for keyword matches in user input
            if re.search(r'\b' + pattern.lower() + r'\b', user_input):
                return random.choice(intent['responses'])
                
    return "I am still learning! Could you please rephrase that or type 'support' to contact our team?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_reply():
    user_msg = request.form["msg"]
    response = get_chatbot_response(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
