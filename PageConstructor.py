#!/usr/bin/python
# -*- coding: utf-8 -*-

class PageConstructor:

	#Constructor that builds a PageConstructor object and stores what type of 
	#page this constructor is building then calls fillHeader(self) to add the
	#common interface parts to page
	def __init__(self, page_type):
		#do stuff

	#Method that reads headerTemplate.html and makes changes to it based on
	#page_type (for example graying out the current page link) then adds it to
	#the beginning of page
	def fillHeader(self):
		#doesn't return anything, just makes changes to the page field.

	#Checks the page type and calls the appropriate method to fill the main
	#content of the page.
	def fillContent(self):
		#do stuff

	#Gets html from homepageTemplate.html, fills in a list of the most recent
	#senatorial activity, then appends the now-complete html for the homepage
	#to the page variable. 
	def getHomepage(self,bill_list):
		#do stuff

	#Gets html from billPageTemplate.html, fills in the info of the bill passed
	#to it, and appends to the page variable. 
	def getBillPage(self,Bill bill):
		#do stuff

	#Gets html from billComparisonTemplate.html, fills in the info of the two
	#bills, and appends to the page variable. (both parameters are Bill objects)
	def getBillComparisonPage(self,bill_one, bill_two):
		#do stuff

	#Generates the html formatting for a given search query page and adds it to
	#the already partially filled in page variable then returns the html code
	#for the page 

	#NOT SURE ABOUT THE PARAMS FOR THIS ONE...
	def getBillSearchQueryPage(self,bill_list,Senator=empty):
		#do stuff

	#Gets html from senatorPageTemplate.html, fills in the senator’s info, and
	#appends to the page variable.
	def getSenatorPage(self, senator):
		#do stuff

	#Gets html from statePageTemplate.html, fills in the state name and senator
	#list, and appends to the page variable.
	def getStatePage(self, stateName, senator_list):
		#do stuff

	#Gets html from allStatesPage.html (literally a list of states) and appends
	#it to the page variable. 
	def getAllStatesPage(self): 
		#do stuff

	#Gets html from congressPage.html and adds into it a list of all the
	#senators from the congress and the last few bills from the congress 
	def getCongressPage(self, int congress,senator_list,bill_list):

	#Prints the finished html page to standard output.
	def displayPage(self):
		#do stuff