import webapp2
import re

from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class DeletePage(BaseHandler):
    def get(self):
    	user = users.get_current_user()
    	items = Item.query().order(-Item.date).fetch()
    	ditem = self.request.get('ditem')
    	#match = re.search(r'(\d+)',citem).group(0)

#    	for item in items:
#    		key = item.key
#    		id = re.search(r'(\d+)',str(key)).group(0)
#    		if id == match:
#    			passitem = item
        
        #self.render("delete.html", {"passitem": passitem})
        self.render("delete.html", {"ditem": ditem})
