from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def my_form_post38():
    if request.method == 'POST':
        text1 = request.form["username"]
        text2 = request.form["email"]
        if request.form['btn'] == "auto":
            password = "abcdefghijklmnopqrstwxyz1234567890$%&*()?"

            for x in range(1):
                pwd = ""
                for a in range(10):
                    pwd = pwd + random.choice(password)
                return render_template('login.html', ans=pwd, ans1=text1, ans2=text2)


if __name__ == '__main__':
    app.run()