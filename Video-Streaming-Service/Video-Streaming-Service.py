# video_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/start_stream', methods=['POST'])
def start_stream():
    return jsonify({'message': 'Video stream started'}), 200

@app.route('/end_stream', methods=['POST'])
def end_stream():
    return jsonify({'message': 'Video stream ended'}), 200

if __name__ == '__main__':
    app.run(port=5005)

