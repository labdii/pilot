from flask import Flask
from flask import render_template


app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():

    context = {
        "title": "INICIO"
    }

    return render_template("index.html", context=context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)