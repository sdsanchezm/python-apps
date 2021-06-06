from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_security import Security, SQLAlchemyUserDatastore, login_required, UserMixin, RoleMixin
from flask_security.utils import hash_password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SECURITY_PASSWORD_SALT'] = 'thisisasecretsalt'

db = SQLAlchemy(app)

'''
To run de database:
$ python
>> from app import db
>> db.create_all()
'''

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

# model to store users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# model to store the links
class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	content2 = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return'<Task %r>' % self.id

'''
@app.route('/', methods=['POST','GET'])
def hello_world():
	return render_template('index.html') 
'''
@app.route('/', methods=['POST','GET'])
@login_required
def index():
	if request.method == 'POST':
		task_content = request.form['content']
		task_description = request.form['content2']
		new_task = Todo(content=task_content, content2=task_description)

		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue adding your task'
	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html', tasks=tasks)

@app.route('/template')
def template1():
	return render_template('base_template.html')

@app.route('/delete/<int:id>')
@login_required
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')
	except:
		return 'There was a problem deleting the task'
		
@app.route('/update/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
	task = Todo.query.get_or_404(id)
	if request.method == 'POST':
		task.content = request.form['content']

		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue updating our task '
	else:
		return render_template('update.html', task=task)

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_datastore.create_user(
            email=request.form.get('email'),
            password=hash_password(request.form.get('password'))
        )
        db.session.commit()

        return redirect(url_for('profile'))

    return render_template('register.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('register.html'))

# login documentation:
# https://flask-login.readthedocs.io/en/latest/#how-it-works

if __name__ == "__main__":
	app.run(debug=True)

