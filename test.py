from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return "hello"




@app.route('/name',methods= ['POST','GET'])

def enter_data2():
    p = """<!DOCTYPE html>
<html>
<body>
<h2>Enter your name and age and we will tell you what year you were born!</h2>
<form action="http://localhost:5000/result" method="GET">
  First name:<br>
  <input type="text" name="firstname" value="">
  <br>
  Enter your age:<br>
  <input type="number" name="number" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>""" # Note that this defaults to first name is Mickey, last name is Mouse -- you could change that!
    return p

@app.route('/newresult',methods = ['POST', 'GET'])
def res2():
    if request.method == 'GET':
        newresult = request.args
        first = newresult.get('firstname')
        newnumm = newresult.get('number')
        age = 2017 - int(newnumm)
        newage= str(age)
        #return render_template("result.html",result = result)
        return "<b>" + first + "</b> <i>" + str("was born in ") + newage + str("!") + "</i>" 


if __name__ == '__main__':
    app.run()