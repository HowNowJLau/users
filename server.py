from flask import Flask, render_template, redirect, request
from user_model import User
app = Flask(__name__)

@app.route('/')
def redirect_to_users():
    return redirect('/users')

@app.route('/users')
def show_users():
    all_users = User.get_all()
    return render_template("read_all.html", all_users=all_users)

@app.route('/users/new')
def new_users_form():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    User.create(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)