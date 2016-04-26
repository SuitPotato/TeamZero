import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class NewKnowledge(BaseHandler):
    def get(self):
        user = users.get_current_user() 
        items = Item.query().filter(Item.type == 'Task').order(-Item.date).fetch()
        
        template_values = {
        	'items':items,
        	'user':user
        }
        self.render("new_knowledge.html", (template_values))