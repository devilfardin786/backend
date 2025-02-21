from flask import Flask, request, jsonify

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
            "user_id": "your_fullname_dob",  # Replace with actual details
            "email": "your_email@example.com",  # Replace with actual email
            "roll_number": "your_roll_number",  # Replace with actual roll number
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

if __name__ == '__main__':
    app.run(debug=True)

