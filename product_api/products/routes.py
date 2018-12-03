from product_api import app,db
from product_api.models import Product
from flask_rest_jsonapi import Api,ResourceList,ResourceDetail
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

api = Api(app)

class ProductSchema(Schema):
	class Meta:
		type_ = 'product'
		self_view = 'product_detail'
		self_view_kwargs = {'id':'<id>'}
		self_view_many = 'products'		
	
	id = fields.Integer(as_string=True, dump_only=True)
	name = fields.Str(required=True, dump_only=True)	

class ProductList(ResourceList):    	
	schema = ProductSchema
	data_layer = {'session': db.session,'model': Product}	
	
class ProductDetail(ResourceDetail):	
	schema = ProductSchema
	data_layer = {'session':db.session,'model':Product}	

api.route(ProductList, 'products', '/products')
api.route(ProductDetail, 'product_detail', '/products/<int:id>', '/products/<int:product_id>')