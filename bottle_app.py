from bottle import default_app, route, post, template

#deocraters let u attach a behavior to a function, tells it what to do when it receives particular address
@route('/')
def hello_world():
    return template("menu.html")

@route('/bmi')
def bmiForm():
    return template("bmi.html")

@post('/bmi_result')
def bmiResult():
    return template("bmi_result.html")

@route('/bmi_BB')
def bmiBBForm():
    return template("bmi_BB.html")

@post('/bmi_BB_result')
def bmiBBResult():
    return template("bmi_BB_result.html")

@route('/bmi_metric')
def metricForm():
    return template("bmi_metric.html")

@route('/start')
def startQuiz():
    return template("start.html")

@post('/q1')
def questionOne():
    return template("q1.html")

@post('/q2')
def questionTwo():
    return template("q2.html")

@post('/q2Edit')
def tryingOut():
    return template("q2Edit.html")

@post('/q3')
def questionThree():
    return template("q3.html")

@post('/q4')
def questionFour():
    return template("q4.html")

@post('/q5')
def questionFive():
    return template("q5.html")

@post('/q6')
def questionSix():
    return template("q6.html")

@post('/q7')
def questionSeven():
    return template("q7.html")

@post('/q8')
def questionEight():
    return template("q8.html")

@post('/q9')
def questionNine():
    return template("q9.html")

@post('/q10')
def questionTen():
    return template("q10.html")

@post('/q11')
def questionEleven():
    return template("q11.html")

@post('/q12')
def questionTwelve():
    return template("q12.html")

@post('/qResult')
def result():
    return template("qResult.html")

@route('/ones')
def phlegmatic():
    return template("ones.html")

@route('/tens')
def melancholic():
    return template("tens.html")

@route('/hundreds')
def choleric():
    return template("hundreds.html")

@route('/thousands')
def saguine():
    return template("thousands.html")

@route('/test')
def test():
    return template("test.html")

@post('/test1')
def test1():
    return template("test1.html")

application = default_app()

