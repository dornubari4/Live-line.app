# gateway_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/gateway', methods=['POST'])
def gateway():
    # Handles requests to route to other microservices
    return jsonify({"status": "Request routed through gateway"}), 200

if __name__ == '__main__':
    app.run(port=5011)

