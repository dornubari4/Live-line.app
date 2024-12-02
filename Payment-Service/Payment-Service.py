# payment_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/create_payment', methods=['POST'])
def create_payment():
    return jsonify({'message': 'Payment created'}), 200

@app.route('/payment/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    return jsonify({'message': 'Payment details'}), 200

if __name__ == '__main__':
    app.run(port=5007)

