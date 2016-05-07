import webapp2
import re

from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class ItemDelete(BaseHandler):
	def get(self):
		items = Item.query().order(-Item.date).fetch()
		ditem = self.request.get('ditem')
#		match = re.search(r'(\d+)',ditem).group(0)
#		
#		for item in items:
#			key = item.key
#			id = re.search(r'(\d+)',str(key)).group(0)
#			if id == match:
#				deleteitem = item
#
#		# Delete the item
#		deleteitem.delete

		test_values = {
			'ditem':ditem,
		}

		self.redirect('success_delete',(test_values))
