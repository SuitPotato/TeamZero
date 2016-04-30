import webapp2
import re

from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class TaskDetails(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().filter(Item.type == 'Task').order(-Item.date).fetch()
		citem = self.request.get('citem')
		match = re.search(r'(\d+)',citem).group(0)
		
		for item in items:
			key = item.key
			id = re.search(r'(\d+)',str(key)).group(0)
			if id == match:
				passitem = item

# stuff that didnt work:
		#citem = Item.query('agxkZXZ-dGVhbXplcm9yEQsSBEl0ZW0YgICAgIDQhwgM')
		#itemkey = item.key()
		#Key('Item', 4572319104106496)	
		#item = Item.query().filter('__key__' == match)
		#item = Item.get_by_key_name(match)
		#item = Item.get_by_id(match)

		template_values = {
			'items':items,
            'user':user,
            'passitem':passitem
		}
		
		self.render("details_task.html", (template_values))