#!/usr/bin/python
# -*- coding: utf-8 -*-

#mport cgitb
#cgitb.enable()

import datetime
from datetime import date

class Senator:
    """An object that stores the database's information on a senator."""

    def __init__(self, params):
        # Takes a given ordered list of strings generated by the database
        # interface and generates an object.
        self.id = params[0]
        self.last_name = params[1]
        self.first_name = params[2]
        self.birthday = params[3]
        self.gender = params[4]
        self.state = params[5]
        self.party = params[6]
        self.wiki = params[7]
        self.bool_is_current = params[8]

        if len(params) == 10:
            self.committees = params[9]
        else:
            self.committees = []

    def getStateLink(self):
        # Generates an HTML link to the senator's state's page and returns it as
        # a properly formatted string.
        HTML_string = ('<a href = "index.py?page_type=state&state='
                       + self.getState() + '">' + self.getState() + '</a>')
        return HTML_string

    def getSenatorLink(self):
        # Generates an HTML link to the senator's page and returns it as a
        # properly formatted string.
        HTML_string = ('<a href = "index.py?page_type=senator&senator='
                       + str(self.getId()) + '">' + self.getName() + '</a>')
        return HTML_string

    def getFirst(self):
        return self.first_name

    def getBirthday(self):
        # if the the date was interpreted by SQL as being in the 21st century
        # then it will return a fixed date corresponding to the year in the
        # 20th century
        if (self.birthday!=None):
            if (self.birthday >= date(2000, 1, 1)):
                self.birthday = date(self.birthday.year - 100, self.birthday.month, self.birthday.day)
        return self.birthday

    def getWikiLink(self):
        wiki_string = ""
        if self.wiki != "":
            wiki_string =  ('<a href = "https://en.wikipedia.org/wiki/' +
                self.wiki + '">' + self.wiki + '</a>')
        return wiki_string

    def getLast(self):
        return self.last_name

    def getName(self):
        return self.first_name + " " + self.last_name

    def getId(self):
        return self.id

    def getState(self):
        return self.state

    def isCurrent(self):
        return self.bool_is_current

    def getParty(self):
        return self.party

    def getCommittees(self):
        return self.committees