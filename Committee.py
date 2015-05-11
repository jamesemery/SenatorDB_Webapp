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
			self.senators = []

	#Generates an Html link to this committee's page.
	def getCommitteeLink(self):
		return ""

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getSuperCommittee(self):
		return self.super_committee

	def getSession(self):
		return self.session

	def getSenators(self):
		return self.senators
