from flask import redirect, render_template, url_for
from app import app
from app.models.db.db_model import User
from app.models.forms.user_form import UserForm
from app.services.session_scope import session_scope

@app.route('/users', methods=['GET'])
def getUsers():
    with session_scope() as session:
        users = session.query(User).all()
    return render_template('user/users.html', users=users)

@app.route('/user/register', methods=['GET','POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data
        )
        
        with session_scope() as session:
            session.add(new_user)
        return redirect(url_for('getUsers'))
    return render_template('user/create.html', form=form)