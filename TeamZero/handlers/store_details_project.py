import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

#################################################################################
# Handler for displaying details of a specific project
#################################################################################
class StoreDetailsProject(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().filter(Item.type == "Project").order(-Item.date).fetch()

		template_values = {
			'items':items,
            'user':user
		}
		self.render("details_project.html", (template_values))