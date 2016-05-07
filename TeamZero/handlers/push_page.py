import webapp2
import re

from google.appengine.api import users
from handlers import BaseHandler
from models import Item

#################################################################################
# Handler for pushing an item to a user (assigning it to them). Key data for the
# item clicked on to be pushed is passed into this handler. The matching item
# from the datastore is found and passed to push.html, which gathers information
# from the user of which user to push the item to. Once the "Submit" button is
# clicked in the push.html page, another handler will be called to make the
# changes to the item in the datastore.
#################################################################################
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
