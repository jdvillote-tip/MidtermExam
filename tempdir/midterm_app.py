from flask import Flask, request, render_template, redirect

sample = Flask(__name__)

@sample.route("/")
def main():
    return redirect('/login', code =302)

@sample.route('/login')
def login():
    return render_template('login.html')

@sample.route('/register')
def register():
    return render_template('register.html')

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5000)   