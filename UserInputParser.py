#!/usr/bin/python
# -*- coding: utf-8 -*-

from PageConstructor import PageConstructor
from DataSource import DataSource
from Bill import Bill
from Senator import Senator
from Committee import Committee

class UserInputParser:
	#Constructor that stores params internally for later calling as well
	#as calling setPageType() so the class knows what it will be trying to
	#return later
	def __init__(self, params):
		self.page_type = params['page_type']
		self.params = params
		self.page_maker = PageConstructor()
		self.db_source = DataSource()


	#Based on the page_type it grabs the relevant variables from params
	#(with potential for throwing an invalid user input exception). The class
	#then uses those variables from params to querey Database.py to grab the
	#requested information and feed it to page_maker to build the page.
	#Then returns the html from page_maker. (note much logic occurs here.
	#If there is a search query in the user input it calls billSearchCuller
	#to remove from the list any bills that do not meet the criteria after
	#the database search. 
	def generateHtmlPageOutput(self):
		html_string = ""
		#The extra bits on the conditionals check that we're actually given a
		#specific senator/state/bill by the CGI parameters. If not, it'll just
		#go into the else.
		if self.page_type == "senator" and self.params["senator"] != "":
			html_string += self.makeSenatorPage()
		elif self.page_type == "bill" and self.params["bill"] != "":
			html_string += self.makeBillPage()
		#state should be listed as a 2-letter abbr. - e.g. MA, VT, WI
		elif self.page_type == "state" and len(self.params["state"]) == 2:
			html_string += self.makeStatePage()
		elif self.page_type == "committee" and self.params["committee"] != "":
			html_string += self.makeCommitteePage()
		elif self.page_type == "session" and self.params["session"] != "":
			html_string += self.makeSessionPage()
		elif self.page_type == "bill_index":
			html_string += self.makeBillIndexPage()
		elif self.page_type == "home":
			html_string += self.makeHomePage()
		else:
			html_string += self.makeErrorPage()	
			#TODO make an error page, figure out where all of it fits.
			#This is the hub, and any major errors should come to this
			#method eventually, so this else might be a great place to
			#generate an error page. Maybe call PageConstructor to make one?
		return html_string

	#The "make" methods all do about the same thing, but with enough
	#variations that it'd be a pain to make them all one. They get the major
	#info we need from the database, then call the requisite PageConstructor
	#method to make the page, after which they get it back as a string and
	#return it.
	#For Senators, Bills & Committees, the object returned by DataSource.py
	#will be an object of the appropriate type; otherwise, it'll be a list of
	#objects.
	def makeSenatorPage(self):
		id_tag = self.params["senator"]
		senator_obj = self.db_source.getSenatorWithCommittees(id_tag)
		self.page_maker.makeSenatorPage(senator_obj)
		html_string = self.page_maker.getPage()
		return html_string

	def makeBillPage(self):
		id_tag = self.params["bill"]
		bill_obj = self.db_source.getBillWithVotes(id_tag)
		self.page_maker.makeBillPage(bill_obj)
		html_string = self.page_maker.getPage()
		return html_string

	def makeBillIndexPage(self):
		bill_list = self.db_source.getBillList()
		self.page_maker.makeBillIndexPage()
		html_string = self.page_maker.getPage()
		return html_string

	def makeStatePage(self):
		state_name = self.params["state"]
		senator_list = self.db_source.getSenatorsInState(state_name)
		self.page_maker.makeStatePage(state_name, senator_list)
		html_string = self.page_maker.getPage()
		return html_string

	def makeCommitteePage(self):
		committee_id = self.params["committee"]
		committee_obj = self.db_source.getCommitteeWithMembers(committee_id)
		self.page_maker.makeCommitteePage(committee_obj)
		html_string = self.page_maker.getPage()
		return html_string

	def makeSessionPage(self):
		session_id = self.params["session"]
		senator_list = self.db_source.getSenatorsInSession(session_id)
		bill_list = self.db_source.getBillsInCongress(session_id, 0)
		#The 0 argument specifies that we want all bills rather than a given
		#number of them.
		self.page_maker.makeSessionPage(session_id,senator_list,bill_list)
		html_string = self.page_maker.getPage()
		return html_string

	def makeHomePage(self):
		self.page_maker.makeHomepage()
		html_string = self.page_maker.getPage()
		return html_string

	def makeErrorPage(self):
		self.page_maker.makeErrorPage()
		html_string = self.page_maker.getPage()
		return html_string		