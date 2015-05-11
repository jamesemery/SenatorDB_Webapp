#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgitb
cgitb.enable()

class Committee:

	def __init__(self, params):
		self.id = params[0]
		self.name = params[1]
		self.super_committee = params[2]
		self.session = params[3]
		if (len(params) == 5):
			self.senators = params[4]
		else:
			self.senators = [[]] #[[SenObj, name], [SenObj, name]]

	#Generates an Html link to this committee's page.
	def getCommitteeLink(self):
		return '<a href = "index.py?page_type=committee&committee=' + str(self.getId()) + '">' + self.getName() + '</a>'

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getSuperCommittee(self):
		return self.super_committee

	def getSuperCommitteeLink(self):
		return '<a href = "index.py?page_type=committee&committee=' + str(self.getSuperCommittee()) + '">' + 'Super-Committee' + '</a>'

	def getSession(self):
		return self.session

	def getSenators(self):
		return self.senators
