from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Validate JSON request
        if not request.is_json:
            return jsonify({"is_success": False, "error": "Invalid JSON"}), 400
        
        data = request.json.get("data", [])
        
        # Ensure data is a list of strings
        if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
            return jsonify({"is_success": False, "error": "Invalid data format"}), 400

        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

        response = {
            "is_success": True,
            "user_id": "fardin_khan_08062003",  # Replace with actual details
            "email": "22bai71309@cuchd.in",  # Replace with actual email
            "roll_number": "22bai71309",  # Replace with actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# Make Flask work with Vercel
app.wsgi_app = ProxyFix(app.wsgi_app)
handler = app  # Required by Vercel
