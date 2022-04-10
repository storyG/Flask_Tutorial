from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
  stuff = "This is bold text"
  favorite_pizza = ["Pepperoni", "Cheese", "41"]
  return render_template("index.html",
                          stuff = stuff,
                          favorite_pizza = favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
  return render_template("user.html", name = name)

# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

# Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
  return render_template("500.html"), 500
