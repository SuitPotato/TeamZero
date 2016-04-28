import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class AssignUsers(BaseHandler):
    def get(self):
        user = users.get_current_user() 
        self.render("assign_users.html", {"user":user})