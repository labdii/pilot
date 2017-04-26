from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():

    context = {
	"ping": "pong",
        "enterprise": "Labdii Inc."
    }

    return jsonify(context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
