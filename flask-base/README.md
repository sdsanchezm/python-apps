# Working with flask
## Experimental .md file as well, lol

This is a crud application using **flask** and additional *django project* will be created.
You can even [clone it, and see what I'm doing](http://github.com/sdsanchezm/flask-base-code)

![Just a Logo](/img/logo.png)
Format: ![Alt Text](url)


### Instructions tu run the application:
Taken from:[the flask quick start site](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart)

Create a new virtualenv called env1:
```
$ virtualenv env1
```

Activate your virtual env (inside the Script folder):
```
$ source ./activate 
```

Install flask:
```
$ pip3 install flask
```

Export the environmental variable in order to run flask (using the python web server):
```
$ export FLASK_APP=app.py
```

Run flask:
```
$ flask run
```

Or could use python directly as well to the app.py file:
$ python.exe app.py #this is in windows, in linux should be python app.py, it shall open in localhost:5000

To create the database:
1. install all required dependencies
2. open python
3. import the model (the name is db in this case):
```python
>> from app import db
```
4. create all the tables:
```python
>> db.create_all()
```


Get all dependencies:
```python
(env1) $ freeze > requirements.davs
```

Result:
click==7.1.2
Flask==1.1.2
Flask-SQLAlchemy==2.4.4
itsdangerous==1.1.0
Jinja2==2.11.2
jsonify==0.5
MarkupSafe==1.1.1
SQLAlchemy==1.3.18
Werkzeug==1.0.1



---
## Flask documentation:
1. https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/ 

---
Read more about Markdown at [Mastering Markdown Github page](https://guides.github.com/features/mastering-markdown/)
From:
Z1RJmh_OqeA
J5bIPtEbS0Q
