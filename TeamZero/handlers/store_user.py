import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

#################################################################################
# Handler for showing all knowledge and task items that are assigned to a user.
# Reached by clicking the "Welcome,<user_name>" button on the top nav-bar. All
# task and knowledge items are fetched from the datastore and passed to store.html
# where they are displayed.
#################################################################################
class StoreUser(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().filter(Item.owner == user.email()).filter(Item.type == "Task").order(-Item.date).fetch()
		items += Item.query().filter(Item.owner == user.email()).filter(Item.type == "Knowledge").order(-Item.date).fetch()

		template_values = {
			'items':items,
                        'user':user
		}
		self.render("user_store.html", (template_values))
