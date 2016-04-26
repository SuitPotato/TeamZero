import webapp2
from google.appengine.api import users
from handlers import BaseHandler

class PushPage(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("push.html", {"user": user})


