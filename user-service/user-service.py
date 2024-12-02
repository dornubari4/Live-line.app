# user_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/register', methods=['POST'])
def register():
    user_id = len(users) + 1
    users[user_id] = request.json
    return jsonify({'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
    for user_id, user in users.items():
        if user['email'] == request.json['email'] and user['password'] == request.json['password']:
            return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=5000)

