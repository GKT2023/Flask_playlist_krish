##  integrate HTML with flask
## HTTP Verb, GET and POST

## building url dynamically
# variable rules and url building

## jINJA2 template - - here we will integrate html with some data source so that we can fetch the values in html itself

'''
{%...%} for loop and  if statements
{{  }} expressions to print output
{#...#} this is for comments
'''

from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >=50:
        res = "Pass"
    else:
        res = "Fail"
    exp = {'score': score, 'res' : res}
    return render_template('result2.html', result=exp)
    # return render_template('result.html', result=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result=score)
    # return "the person is fail and marks is: " + str(score)

# result checker
@app.route('/results/<int:score>')
def results(score):
    result = ""
    if score < 50:
        result = "fail"
    else:
        result = 'success'
    return redirect(url_for(result,score=score))


## result checker html page
@app.route("/submit", methods=['GET','POST'])
def submit():
    average = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        datascience = float(request.form['datascience'])
        c = float(request.form['c'])
        maths = float(request.form['maths'])

        average = (science + maths + c + datascience) / 4

    result = ""
    if average < 50:
        result = "fail"
        
    else:
        result = "success"
    return redirect(url_for(result, score=average))
        

if __name__ == '__main__':
    app.run(debug=True)