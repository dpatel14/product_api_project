from product_api import app,db
from product_api.models import ProductLog
from product_api.forms import ProductLogForm
from flask import request,render_template, url_for, flash, redirect
from flask_rest_jsonapi import Api,ResourceList,ResourceDetail
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
import requests
import json

api = Api(app)

class ProductLogSchema(Schema):
	class Meta:
		type_ = 'productlog'
		self_view = 'productlog_detail'
		self_view_kwargs = {'id':'<id>'}
		self_view_many = 'productlogs'
	
	id = fields.Integer(as_string=True, dump_only=True)
	longitude= fields.Float(required=True,dump_only=True)
	latitude= fields.Float(required=True,dump_only=True)
	elevation= fields.Integer(required=True,dump_only=True)
	
@app.route('/productlog/new', methods=['GET','POST'])
def new_product_log():  
	form = ProductLogForm()	
	if request.method == 'GET':		
		return render_template('create_productlog.html', title='New Product Log',form=form)	
	else:
		if form.validate_on_submit():
			url = 'http://127.0.0.1:5000/productlog/add'
			payload = {'longitude': form.longitude.data,'latitude':form.latitude.data,'elevation':form.elevation.data}
			headers = {'content-type': 'application/json'}
			r = requests.post(url, data=json.dumps(payload), headers=headers)		
			return redirect(url_for('productlogs'))	
			
@app.route('/productlog/add', methods=['POST'])
def add_product_log():  	
	req_data = request.get_json(force=True)
	longitude = req_data['longitude']
	latitude = req_data['latitude']	
	elevation = req_data['elevation']
	new_product_log = ProductLog(posted_date=None,longitude=longitude,latitude=latitude,elevation=elevation)
	db.session.add(new_product_log)
	db.session.commit()
	flash('Product Log has been created..!!','success')	
	return redirect(url_for('productlogs'))		

@app.route("/productlogs/<int:id>/update",methods=['GET','POST'])
def update_productlog(id):
	productlog = ProductLog.query.get_or_404(id)	
	form = ProductLogForm()		
	
	if request.method == 'GET':				
		form.longitude.data = productlog.longitude		
		form.latitude.data = productlog.latitude
		form.elevation.data = productlog.elevation				
			
	elif form.validate_on_submit():
		productlog.longitude = form.longitude.data
		productlog.latitude = form.latitude.data
		productlog.elevation = form.elevation.data			
		db.session.commit()
		flash('Product Log has been updated..!!','success')
		return redirect(url_for('productlog_detail',id=productlog.id))
	
	return render_template('create_productlog.html', title='Update Log',form=form,legend='Update Post')	
		
@app.route("/productlogs/<int:id>/delete",methods=['GET','POST'])
def delete_productlog(id):
	productlog = ProductLog.query.get_or_404(id)		
	db.session.delete(productlog)
	db.session.commit()
	flash('Product Log has been deleted..!!','success')
	return redirect(url_for('productlogs'))		
	
class ProductLogList(ResourceList):	    
	schema = ProductLogSchema
	data_layer = {'session':db.session,'model':ProductLog}	
	
class ProductLogDetail(ResourceDetail):	
	schema = ProductLogSchema
	data_layer = {'session':db.session,'model':ProductLog}	

api.route(ProductLogList, 'index', '/')
api.route(ProductLogList, 'home', '/home')
api.route(ProductLogList, 'productlogs', '/productlogs')
api.route(ProductLogDetail, 'productlog_detail', '/productlogs/<int:id>', '/productlogs/<int:productlog_id>')