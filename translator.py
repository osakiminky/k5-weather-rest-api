from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("translator.html")

@app.route("/api/v1/<word>/")
def api(word):
    definition = word.upper()
    both_definitions = {"definition": definition, "word":word}
    return both_definitions

app.run(debug=True, port=5001)
