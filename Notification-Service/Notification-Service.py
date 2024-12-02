# notification_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/notify_user', methods=['POST'])
def notify_user():
    # Here you would integrate with an SMS or Email service
    return jsonify({'message': 'Notification sent to user'}), 200

@app.route('/notify_driver', methods=['POST'])
def notify_driver():
    return jsonify({'message': 'Notification sent to driver'}), 200

if __name__ == '__main__':
    app.run(port=5004)

