# driver_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)
drivers = {}

@app.route('/register_driver', methods=['POST'])
def register_driver():
    driver_id = len(drivers) + 1
    drivers[driver_id] = request.json
    return jsonify({'driver_id': driver_id}), 201

@app.route('/driver/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = drivers.get(driver_id)
    if driver:
        return jsonify(driver), 200
    return jsonify({'message': 'Driver not found'}), 404

if __name__ == '__main__':
    app.run(port=5001)

