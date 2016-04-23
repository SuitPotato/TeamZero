import webapp2
from google.appengine.api import users
from models import Project
from handlers import BaseHandler

class ProjectInput(webapp2.RequestHandler):
	def post(self):
	
		#Getting Inputs
		projectname=self.request.get("project_name")
		
		#Project Type isn't required at the moment of the project.py model
		#Will remove when type is not needed whatsoever
		#projecttype=self.request.get("item_type")
		
		projectdescription=self.request.get("project_description")
		

##############################################################################################################		
		
		#Placing data in model
		project=Project()
		project.name=projectname
		
		#Same as above
		#project.type=projecttype
		
		project.description=projectdescription
		project.owner=users.get_current_user().email()
	
		project.put()
		self.redirect('success')
		