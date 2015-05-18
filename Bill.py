#!/usr/bin/python
# -*- coding: utf-8 -*-

#import cgitb
#cgitb.enable()

class Bill:
    """An object that stores the database's information on a bill."""
    
    def __init__(self, params):
        # Takes a given ordered list of strings generated by the database
        # interface and generates an object.
        # (This leaves vote_tally empty by default)
        self.id = params[0]
        self.session_of_congress = params[1]
        self.roll = params[2]
        self.vote_date = params[3]
        self.type = params[4]
        self.question = params[5]

        if len(params)!=6:
            self.yea_votes = params[6]
            self.nay_votes = params[7]
            self.abstaining = params[8]
            self.absent = params[9]
        else:
            self.yea_votes = []
            self.nay_votes = []
            self.abstaining = []
            self.absent = []

    def getBillLink(self):
        # Generates an HTML link to the bill’s page and returns it as a
        # properly formatted string.
        HTML_string = ('<a href = "index.py?page_type=bill&bill=' +
                       str(self.getId()) + '">' + self.getQuestion() + '</a>')
        return HTML_string

    def getId(self):
        return self.id

    def getSession(self):
        return self.session_of_congress

    def getSessionLink(self):
        HTML_string = ('<a href = "index.py?page_type=session&session=' +
                       str(self.getSession()) + '">' + str(self.getSession()) +
                       '<sup>th</sup>' + '</a>')
        return HTML_string

    def getRoll(self):
        return self.roll

    def getVoteDate(self):
        return self.vote_date

    def getType(self):
        return self.type

    def getQuestion(self):
        return self.question

    def getYea_Votes(self):
        return self.yea_votes

    def getNay_Votes(self):
        return self.nay_votes

    def getAbstaining(self):
        return self.abstaining

    def getAbsent(self):
        return self.absent