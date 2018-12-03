from product_api import app
from product_api.models import ProductLog
from flask import request,jsonify
from flask_rest_jsonapi import Api

import json
api = Api(app)

# PAGINATION API
	
@app.route('/productlogs/page')
def view_paginated_list():
	return jsonify(get_paginated_list(
		ProductLog, 
		'productlogs/page', 
		start=request.args.get('start', 1), 
		limit=request.args.get('limit', 4)
	))

def get_paginated_list(klass, url, start, limit):        
    results = klass.query.all()
    count = len(results)
    if (count < start):
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    
	# finally extract result according to bounds    
    obj['results'] = []
	  
    result_list = results[(start - 1):(start - 1 + limit)]
    for result in result_list:        
        obj['results'].append(
			{		
				"attributes": {
					"elevation": result.elevation, 
					"latitude": result.latitude, 
					"longitude": result.longitude
				}, 
			"id": result.id, 
			}
		)           
    return obj