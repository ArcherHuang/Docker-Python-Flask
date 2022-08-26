from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# GET http://VM-IP
@app.route("/")
def hello():
    print(f"Hell World")
    return "Python Flask in a container !"

# POST http://VM-IP/store
# Body
#   {
#     "run": 66
#   }
@app.route("/store", methods=["POST"])
def save_store():
    request_data = request.get_json()
    print(f"data: {request_data}")
    with open("/model/data.json", "w") as outfile:
        json.dump(request_data, outfile)
    return jsonify(request_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)