<<<<<<< HEAD
## main guide: https://github.com/PrettyPrinted/building_user_login_system/tree/master/finish 
## 8aTnmsDMldY 
from flask import Flask, render_template, url_for, redirect, Response, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# model
db = SQLAlchemy(app)

# declaring models in flask: 
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
'''
class users1(db.Model):
    id = db.Column( db.Integer, primary_key=True)
    username = db.Column( db.String(80), unique = True)
    password = db.Column( db.String(60), unique = True)
    email = db.Column( db.String(80), nullable = False, unique = True)
    integer21 = db.Column( db.Integer, )
    text21 = db.Column( db.Text)
    datetime21 = db.Column( db.DateTime, )
    float21 = db.Column( db.Float )
    boolean21 = db.Column( db.Boolean )
    pickleType21 = db.Column( db.PickleType )
    largeBinary21 = db.Column( db.LargeBinary, )
'''

class timeRecord_model(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	activity_name = db.Column(db.String(200), nullable=False)
	activity_level = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return'<Activity %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temp')
def test():
    return render_template('temp.html', supervar='ok ok')


@app.route('/timeRecord', methods=['POST','GET'])
def timeRecord():
    if request.method == 'POST':
        activity_name = request.form['activity_name1']
        activity_level = request.form['activity_level1']
        new_activity = timeRecord_model(activity_name=activity_name, activity_level=activity_level)
		
        try:
            db.session.add(new_activity)
            db.session.commit()
            return redirect('/timeRecord')
        except:
            return 'There was an issue adding your activity'
    else:
        activities = timeRecord_model.query.order_by(timeRecord_model.date_created).all()
        return render_template('timeRecord.html', activities=activities)


'''
@app.route('/login')
def login()
    return 'ok login'

@app.route('/signup')
def signup()
    return 'ok signup'

@app.route('/logout')
def logout()
    return 'ok logout'
'''

if __name__ == '__main__':
    app.run(debug = True)
=======
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

class user1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)

@app.route('/a', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        usernameval = request.form['username']
        new_username = user1(username=usernameval)
        try:
            db.session.add(new_username)
            db.session.commit()
            return redirect('/a')
        except:
            return 'Error, try again'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> a09c254de1cb24b6ddfb9c4ab9cd2046d77c6b5e
