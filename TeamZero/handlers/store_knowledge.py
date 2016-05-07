import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

#################################################################################
# Handler for showing only knowledge items that are assigned to a user.
# Reached by clicking the "Knowledge List" button on the left sidebar. All
# knowledge items are fetched from the datastore and passed to knowledge_store.html
# where they are displayed.
#################################################################################
class StoreKnowledge(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().filter(Item.type == 'Knowledge').order(-Item.date).fetch()

		template_values = {
			'items':items,
            'user':user
		}
		self.render("knowledge_store.html", (template_values))