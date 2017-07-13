


def db_users(user_id, client, all=False):
	if all:
		return coll.find({})
	else:
		db = client.hackathon
		coll = db.users
		# print type(int(params[1]))
		return coll.find_one({"employee_id": int(params[1])})

def db_orders(orders, client, filter_params=None):
	db = client.hackathon
	coll = db.orders
	if not filter_params:
		orders = coll.find()
		return 


def db_items(params, client, all=False):
	db = client.hackathon
	coll = db.items
	if all:
		return coll.find({})
	else:
		return None

def db_user(params, client, all):
	
	db = client.hackathon
	coll = db.users
	if all:
		return coll.find({})
	else:
		return coll.find_one({'employee_id': int(params['employee_id'])})