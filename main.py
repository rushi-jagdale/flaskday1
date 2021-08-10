from flask import Flask

app = Flask(__name__)

@app.route('/add')
def add():
    a =20
    b= 30
    c = a +b 
    return "add %d"%c

@app.route('/name/<name>')
def names(name):
    return "your name is ,"+name;

@app.route('/ages/<age>')
def age(age):
    return "your age is ,"+age;

if __name__ == "__main__":
   app.run(debug = True,port=3000)   