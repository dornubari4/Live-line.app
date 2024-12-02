# hospital_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)
hospitals = {}

@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    return jsonify(hospitals), 200

@app.route('/hospital/<int:hospital_id>', methods=['GET'])
def get_hospital(hospital_id):
    hospital = hospitals.get(hospital_id)
    if hospital:
        return jsonify(hospital), 200
    return jsonify({'message': 'Hospital not found'}), 404

if __name__ == '__main__':
    app.run(port=5003)

