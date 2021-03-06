#!/usr/bin/python
# -*- coding: utf-8 -*-

#import cgitb
#cgitb.enable()

class Committee:
    """An object that stores the database's information on a committee."""

    def __init__(self, params):
        # Takes a given ordered list of strings generated by the database
        # interface and generates an object.
        self.id = params[0]
        self.name = params[1]
        self.super_committee = params[2]
        self.session_of_congress = params[3]

        # [[SenObj, name], [SenObj, name]]
        if len(params) == 6:
        	#A list of Senator objects paired with their role;
        	#e.g. [[SenObj1, "Member"], [SenObj2, "Leader"]...]
            self.senators = params[4]
            #A list of lists, e.g. [[102, "Subcommittee1"], [103, "SC2"]...]
            self.associated = params[5] 
        else:
            self.senators = [[]]
            self.associated = [[]]

    def getCommitteeLink(self):
        # Generates an HTML link to the committee's page and returns it as a
        # properly formatted string.
        HTML_string = ('<a href = "index.py?page_type=committee&committee=' + 
                       str(self.getId()) + '">' + self.getName() + '</a>')
        return HTML_string

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getSuperCommittee(self):
        return self.super_committee

    def getSuperCommitteeLink(self):
        HTML_string = ('<a href = "index.py?page_type=committee&committee=' + 
                       str(self.getSuperCommittee()) + '">' + 'Super-Committee'
                       + '</a>')
        return HTML_string

    def getSession(self):
        return self.session_of_congress

    def getSenators(self):
        return self.senators

    def getAssociated(self):
        return self.associated

    def isSuper(self):
        # returns true if this committee is a super committee (i.e. super_committee == id)
        return (self.super_committee == self.id)