from flask import Flask, render_template, request, jsonify
from ga_optimizer import run_ga

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    input_data = request.get_json()
    result = run_ga(input_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
