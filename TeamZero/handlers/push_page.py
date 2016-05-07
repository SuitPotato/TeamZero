import webapp2
import re

from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class PushPage(BaseHandler):					
	def get(self):
		items = Item.query().fetch()
		pitem = self.request.get('pitem')
		match = re.search(r'(\d+)',pitem).group(0)

		for item in items:
			key = item.key
			id = re.search(r'(\d+)',str(key)).group(0)
			if id == match:
				passitem = item
    	
		user = users.get_current_user()
		self.render("push.html", {"passitem": passitem})
