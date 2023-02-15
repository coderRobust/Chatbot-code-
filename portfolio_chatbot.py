from flask import Flask, request
import random

app = Flask(__name__)

# Route for the homepage


@app.route('/')
def index():
    return 'Welcome to my portfolio website!'

# Route for the chatbot


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message'].lower()

    # Bot's response to a greeting
    if 'hello' in message or 'hi' in message:
        responses = ['Hello!', 'Hi!', 'Nice to meet you!']
        bot_response = random.choice(responses)

    # Bot's response to a question about your work
    elif 'work' in message or 'projects' in message:
        bot_response = 'I specialize in web development and have worked on several projects, including python, Java, Javascript. AWS'

    # Bot's response to a question about your skills
    elif 'skills' in message or 'abilities' in message:
        bot_response = 'I have expertise in HTML, CSS, JavaScript, and Python, Java among others.'

    # Bot's response to a question that it doesn't know the answer to
    else:
        bot_response = "I'm sorry, I don't understand.Can you please rephrase your question?"

    return {'message': bot_response}


if __name__ == '__main__':
    app.run(debug=True)
