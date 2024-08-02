from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        try:
            data = request.json.get('data', [])
            user_id = "john_doe_17091999"
            email = "john@xyz.com"
            roll_number = "ABCD123"
            
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]
            highest_alphabet = sorted(alphabets, key=lambda x: x.lower())[-1:] if alphabets else []

            response = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"is_success": False, "error": str(e)}), 400
    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
