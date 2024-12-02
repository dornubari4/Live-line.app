# feedback_rating_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    # Store feedback and rating
    return jsonify({"status": "Feedback received"}), 200

if __name__ == '__main__':
    app.run(port=5008)

