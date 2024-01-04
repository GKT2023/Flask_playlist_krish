## building url dynamically
# variable rules and url building

from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route("/")
def welcome():
    return "welcome to the page"


@app.route('/success/<int:score>')
def success(score):
    return "the person is pass and marks is: " + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "the person is fail and marks is: " + str(score)

# result checker
@app.route('/results/<int:score>')
def results(score):
    result = ""
    if score < 50:
        result = "fail"
    else:
        result = 'success'
    return redirect(url_for(result,score=score))


if __name__ == '__main__':
    app.run(debug=True)