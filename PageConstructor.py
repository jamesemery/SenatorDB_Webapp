#!/usr/bin/python
# -*- coding: utf-8 -*-

class PageConstructor:

	#Constructor that builds a PageConstructor object and calls fillHeader(self)
	#to add the common interface parts to page
	def __init__(self):
		self.page = ""
		self.fillHeader()

	#Method that reads headerTemplate.html and makes changes to it based on
	#page_type (for example graying out the current page link) then adds it to
	#the beginning of page
	def fillHeader(self):
		headerFile = open("headerTemplate.html", r)
		headerString = headerFile.read()
		self.page += headerString
		#doesn't return anything, just makes changes to the page field.

	#Gets html from homepageTemplate.html, fills in a list of the most recent
	#senatorial activity, then appends the now-complete html for the homepage
	#to the page variable. 
	def getHomepage(self):
		#do stuff

	#Gets html from billPageTemplate.html, fills in the info of the bill passed
	#to it, and appends to the page variable. 
	def getBillPage(self, bill):
		#do stuff

	#Gets html from committeeTemplate.html, fills in info, and appends to the 
	#page variable.
	def getCommitteePage(self, committee):
		#do stuff

	#Gets html from senatorPageTemplate.html, fills in the senator’s info, and
	#appends to the page variable.
	def getSenatorPage(self, senator):
		#do stuff

	#Gets html from statePageTemplate.html, fills in the state name and senator
	#list, and appends to the page variable.
	def getStatePage(self, state_name, senator_list):
		#do stuff

	#Gets html from allStatesPage.html (literally a list of states) and appends
	#it to the page variable. 
	def getAllStatesPage(self): 
		#do stuff

	#Gets html from congressPage.html and adds into it a list of all the
	#senators from the session and the last few bills from the session 
	def getSessionPage(self, session_id,senator_list,bill_list):

	#Gets a general-purpose error page.
	def getErrorPage(self):

	#Returns the finished page.
	def displayPage(self):
		return self.page