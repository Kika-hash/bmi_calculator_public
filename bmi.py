from flask import Flask, request, render_template, redirect, url_for
from backend import rest_handler, needle_calculation

app = Flask(__name__, static_folder="static")

@app.route("/")
def main_page():
    return render_template("main.html")



@app.route('/check_bmi', methods=['GET', 'POST'])
def check_bmi():
    if request.method == "POST":
        weight = int(request.form['weight'])
        height = int(request.form['height'])
        response = rest_handler(weight, height)
        needle = needle_calculation(weight, height)
        return render_template("main.html", result_message=response, needle_degree=needle)
    return redirect(url_for('main_.html'))

if __name__ == '__main__':
    app.run(debug=True)