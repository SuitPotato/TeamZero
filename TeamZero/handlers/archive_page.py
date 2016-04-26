import webapp2
from google.appengine.api import users
from handlers import BaseHandler

class ArchivePage(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("archive.html", {"user": user})


