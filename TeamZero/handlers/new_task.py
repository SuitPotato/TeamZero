import webapp2
from google.appengine.api import users
from handlers import BaseHandler

#################################################################################
# Handler for creating a new task item. Information is gathered by new_task
# html and passed to item_input.py handler via the /created method
#################################################################################
class NewTask(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("new_task.html", {"user": user})
        
        
