import webapp2
from google.appengine.api import users
from handlers import BaseHandler

class NewKnowledge(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("new_knowledge.html", {"user": user})
        
        
