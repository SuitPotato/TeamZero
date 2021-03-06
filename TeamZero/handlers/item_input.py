import webapp2
from google.appengine.api import users
from models import Item
from handlers import BaseHandler

class ItemInput(webapp2.RequestHandler):
	def post(self):
		#Getting Inputs
		itemname=self.request.get("item_name")
		itemtype=self.request.get("item_type")
		itemdescription=self.request.get("item_description")
		itemassociation=self.request.get("item_association")
		
		
		#Placing data in model
		item=Item()
		item.name=itemname
		item.type=itemtype
		item.description=itemdescription
		item.association=itemassociation
		item.owner=users.get_current_user().email()
		
		item.put()
		self.redirect('success')
		
