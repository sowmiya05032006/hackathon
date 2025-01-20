import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Use the absolute path to the JSON file to load health data
with open(r'C:\Users\sowmi!!!!\Desktop\chat_bot\health_data.json', 'r') as file:
    health_data = json.load(file)

# Print the loaded data to verify
print("Health data loaded successfully.")
print(health_data)  # This will print the contents of the JSON file

@app.route('/')
def home():
    # Home page route
    return "Welcome to the Health Chatbot! Ask me anything about health."

@app.route('/chat', methods=['POST'])
def chat():
    # This route expects a POST request with a JSON payload
    user_message = request.json.get('message', '').lower()
    
    # Generate a response based on the user's message
    response = generate_response(user_message)
    return jsonify({"response": response})

def generate_response(message):
    # Check if the message matches any health topics in the data
    for topic, info in health_data.items():
        if topic.lower() in message:
            return info

    # Default response if no match is found
    return "I'm sorry, I couldn't find information on that. Could you please rephrase or ask about another health topic?"

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
