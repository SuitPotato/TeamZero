import webapp2
import re

from google.appengine.api import users
from handlers import BaseHandler
from models import Item

class KnowledgeDetails(BaseHandler):
	def get(self):
		user = users.get_current_user()
		items = Item.query().filter(Item.type == 'Knowledge').order(-Item.date).fetch()
		citem = self.request.get('citem')
		match = re.search(r'(\d+)',citem).group(0)
		
		for item in items:
			key = item.key
			id = re.search(r'(\d+)',str(key)).group(0)
			if id == match:
				passitem = item

		template_values = {
			'items':items,
            'user':user,
            'passitem':passitem
		}
		self.render("details_knowledge.html", (template_values))