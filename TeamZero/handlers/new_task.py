import webapp2
from google.appengine.api import users
from handlers import BaseHandler

class NewTask(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("new_task.html", {"user": user})
        
        
