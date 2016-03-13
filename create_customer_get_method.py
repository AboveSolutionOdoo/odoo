import json
from flask import Flask, jsonify, request


app = Flask(__name__)

api = erppeek.Client('http://localhost:8069')


api.login('admin','odoo123','SaiStores')


@app.route('/create_task/', methods=['GET'])
@crossdomain(origin='*')



def create_task():
	
	name = request.args.get('name')
	email = request.args.get('email')
	mobile = request.args.get('mobile')
	newid=api.create('res.partner',{"name":name,"mobile":mobile,"email":email})
	
	return jsonify({"id":newid})
	


if __name__ == '__main__':
	
	app.run(debug=True)	
	
	