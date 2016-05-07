import webapp2
from google.appengine.api import users
from handlers import BaseHandler
from models import Item

# Handler for assigning users to an item
# Want to change this to pass in all users and present them within a drop-down in assign_users.html
class AssignUsers(BaseHandler):
    def get(self):
        user = users.get_current_user() 
        self.render("assign_users.html", {"user":user})