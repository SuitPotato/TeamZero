import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

#################################################################################
# Handler for displaying details of each project, reached by clicking "Projects"
# tab in the left sidebar
#################################################################################
class StoreProject(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().filter(Item.type == 'Project').order(-Item.date).fetch()

		template_values = {
			'items':items,
            'user':user
		}
		self.render("project_store.html", (template_values))