import webapp2
from google.appengine.api import users
from handlers import BaseHandler

#################################################################################
# Handler for editing an item
#################################################################################
class EditPage(BaseHandler):
    def get(self):
    	# TODO: implement code for edit, includes fetching the specific item
    	# from the datastore, passing it to edit.html, getting new info from
    	# the user, saving that info to the datastore, and confirming success
        user = users.get_current_user()
        self.render("edit.html", {"user": user})


