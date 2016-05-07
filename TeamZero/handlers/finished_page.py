import webapp2
from google.appengine.api import users
from handlers import BaseHandler

#################################################################################
# Handler for marking a task as finished
#################################################################################
class FinishedPage(BaseHandler):
    def get(self):
        user = users.get_current_user()
        # TODO: Will need to get specific item from user about which task to mark
        #       finished. Then, the item is not remove from the datastore, but 
        #       rather, it merely disappears from the user's task store
        self.render("finished.html", {"user": user})

