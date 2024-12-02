# tracking_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)
tracking_data = {}

@app.route('/track_ambulance/<int:booking_id>', methods=['GET'])
def track_ambulance(booking_id):
    location = tracking_data.get(booking_id)
    if location:
        return jsonify(location), 200
    return jsonify({'message': 'Tracking data not found'}), 404

if __name__ == '__main__':
    app.run(port=5006)

