import webapp2
from google.appengine.api import users
from handlers import BaseHandler

#################################################################################
# Handler to call success_delete.html as confirmation that a task was 
# successfully deleted.
#################################################################################
class SuccessDelete(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.render("success_delete.html", {"user": user})


