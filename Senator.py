#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgitb
cgitb.enable()

class Senator:
	#Constructor that builds a senator object from the senators id and an 
	#array of string parameters containing the variables from the senator as
	#generated by the database interface
	#birthday might be a date?
	def __init__(self, params):
		self.id = params[0]
		self.last = params[1]
		self.first = params[2]
		self.birthday = params[3]
		self.gender = params[4]
		self.state = params[5]
		self.party = params[6]
		self.wiki = params[7]
		self.current = params[8] #Boolean value, true means a current senator
		self.committees = []
		#if there is a 9th argument in params then it indicates that a list has
		#committee objects from the database and will thus store them
		if len(params) == 10:
			self.committees = params[9]

	#Generates a link to the senator’s page with the properly formatted text and
	#returns it as a string(e.g. (R-AK) Richard White ).

	def getStateLink(self):
		htmlLink = ('<a href = "http://thacker.mathcs.carleton.edu/cs257/emeryj/index.py?page_type=state&state='
			+ self.getState() + '">' + self.getState() + '</a>')
		return htmlLink

	def getSenatorLink(self):
		str_id = str(self.getId())
		htmlLink = ('<a href = "http://thacker.mathcs.carleton.edu/cs257/emeryj/index.py?page_type=senator&senator='
			+ str_id + '">' + self.getName() + '</a>')
		return htmlLink

	def getFirst(self):
		return self.first

	def getBirthday(self):
		return self.birthday

	def getLast(self):
		return self.last

	def getName(self):
		return self.first + " " + self.last

	def getId(self):
		return self.id

	def getState(self):
		return self.state

	def isCurrent(self):
		return self.current

	def getParty(self):
		return self.party

	def getCommittees(self):
		return self.committees