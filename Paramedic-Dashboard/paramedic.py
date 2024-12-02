# paramedic_dashboard.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Fetch paramedic dashboard data
    return jsonify({"dashboard_data": "Paramedic dashboard"}), 200

if __name__ == '__main__':
    app.run(port=5005)

