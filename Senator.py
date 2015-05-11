#!/usr/bin/python
# -*- coding: utf-8 -*-

class Senator:
	#Constructor that builds a senator object from the senators id and an 
	#array of string parameters containing the variables from the senator as
	#generated by the database interface
	#birthday might be a date? ot
	def __init__(self, params):
		self.id = params[0]
		self.last = params[1]
		self.first = params[2]
		self.birthday = params[3]
		self.gender = params[4]
		self.party = params[5]
		self.wiki = params[6]
		self.current = params[7] #Boolean value, true means a current senator
		self.committees = []
		#if there is a 9th argument in params then it indicates that a list has
		#committee objects from the database and will thus store them
		if len(params) == 9:
			self.committees = params[8]

	#Generates a link to the senator’s page with the properly formatted text and
	#returns it as a string(e.g. (R-AK) Richard White ).
	def getSenatorLink(self):
		htmlLink = "<a href = 'http://thacker.mathcs.carleton.edu/cs257/emeryj/index.py?page_type=senator&senator'" + self.getId() + ">" + self.getName() + "</a>"
		return htmlLink

	def getId(self):
		return self.id

	def getFirst(self):
		return self.first

	def getLast(self):
		return self.last

	def getName(self):
		return self.first + " " + self.last

	def getBirthday(self):
		return self.birthday

	def getGender(self):
		return self.gender

	def getParty(self):
		return self.party

	def getWiki(self):
		return self.wiki

	def isCurrent(self):
		return self.current

	def getCommittees(self):
		return self.committees