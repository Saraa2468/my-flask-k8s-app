from flask import Flask, jsonify
app = Flask(_name_)

@app.route("/")
def hello():
    return jsonify({"message":"hello from my-app", "version":"v1"})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)