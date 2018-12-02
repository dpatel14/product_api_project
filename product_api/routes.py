from product_api import app,db,ma
from product_api.models import Product

from flask_rest_jsonapi import Api,ResourceList

from sqlalchemy import event, DDL
from sqlalchemy.event import listen

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

@app.route("/")
def home():
	return "HILLO"
	
class ProductSchema(Schema):
	class Meta:
		type_ = 'product'
		self_view = 'product_detail'
		self_view_kwargs = {'id':'<id>'}
		self_view_many = 'product_list'
	
	id = fields.Integer(as_string=True, dump_only=True)
	name = fields.Str(required=True, load_only=True)

class ProductList(ResourceList):
	schema = ProductSchema
	data_layer = {'session':db.session,'model':Product}	
	
api = Api(app)
api.route(ProductList, 'product_list', '/products')