from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/index")
def index():
    
    file_obj = open("/opt/file.json", "a+")
    file_obj.append(request.json)
    file_obj.close()
    return jsonify({"hello": "{}".format(request.json)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)