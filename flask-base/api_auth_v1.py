from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

#from: J5bIPtEbS0Q

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey21'

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token')

		if not token:
			return jsonify({'message':'Token is missing'}), 403

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message':'token is invalid'}), 403

		return f(*args, **kwargs)

	return decorated

@app.route('/unprotected')
def unprotected():
	return jsonify({'message': 'Anyone can see this'})

@app.route('/protected')
@token_required
def protected():
	return jsonify({'message':'this is available for users with valid tokens'})

@app.route('/login')
def login():
	auth = request.authorization

	if auth and auth.password == 'secret1':
		token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, app.config['SECRET_KEY'])

		return jsonify({'token': token.decode('UTF-8')})

	return make_response('Could not verify', 401, {'WWW-authenticate':'Basic realm="Login Required"'})



if __name__ == '__main__':

	app.run(debug=True)

