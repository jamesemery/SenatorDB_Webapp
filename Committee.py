#!/usr/bin/python
# -*- coding: utf-8 -*-

class Committee:

	def __init__(self, params):
		this.id = params[0]
		this.name = params[1]
		this.super_committee = params[2]
		this.session = params[3]
		this.senators = params[4]

	#Generates an Html link to this committee's page.
	def generateCommitteeLink(self):
		return ""

	def getId(self):
		return this.id

	def getName(self):
		return this.name

	def getSuperCommittee(self):
		return this.super_committee

	def getSession(self):
		return this.session

	def getSenators(self):
		return this.senators
