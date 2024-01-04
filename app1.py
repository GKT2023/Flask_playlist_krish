from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>welcome to flask tutorials</h1>"

@app.route('/members')
def members():
    return "<h1> Entire python community wants to learn Flask"

if __name__ == '__main__':
    app.run(debug=True)