#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgitb
cgitb.enable()

class Session:
    """An object that stores the database's information on a session."""

    def __init__(self, params):
        # Takes a given ordered list of strings generated by the database
        # interface and generates an object.
        self.id = params[0]
        self.start_date = params[1]
        self.end_date = params[2]
        self.senators = params[3]
        self.bills = params[4]
        self.committees = params[5]

    def getId(self):
    	return self.id

    def getStart_Date(self):
    	return self.start_date

    def getEnd_Date(self):
    	return self.end_date

    def getSenators(self):
    	return self.senators

    def getBills(self):
    	return self.bills

    def getCommittees(self):
    	return self.committees