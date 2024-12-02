# booking_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)
bookings = {}

@app.route('/request_ambulance', methods=['POST'])
def request_ambulance():
    booking_id = len(bookings) + 1
    bookings[booking_id] = request.json
    return jsonify({'booking_id': booking_id}), 201

@app.route('/booking/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = bookings.get(booking_id)
    if booking:
        return jsonify(booking), 200
    return jsonify({'message': 'Booking not found'}), 404

if __name__ == '__main__':
    app.run(port=5002)

