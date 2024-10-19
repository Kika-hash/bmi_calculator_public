from flask import Flask, request, render_template, jsonify
from backend import rest_handler

app = Flask(__name__, static_folder="static")

@app.route("/")
def main_page():
    return render_template("main.html")

"""

@app.route('/check_bmi', methods=['POST'])
def check_bmi():
    data = request.get_json()

    weight = data.get('weight')
    height = data.get('height')

    if not weight or not height or height <= 0:
        return jsonify({"error": "Nieprawidłowe dane: podaj prawidłową wagę i wzrost."}), 400

    result = rest_handler(weight, height)

    # Sprawdzenie, czy rest_handler zwrócił prawidłową odpowiedź
    if not result or "message" not in result or "bmi_status" not in result:
        return jsonify({"error": "Błąd w przetwarzaniu danych BMI."}), 500

    # Zwrócenie odpowiedzi JSON z wartościami 'message' i 'bmi_status'
    return jsonify({
        "message": result["message"],
        "bmi_status": result["bmi_status"]  # Zakładam, że to kąt wskazówki w stopniach
    })

"""


if __name__ == '__main__':
    app.run(debug=True)