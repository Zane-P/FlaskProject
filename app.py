from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return celsius + 'C = ' + str(fahrenheit) + 'F'


@app.route('/c/<fahrenheit>')
def fahrenheit_to_celsius(fahrenheit):
    celsius = (float(fahrenheit) - 32) * 5 / 9
    return fahrenheit + 'F = ' + str(celsius) + 'C'


if __name__ == '__main__':
    app.run()
