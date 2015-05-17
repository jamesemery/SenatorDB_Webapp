#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgitb
cgitb.enable()

from PageConstructor import PageConstructor
from DataSource import DataSource
from Bill import Bill
from Senator import Senator
from Committee import Committee

class UserInputParser:
    """""" # TODO: Write a class description/doc/thing!

    def __init__(self, params):
        # A constructor that stores the provided parameters internally, as well
        # as calling both PageConstructor() and DataSource().
        self.page_type = params['page_type']
        self.params = params
        self.page_maker = PageConstructor()
        self.db_source = DataSource()

    def generateHtmlPageOutput(self):
        # Determines which type of page we're constructing, then calls the
        # appropriate make____Page() method to generate the HTML.
        HTML_string = ""

        # The extra bits on the conditionals check that it's actually given a
        # specific senator/state/bill by the CGI parameters. If not, it'll just
        # go into the else.
        if self.page_type == "senator" and self.params["senator"] != "":
            HTML_string += self.makeSenatorPage()
        elif self.page_type == "bill" and self.params["bill"] != "":
            HTML_string += self.makeBillPage()
        elif self.page_type == "state" and len(self.params["state"]) == 2:
            # State should be listed as the abbreviation.
            HTML_string += self.makeStatePage()
        elif self.page_type == "committee" and self.params["committee"] != "":
            HTML_string += self.makeCommitteePage()
        elif self.page_type == "session" and self.params["session"] != "":
            HTML_string += self.makeSessionPage()
        elif self.page_type == "bill_index":
            HTML_string += self.makeBillIndexPage()
        elif self.page_type == "senator_index":
            HTML_string += self.makeSenatorIndexPage()
        elif self.page_type == "home":
            HTML_string += self.makeHomePage()
        else:
            HTML_string += self.makeErrorPage()
            
        return HTML_string

    # The "make" methods all do about the same thing, but with enough
    # variations that it'd be a pain to make them all one. They get the major
    # info we need from the database, then call the requisite PageConstructor
    # method to make the page, after which they get it back as a string and
    # return it.
    # 
    # For Senators, Bills & Committees, the object returned by DataSource.py
    # will be an object of the appropriate type; otherwise, it'll be a list of
    # objects.
    def makeSenatorPage(self):
        id_tag = self.params["senator"]
        senator_obj = self.db_source.getSenatorWithCommittees(id_tag)
        senator_vote_pair = self.db_source.getVotesBySenator(id_tag,20)
        self.page_maker.makeSenatorPage(senator_obj,senator_vote_pair)
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeSenatorIndexPage(self):
        senator_list = self.db_source.getSenatorList()
        self.page_maker.makeSenatorIndexPage(senator_list)
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeBillPage(self):
        id_tag = self.params["bill"]
        bill_obj = self.db_source.getBillWithVotes(id_tag)
        self.page_maker.makeBillPage(bill_obj)
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeBillIndexPage(self):
        bill_list = self.db_source.getBillList()
        self.page_maker.makeBillIndexPage(bill_list)
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeStatePage(self):
        state_name = self.params["state"]
        senator_list = self.db_source.getSenatorsInState(state_name)
        self.page_maker.makeStatePage(state_name, senator_list)
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeCommitteePage(self):
        committee_id = self.params["committee"]
        committee_obj = self.db_source.getCommitteeWithMembers(committee_id)
        self.page_maker.makeCommitteePage(committee_obj)
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeSessionPage(self):
        session_id = self.params["session"]
        senator_list = self.db_source.getSenatorsInSession(session_id)
        bill_list = self.db_source.getBillsInCongress(session_id, 0)
        # The 0 argument specifies that we want all bills rather than a certain
        # number of them.
        self.page_maker.makeSessionPage(session_id,senator_list,bill_list)
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeHomePage(self):
        self.page_maker.makeHomepage()
        HTML_string = self.page_maker.getPage()
        return HTML_string

    def makeErrorPage(self):
        self.page_maker.makeErrorPage()
        HTML_string = self.page_maker.getPage()
        return HTML_string      