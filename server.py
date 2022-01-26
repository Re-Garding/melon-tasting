
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from jinja2 import StrictUndefined
import os, model, crud

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
    return render_template("homepage.html") 

@app.route('/booking')
def book():
    return render_template("book.html")

@app.route('/booked')
def all_bookings():
    return render_template("all_bookings.html")


if __name__ == "__main__":
    model.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
    host="0.0.0.0",
    use_reloader=True,
    use_debugger=True,
