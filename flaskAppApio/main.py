from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import kw1

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    name = current_user.name
    return render_template('profile.html', name=current_user.name)

@main.route('/app1')
@login_required
def app1():
    return render_template('jumbotron.html')

@main.route('/app2')
@login_required
def app2():
    return render_template('blog.html')

@main.route('/app3')
@login_required
def app3():
    return render_template('records.html')

@main.route('/app4')
@login_required
def app4():
    keywords_listx = kw1.query.order_by(kw1.id).all()
    return render_template('form.html', keywords_list = keywords_listx)

@main.route('/app4', methods=['POST'])
@login_required
def app4_post():
    keywordx = request.form.get('keywordn')
    new_kw1 = kw1(kw1_name=keywordx)
    db.session.add(new_kw1)
    db.session.commit()
    return redirect('/app4')
    # return render_template('form.html')


# redirect returns a 302 header to the browser, with its Location header as the URL for the index function. render_template returns a 200, with the index.html template returned as the content at that
# https://stackoverflow.com/questions/21668481/difference-between-render-template-and-redirect




