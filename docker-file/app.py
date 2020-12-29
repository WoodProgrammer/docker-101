from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/index")
def index():
    return jsonify({"hello": "NKU"})

if __name__ == "__main__":
    app.run(host="0.0.0.0")