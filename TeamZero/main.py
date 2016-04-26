#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from handlers import IndexPage, NewItem, LoginPage, ItemInput, LogoutPage
from handlers import NewTask, NewKnowledge
from handlers import About, LoggedInPage, LoggedOutPage, Success
from handlers import StoreHandler, StoreUser, StoreKnowledge, StoreTask, StoreDetails
from handlers import StoreProject
from handlers import DeletePage, EditPage, FinishedPage, PushPage, ArchivePage, AssociatePage

app = webapp2.WSGIApplication([
    ('/newitem', NewItem),
    ('/newtask', NewTask),
    ('/newknowledge', NewKnowledge),
    ('/', IndexPage),
    ('/login', LoginPage),
    ('/logout', LogoutPage),
    ('/created', ItemInput),
    ('/about', About),
    ('/loggedin', LoggedInPage),
    ('/loggedout', LoggedOutPage),
	('/success', Success),
	('/store', StoreHandler),
	('/userprofile', StoreUser),
	('/knowledge', StoreKnowledge),
	('/task', StoreTask),
	('/details', StoreDetails),
	('/project', StoreProject),
	('/delete', DeletePage),
	('/edit', EditPage),
	('/finished', FinishedPage),
	('/push', PushPage),
	('/archive', ArchivePage),
	('/associate', AssociatePage)
	
], debug=True)
