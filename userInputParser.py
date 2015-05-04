#!/usr/bin/python
# -*- coding: utf-8 -*-

class userInputParser:
	#Constructor that stores params internally for later calling as well
	#as calling setPageType() so the class knows what it will be trying to
	#return later
	def __init__(self, params):
		this.page_type = this.setPageType()
		this.params = params
		this.page_constructor = PageConstructor()
	
	#Reads the page variable from the passed by the user and figures out what
	#page_type the webapp should try to generate. It will also create a new
	#PageConstructor object with the proper type of page primed and stored as
	#a page_constructor variable
	def setPageType(self):
		#do things

	#Based the page_type it grabs the relevant variables from params
	#(with potential for throwing an invalid user input exception). The class
	#then uses those variables from params to querey Database.py to grab the
	#requested information and feed it to page_constructor to build the page.
	#Then returns the html from page_constructor. (note much logic occurs here.
	#If there is a search query in the user input it calls billSearchCuller
	#to remove from the list any bills that do not meet the criteria after
	#the database search. 
	def generateHtmlPageOutput(self):
		HtmlString = ""
		return HtmlString

	#Takes a list of bills and a search criteria and returns a new list of bills
	#(empty list if none meet the criteria) with everything that meets the
	#criteria. (ex. takes a list of bills from the 114th congress and returns
	#only the bills that “John Snow” voted on)
	def billSearchCuller(self, bill_list, search_param):
		culled_array = []
		return culled_array
