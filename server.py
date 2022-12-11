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

@app.route('/users/<int:id>')
def show_one(id):
    one_user = User.get_one({'id':id})
    return render_template("read_one.html", one_user=one_user)

@app.route('/users/create', methods=["POST"])
def create_user():
    id = User.create(request.form)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/edit')
def edit_users_form(id):
    data = { 'id' : id }
    one_user = User.get_one(data)
    return render_template("edit.html", one_user=one_user)

@app.route('/users/<int:id>/update', methods=["POST"])
def edit_user(id):
    data = {
        'id' : id,
        **request.form
    }
    User.update(data)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    User.delete({'id':id})
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)