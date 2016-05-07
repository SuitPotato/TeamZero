import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

#################################################################################
# Handler for creating a new knowledge item. Tasks are fetched from the datastore
# and then passed into the new_knowledge html. There, they are presented in a drop
# down menu during association, if the user chooses to associate the new knowledge
# item with an existing task.
# 
# Either way, information is gathered by new_knowledge html and passed to 
# item_input.py handler via the /created method
#################################################################################
class NewKnowledge(BaseHandler):
    def get(self):
        user = users.get_current_user() 
        items = Item.query().filter(Item.type == 'Task').order(-Item.date).fetch()
        
        template_values = {
        	'items':items,
        	'user':user
        }
        self.render("new_knowledge.html", (template_values))