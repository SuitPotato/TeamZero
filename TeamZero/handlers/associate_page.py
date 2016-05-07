import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

##################################################################
# Handler for associating a knowledge item to a task item
# All task items from the datastore are fetched and presented to
# the user in a drop-down within associate page
##################################################################
class AssociatePage(BaseHandler):
    def get(self):
        user = users.get_current_user() 
        items = Item.query().filter(Item.type == 'Task').order(-Item.date).fetch()
        
        template_values = {
        	'items':items,
        	'user':user
        }
        self.render("associate.html", (template_values))