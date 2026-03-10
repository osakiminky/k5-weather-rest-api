from flask import Flask, render_template
app = Flask("Website")

# Define a route for the URL "/home"
#Function will run when a u visit http://localhost:5000
@app.route("/")
def home():
    return render_template("tutorial.html")

# Define another route for the URL "/about/"
#Function will run when u visit http://localhost:5000/about/
@app.route("/about/")
def about():
    return render_template("about.html")

# Run the Flask development server
app.run(debug=True)