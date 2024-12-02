# iot_integration_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/connect_device', methods=['POST'])
def connect_device():
    data = request.json
    # Logic to connect and integrate IoT devices
    return jsonify({"status": "Device connected", "device_id": data.get("device_id")}), 200

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    # Logic to receive and process data from IoT devices
    return jsonify({"status": "Data received", "data": data}), 200

if __name__ == '__main__':
    app.run(port=5015)

