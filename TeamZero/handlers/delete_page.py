import webapp2
import re

from google.appengine.api import users
from handlers import BaseHandler
from models import Item

##################################################################
# Handler for deleting an item from the datastore. A key string called
# ditem is passed from a mouse click into this handler and the
# matching item from the datstore is found, to be passed into
# the delete page
#
##################################################################
class DeletePage(BaseHandler):
    def get(self):
    	user = users.get_current_user()
    	items = Item.query().order(-Item.date).fetch()
    	ditem = self.request.get('ditem')
    	match = re.search(r'(\d+)',ditem).group(0)

    	for item in items:
    		key = item.key
    		id = re.search(r'(\d+)',str(key)).group(0)
    		if id == match:
    			passitem = item
    			
    	# this was a test but doesn't work
    	#passitem.delete()
        
        #self.render("delete.html", {"passitem": passitem})
        self.render("delete.html", {"ditem": ditem})
