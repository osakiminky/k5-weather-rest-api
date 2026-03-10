from flask import Flask, render_template

app = Flask(__name__)


# Define a route for the URL "/home"
#Function will run when a u visit http://localhost:5000
@app.route("/")
def home():
    return render_template("home.html")

# Define another route for the URL "/station/" & "/date/"
#Function will run when u visit http://localhost:5000/about/
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)