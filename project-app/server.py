from flask import Flask, jsonify, request
from flask_cors import CORS

from chat import response_chat

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


@app.route('/message', methods=['POST'])
def handle_message():
    message = request.json['message']
    response = {'response': response_chat(message)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
