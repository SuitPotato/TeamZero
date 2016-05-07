import webapp2
from google.appengine.api import users
from handlers import BaseHandler

#################################################################################
# Handler for creating a new project item. Information is gathered by new_project
# html and passed to item_input.py handler via the /created method
#################################################################################
class NewProject(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("new_project.html", {"user": user})
        
        
