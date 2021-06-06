from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

class kw1(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    keyword = db.Column(db.String(20), unique = True)

class kw2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    key_number = db.Column(db.Integer, )
    
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

    
@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == 'POST':
        keyword1 = request.form['keyword']
        k1_obj = kw1(keyword=keyword1)
        try:
            db.session.add(k1_obj)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error, try again!!!'
    else:
        return render_template('form.html')


@app.route('/')
def index():
    return '<html><a href="/form">/form</a><br><a href="/records">/records</a></html>'


@app.route('/jumbotron')
def jumbotron():
    return render_template('jumbotron.html')


@app.route('/records')
def records():
    records_db = kw1.query.order_by(kw1.id).all()
    return render_template('records.html', records_html = records_db)


@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__=='__main__':
    app.run(debug=True)
