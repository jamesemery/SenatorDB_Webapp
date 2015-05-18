#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgitb
cgitb.enable()

from DataSource import DataSource
from Bill import Bill
from Senator import Senator
from Committee import Committee
import datetime

class PageConstructor:
    """Contains all of the methods to access and fill out the HTML templates."""
    global STATE_LIST
    global STATE_ABBREVIATION_LIST
    STATE_LIST = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
        'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',
        'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
        'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
        'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
        'West Virginia', 'Wisconsin', 'Wyoming']

    STATE_ABBREVIATION_LIST = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE',
        'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
        'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
        'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    def __init__(self):
        # The constructor opens a connection to the database, creates an empty
        # string of HTML, and creates an empty dictionary to be filled with
        # database-specific replacements to the HTML templates.
        self.page = ""
        self.replacements = {}
        self.dbSource = DataSource()

    def readTemplate(self):
        # A method that reads template.html, adds the template to self.page, and
        # adds the HTML for the dropdown menus to self.replacements.
        templateFile = open("Website/template.html", "r")
        templateString = templateFile.read()
        self.page += templateString

        self.replacements["SenatorDropdown"] = ""
        i = 0
        while i < len(STATE_LIST):
            self.replacements["SenatorDropdown"] += (
                '<li><a href = "index.py?page_type=state&state=' 
                + STATE_ABBREVIATION_LIST[i] + '">'
                + STATE_LIST[i] + '</a></li>')
            i+=1

        # TODO: DELETE THIS before finishing!
        # 
        # bill_list = self.dbSource.getBillsInCongress(114,20)
        # self.replacements["BillDropdown"] = ""
        # for entry in bill_list:
        #     self.replacements["BillDropdown"] += ('<li>' +
        #         entry.getBillLink() + '</li>')

        committee_list = self.dbSource.getCommitteesBySession(114)
        self.replacements["CommitteeDropdown"] = ""
        for entry in committee_list:
            self.replacements["CommitteeDropdown"] += ('<li>' +
                entry.getCommitteeLink() + "</li>")

    def makeHomepage(self):
        # Gets HTML from HomepageTemplate.html and places it in the body of the
        # generated page.
        self.readTemplate()
        pageFile = open("Website/HomepageTemplate.html", "r")
        pageString = pageFile.read()
        self.replacements["results"] = pageString
 
    def makeBillPage(self, bill):
        # Gets HTML from BillPageTemplate.html, fills in the info of the bill
        # passed to it, and places it in the body of the generated page.
        self.readTemplate()
        billFile = open("Website/BillPageTemplate.html", "r")
        billString = billFile.read()

        session_link = ('<a href="index.py?page_type=session&session=' +
                        str(bill.getSession()) + '">' + str(bill.getSession()) +
                        "</a>")

        votes = (str(len(bill.getYea_Votes())) + " yea | " + 
                 str(len(bill.getNay_Votes())) + " nay | " +
                 str(len(bill.getAbstaining())) + " abstain | " + 
                 str(len(bill.getAbsent())) + " absent")

        # Loops through the vote data and adds to a dictonary based 
        # on the party of the senator with keyed values that correspond 
        # to the votes in order
        # all yea votes
        party_dict = {}
        for senator in bill.getYea_Votes():
            party_votes = party_dict.get(senator.getParty())
            if party_votes == None:
                party_dict[senator.getParty()] = [1,0,0,0]
            else:
                party_votes[0] = party_votes[0] + 1
                party_dict[senator.getParty()] = party_votes

        # all nay votes
        for senator in bill.getNay_Votes():
            party_votes = party_dict.get(senator.getParty())
            if party_votes == None:
                party_dict[senator.getParty()] = [0,1,0,0]
            else:
                party_votes[1] = party_votes[1] + 1
                party_dict[senator.getParty()] = party_votes

        # all abstaining votes
        for senator in bill.getAbstaining():
            party_votes = party_dict.get(senator.getParty())
            if party_votes == None:
                party_dict[senator.getParty()] = [0,0,1,0]
            else:
                party_votes[2] = party_votes[2] + 1
                party_dict[senator.getParty()] = party_votes

        # all absent votes
        for senator in bill.getAbsent():
            party_votes = party_dict.get(senator.getParty())
            if party_votes == None:
                party_dict[senator.getParty()] = [0,0,0,1]
            else:
                party_votes[2] = party_votes[2] + 1
                party_dict[senator.getParty()] = party_votes


        breakdown_string = ""
        for party in party_dict.iterkeys():
            breakdown_string += "<p>" + party + ": "
            breakdown_string += (str(party_dict.get(party)[0]) + " yea | " + 
                 str(party_dict.get(party)[1]) + " nay | " +
                 str(party_dict.get(party)[2]) + " abstain | " + 
                 str(party_dict.get(party)[3]) + " absent" + "</p>" )

        # Table headers: Vote | Senator | Party | State
        table_string = ""
        for s in bill.getYea_Votes():
            table_string += ('<tr><td class="col-xs-2">Yea</td>' + 
                             '<td class="col-xs-4">' + s.getSenatorLink() + 
                             '</td><td class="col-xs-3">' + s.getParty() + 
                             '</td><td class="col-xs-3">' + s.getStateLink() + 
                             '</td></tr>')
        for s in bill.getNay_Votes():
            table_string += ('<tr><td class="col-xs-2">Nay</td>' + 
                             '<td class="col-xs-4">' + s.getSenatorLink() + 
                             '</td><td class="col-xs-3">' + s.getParty() + 
                             '</td><td class="col-xs-3">' + s.getStateLink() + 
                             '</td></tr>')
        for s in bill.getAbstaining():
            table_string += ('<tr><td class="col-xs-2">Abstain</td>' + 
                             '<td class="col-xs-4">' + s.getSenatorLink() + 
                             '</td><td class="col-xs-3">' + s.getParty() + 
                             '</td><td class="col-xs-3">' + s.getStateLink() + 
                             '</td></tr>')
        for s in bill.getAbsent():
            table_string += ('<tr><td class="col-xs-2">Absent</td>' + 
                             '<td class="col-xs-4">' + s.getSenatorLink() + 
                             '</td><td class="col-xs-3">' + s.getParty() + 
                             '</td><td class="col-xs-3">' + s.getStateLink() + 
                             '</td></tr>')

        fill_tags = {"BillName": bill.getQuestion(),
                     "VotesBreakdown": breakdown_string,
                     "BillType": bill.getType(),
                     "BillSession": session_link,
                     "BillDate": bill.getVoteDate().strftime("%B %d, %Y"),
                     "BillVotes": votes,
                     "SenatorTable": table_string}

        content_string = billString.format(**fill_tags)
        self.replacements["results"] = content_string

    def makeCommitteePage(self, committee):
        # Gets HTML from CommitteePageTemplate.html, fills in the info of the
        # committee passed to it, and places it in the body of the generated
        # page.
        self.readTemplate()
        committeeFile = open("Website/CommitteePageTemplate.html", "r")
        committeeString = committeeFile.read()

        session_link = ('<a href="index.py?page_type=session&session=' +
                        str(committee.getSession()) + '">' +
                        str(committee.getSession()) + "</a>")

        # Table headers: Position | Senator | Party | State
        table_string = ""
        for senator_pair in committee.getSenators():
            # A senator_pair has a senator object at index 0 and a string
            # describing the senator's role in the committee at index 1.
            senator = senator_pair[0]
            table_string += ('<tr><td class="col-xs-3">' + senator_pair[1] + 
                             '</td><td class="col-xs-3">' +
                             senator.getSenatorLink() + '</td>' + 
                             '<td class="col-xs-3">' + senator.getParty() +
                             '</td><td class="col-xs-3">' + 
                             senator.getStateLink() + '</td></tr>')

        associated_string = ""
        if committee.isSuper():
            associated_list = committee.getAssociated()
            if len(associated_list)>0:
                associated_string += ("<h5>Sub-Committees:</h5>" + 
                                      '<ul id="committees">')

                for pair in associated_list:
                    associated_string += ('<li><a href = "index.py?' +
                                          "page_type=committee&committee='" +
                                          str(pair[0]) + '">' + str(pair[1]) +
                                          '</a></li>')
                associated_string += "</ul>"
        else:
            pair = committee.getAssociated()[0]
            associated_string += ("<p><strong>Super-Committee: </strong>" + 
                                  '<a href = "index.py?' + 
                                  "page_type=committee&committee='" + 
                                  str(pair[0]) + '">' + str(pair[1]) + '</a></p>')


        fill_tags = {"CommitteeName": committee.getName(),
                     "SessionNumber": session_link,
                     "Supercommittee": associated_string, 
                     "SenatorTable": table_string}
                     
        content_string = committeeString.format(**fill_tags)
        self.replacements["results"] = content_string

    def makeSenatorPage(self, senator, vote_pair_list):
        # Gets HTML from SenatorPageTemplate.html, fills in the info of the
        # senator passed to it, and places it in the body of the generated page.
        self.readTemplate()
        senatorFile = open("Website/SenatorPageTemplate.html", "r")
        senatorString = senatorFile.read()

        committee_list = ""
        for committee_pair in senator.getCommittees():
            # A committee_pair contains a committee object at index 0 and a
            # string detailing the senator's role at index 1.
            committee_list += ("<li>" + committee_pair[1] + " of the " +
                               committee_pair[0].getCommitteeLink() +
                               ' during Session <a href="index.py?page_type='
                               + 'session&session=' + 
                               str(committee_pair[0].getSession()) + '">' + 
                               str(committee_pair[0].getSession()) + "</a></li>")

        # Table headers: Date | Number | Bill Name | Vote
        table_string = ""
        for bill_pair in vote_pair_list:
            # A bill_pair contains a bill object at index 0 and a string of
            # the senator's vote at index 1.
            table_string += ('<tr><td class="col-xs-2">' + 
                             bill_pair[0].getVoteDate().strftime("%B %d, %Y") + 
                             '</td><td class="col-xs-2">' + 
                             str(bill_pair[0].getRoll()) + 
                             '</td><td class="col-xs-6">' + 
                             bill_pair[0].getBillLink() +
                             '</td><td class="col-xs-2">' + bill_pair[1] +
                             '</td></tr>')

        fill_tags = {"SenatorName": senator.getName(),
                     "SenatorParty": senator.getParty(),
                     "SenatorStateLink": senator.getStateLink(),
                     "Birthday": senator.getBirthday(),
                     "Currently": senator.isCurrent(),
                     "CommitteeMemberList": committee_list,
                     "BillTable": table_string}

        content_string = senatorString.format(**fill_tags)
        self.replacements["results"] = content_string

    def makeSenatorIndexPage(self, senator_list):
        # Gets HTML from SenatorIndexPageTemplate.html, fills in the table with
        # info on all of the senators, and places the HTML in the body of the
        # generated page.
        self.readTemplate()
        senatorIndexFile = open("Website/SenatorIndexPageTemplate.html", "r")
        senatorIndexString = senatorIndexFile.read()

        # Table headers: Senator | Party | State
        table_string = ""
        for senator in senator_list:
            table_string += ('<tr><td class="col-xs-4">' +
                             senator.getSenatorLink() +
                             '</td><td class="col-xs-4">' + senator.getParty() +
                             '</td><td class="col-xs-4">' +
                             senator.getStateLink() + '</td></tr>')

        fill_tags = {"SenatorTable": table_string}

        content_string = senatorIndexString.format(**fill_tags)
        self.replacements["results"] = content_string

    def makeBillIndexPage(self, bill_list):
        # Gets HTML from BillIndexPageTemplate.html, fills in the table with
        # info on all of the bills, and places the HTML in the body of the
        # generated page.
        self.readTemplate()
        billIndexFile = open("Website/BillIndexPageTemplate.html", "r")
        billIndexString = billIndexFile.read()

        # Table headers: Date | # | Bill
        table_string = ""
        for bill in bill_list:
            table_string += ('<tr><td class="col-xs-3">' + 
                             bill.getVoteDate().strftime("%B %d, %Y") +
                             '</td><td class="col-xs-3">' +
                             bill.getVoteDate().strftime("%Y") + " s" + 
                             str(bill.getRoll()) +
                             '</td><td class="col-xs-6">' + bill.getBillLink() +
                             '</td></tr>')

        fill_tags = {"BillData": table_string}

        content_string = billIndexString.format(**fill_tags)
        self.replacements["results"] = content_string

    def makeStatePage(self, state_name, senator_list):
        # Gets HTML from StatePageTemplate.html, fills in the table with
        # info on the state's senators, and places the HTML in the body of the
        # generated page.
        self.readTemplate()
        stateFile = open("Website/StatePageTemplate.html", "r")
        stateString = stateFile.read()

        # Table headers: Current? | Senator | Party
        table_string = ""
        for s in senator_list:
            table_string += ("<tr><td>" + str(s.isCurrent()) +
                             "</td><td>" + s.getSenatorLink() +
                             "</td><td>" + s.getParty() + "</td></tr>")

        full_state_name = STATE_LIST[STATE_ABBREVIATION_LIST.index(state_name)]
        fill_tags = {"StateName": full_state_name,
                     "SenatorTable": table_string}

        content_string = stateString.format(**fill_tags)
        self.replacements["results"] = content_string

    def makeSessionPage(self, session):
        # Gets HTML from SessionPageTemplate.html, fills in the two tables with
        # info on the session's senators and bills, and places the HTML in the
        # body of the generated page.
        self.readTemplate()
        sessionFile = open("Website/SessionPageTemplate.html", "r")
        sessionString = sessionFile.read()

        c_list_string = ""
        committee_list = session.getCommittees()
        for c in committee_list:
            if c.isSuper():
                c_list_string += ('<li>' + c.getCommitteeLink() + ' </li>')

        # Table headers: Senator | Party | State
        s_table_string = ""
        senator_list = session.getSenators()
        for s in senator_list:
            s_table_string += ("<tr><td>" + s.getSenatorLink() + 
                               "</td><td>" + s.getParty() + 
                               "</td><td>" + s.getStateLink() + "</td></tr>")

        # Table headers: Date | # | Bill
        b_table_string = ""
        bill_list = session.getBills()
        for b in bill_list:
            b_table_string += ("<tr><td>" + 
                               b.getVoteDate().strftime("%B %d, %Y") + 
                               "</td><td>" + str(b.getRoll()) + 
                               "</td><td>" + b.getBillLink() + "</td></tr>")

        fill_tags = {"sessionID": str(session),
                     "StartDate": session.getStart_Date().strftime("%B %d, %Y"),
                     "EndDate": session.getEnd_Date().strftime("%B %d, %Y"),
                     "CommitteeList": c_list_string,
                     "SenatorTable": s_table_string,
                     "BillTable": b_table_string}

        content_string = sessionString.format(**fill_tags)
        self.replacements["results"] = content_string

    def makeErrorPage(self):
        # Gets HTML from ErrorPageTemplate.html and places it in the body of the
        # generated page.
        self.readTemplate()
        errorFile = open("Website/ErrorPageTemplate.html", "r")
        errorString = errorFile.read()
        self.replacements["results"] = errorString

    def getPage(self):
        # When the appropriate make function has been called, this places the
        # edited body of the page in between the header and the footer, fleshes
        # out the menu dropdowns, and returns the finished page.
        self.page = self.page.format(**self.replacements)
        return self.page