# analytics_reporting_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    # Logic to process and generate analytics report based on data
    report_data = {"total_responses": 150, "average_response_time": "5 minutes", "positive_feedback": "85%"}
    return jsonify({"status": "Report generated", "report": report_data}), 200

@app.route('/get_analytics', methods=['GET'])
def get_analytics():
    # Return general analytics data
    analytics_data = {
        "total_users": 2000,
        "active_ambulances": 50,
        "incidents_today": 30
    }
    return jsonify({"status": "Analytics data", "data": analytics_data}), 200

if __name__ == '__main__':
    app.run(port=5019)

