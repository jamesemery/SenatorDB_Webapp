#!/usr/bin/python
# -*- coding: utf-8 -*-

class UserInputParser:
	#Constructor that stores params internally for later calling as well
	#as calling setPageType() so the class knows what it will be trying to
	#return later
	def __init__(self, params):
		this.page_type = params['page_type'].value
		this.params = params
		this.page_maker = PageConstructor()
		this.dbSource = DataSource()


	#Based on the page_type it grabs the relevant variables from params
	#(with potential for throwing an invalid user input exception). The class
	#then uses those variables from params to querey Database.py to grab the
	#requested information and feed it to page_maker to build the page.
	#Then returns the html from page_maker. (note much logic occurs here.
	#If there is a search query in the user input it calls billSearchCuller
	#to remove from the list any bills that do not meet the criteria after
	#the database search. 
	def generateHtmlPageOutput(self):
		htmlString = ""
		#The extra bits on the conditionals check that we're actually given a
		#specific senator/state/bill by the CGI parameters. If not, it'll just
		#go into the else.
		if this.page_type == "senator" and this.params["senator"] != "":
			htmlString += this.makeSenatorPage()
		elif this.page_type == "bill" and this.params["bill"] != "":
			htmlString += this.makeBillPage()
		elif this.page_type == "state" and len(this.params["state"]) = 2:
			htmlString += this.makeStatePage()
		elif this.page_type == "committee" and this.params["committee"] != "":
			htmlString += this.makeCommitteePage()
		elif this.page_type == "session" and this.params["session"] != "":
			htmlString += this.makeSessionPage()
		elif this.page_type == "home":
			htmlString += this.makeHomePage()
		else:
			#TODO make an error page, figure out where all of it fits.
			#This is the hub, and any major errors should come to this
			#method eventually, so this else might be a great place to
			#generate an error page. Maybe call PageConstructor to make one?
		return htmlString


	def makeSenatorPage(self):
		idTag = this.params["senator"]
		senatorObj = Senator(this.dbSource.getBiographyForSenator(idTag))
		this.page_maker.fillContent("senator", senatorObj)
		htmlString = this.page_maker.displayPage()
		return htmlString

	def makeBillPage(self):
		idTag = this.params["bill"]
		billObj = Bill(this.dbSource.getBillBiography(idTag))
		this.page_maker.fillContent("bill", billObj)
		htmlString = this.page_maker.displayPage()
		return htmlString

	def makeStatePage(self):
		stateName = this.params["state"]
		senatorList = this.dbSource.getSenatorsInState(stateName)
		this.page_maker.fillContent("state", senatorList)
		htmlString = this.page_maker.displayPage()
		return htmlString

	def makeCommitteePage(self):
		htmlString = ""
		return htmlString

	def makeSessionPage(self):
		htmlString = ""
		return htmlString

	def makeHomePage(self):
		htmlString = ""
		return htmlString		

	#Takes a list of bills and a search criteria and returns a new list of bills
	#(empty list if none meet the criteria) with everything that meets the
	#criteria. (ex. takes a list of bills from the 114th congress and returns
	#only the bills that “John Snow” voted on)
	def billSearchCuller(self, bill_list, search_param):
		#TODO this. I'm not quite sure how it works or when we're using it.
		culled_array = []
		return culled_array
