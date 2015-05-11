#!/usr/bin/python
# -*- coding: utf-8 -*-

#Although it's kind of a pain, the drop-down menus in the header need to make
#database calls.
from DataSource import DataSource
from Bill import Bill
from Senator import Senator
from Committee import Committee

class PageConstructor:
	STATE_LIST = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
		'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',
		'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
		'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
		'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
		'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
		'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
		'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
		'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
		'West Virginia', 'Wisconsin', 'Wyoming']

	#Constructor that builds a PageConstructor object and an empty string for
	#the page.
	def __init__(self):
		self.page = ""
		self.replacements = {} #the various inserts that will be created
		self.dbSource = DataSource() #we'll need a bit of data from the database

	#Method that reads headerTemplate.html and makes changes to it based on
	#page_type (for example filling in breadcrumbs) then adds it to
	#the beginning of page.
	def readTemplate(self, page_type):

		templateFile = open("template.html", r)
		templateString = templateFile.read()
		self.page += templateString

		#Senator Dropdown Menu via replacement
		senators_by_state_html = ""
		for state in STATE_LIST:
			#TODO make the links work correctly.
			senators_by_state_html += ('<li><a href = "link to the state">'
				+ state + '</a></li>')
		self.replacements["SenatorDropdown"] = senators_by_state_html

		#Bill Dropdown Menu via replacement
		bill_list = self.dbSource.getBillList()
		self.replacements["BillDropdown"] = ""
		for i in range(20):
			self.replacements["BillDropdown"] += '<li>' +
				bill_list[i].getBillLink() + '</li>'

		#Committee Dropdown Menu via replacement
		committee_list = self.dbSource.getCommitteeBySession(114)
		self.replacements["CommitteeDropdown"] = ""
		for entry in committee_list:
			self.replacements["CommitteeDropdown"] += '<li' +
				entry.getCommitteeLink() + </li>
		#doesn't return anything, just makes changes to the page field.

	#TODO
	#MAKE SURE ALL MAKEPAGE FUNCTIONS CALL READTEMPLATE AND GIVE TYPE

	#Just opens Homepage.html. Simple as that. The page is complete, so we're
	#not bothering to read from the template.
	def makeHomepage(self):
		pageFile = open("Homepage.html", r)
		pageString = pageFile.read()
		self.page += pageString

	#Gets html from billPageTemplate.html, fills in the info of the bill passed
	#to it, and appends to the page variable. 
	def makeBillPage(self, bill):
		self.readTemplate()
		#do stuff

	#Gets html from committeeTemplate.html, fills in info, and appends to the 
	#page variable.
	def makeCommitteePage(self, committee):
		self.readTemplate()
		#do stuff

	#Gets html from senatorPageTemplate.html, fills in the senator’s info, and
	#appends to the page variable.
	def makeSenatorPage(self, senator):
		self.readTemplate()
		#do stuff

	def makeSenatorIndexPage(self, senator_list):
		self.readTemplate()
		#do stuff

	#Gets html from statePageTemplate.html, fills in the state name and senator
	#list, and appends to the page variable.
	def makeStatePage(self, state_name, senator_list):
		self.readTemplate()
		#do stuff

	#Gets html from congressPage.html and adds into it a list of all the
	#senators from the session and the last few bills from the session 
	def makeSessionPage(self, session_id,senator_list,bill_list):
		self.readTemplate()

	#Makes a page with a big list of all bills ever.
	def makeBillIndexPage(self, bill_list):
		self.readTemplate()

	#Gets a general-purpose error page.
	def makeErrorPage(self):
		self.readTemplate()


	#Returns the finished page.
	def getPage(self):
		#TODO insert the various replacements.
		return self.page