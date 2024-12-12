from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Health Calculator app!"})

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    try:
        result = calculate_bmi(data["height"], data["weight"])
        return jsonify({"operation": "BMI", "result": result})
    except KeyError as e:
        return jsonify({"error": "Missing required parameters 'height' and 'weight'"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    try:
        result = calculate_bmr(data["height"], data["weight"], data["age"], data["gender"])
        return jsonify({"operation": "BMR", "result": result})
    except KeyError as e:
        return jsonify({"error": "Missing required parameters 'height' , 'weight' , 'age' and 'gender'"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

