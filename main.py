from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/signin')
def signin():
    return render_template("signin.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/homie')
def homie():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
