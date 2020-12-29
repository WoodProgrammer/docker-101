from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/index")
def index():
    hello_val = os.environ.get("HELLO_VAL", "default")
    return jsonify({"hello": "{}".format(hello_val)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)