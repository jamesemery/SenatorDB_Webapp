#!/usr/bin/python
# -*- coding: utf-8 -*-

#Although it's kind of a pain, the drop-down menus in the header need to make
#database calls.
import cgitb
cgitb.enable()
from DataSource import DataSource
from Bill import Bill
from Senator import Senator
from Committee import Committee



class PageConstructor:
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

	STATE_ABBREVIATION_LIST = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC'
		, 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA'
		, 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ'
		, 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX'
		, 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

	#Constructor that builds a PageConstructor object and an empty string for
	#the page.



	def __init__(self):
		self.page = ""
		self.replacements = {} #the various inserts that will be created
		self.dbSource = DataSource() #we'll need a bit of data from the database

	#Method that reads headerTemplate.html and makes changes to it based on
	#page_type (for example filling in breadcrumbs) then adds it to
	#the beginning of page.
	def readTemplate(self):

		templateFile = open("Website/template.html", "r")
		templateString = templateFile.read()
		self.page += templateString

		#Senator Dropdown Menu via replacement
		senators_by_state_html = ""
		i = 0
		while i < len(STATE_LIST):
			senators_by_state_html += ('<li><a href = "http://thacker.mathcs.' + 'carleton.edu/cs257/emeryj/index.py?page_type=state&state=' 
				+ STATE_ABBREVIATION_LIST[i] + '">'
				+ STATE_LIST[i] + '</a></li>')
			i+=1

		self.replacements["SenatorDropdown"] = senators_by_state_html

		#Bill Dropdown Menu via replacement
		bill_list = self.dbSource.getBillsInCongress(114,20)
		self.replacements["BillDropdown"] = ""
		for entry in bill_list:
			self.replacements["BillDropdown"] += ('<li>' +
				entry.getBillLink() + '</li>')

		#Committee Dropdown Menu via replacement
		committee_list = self.dbSource.getCommitteeBySession(114)
		self.replacements["CommitteeDropdown"] = ""
		for entry in committee_list:
			self.replacements["CommitteeDropdown"] += ('<li>' +
				entry.getCommitteeLink() + "</li>")
		#doesn't return anything, just makes changes to the page field.

	#TODO
	#MAKE SURE ALL MAKEPAGE FUNCTIONS CALL READTEMPLATE AND GIVE TYPE

	#Just opens Homepage.html. Simple as that. The page is complete, so we're
	#not bothering to read from the template.
	def makeHomepage(self):
		self.readTemplate()
		pageFile = open("Website/BillPageTemplate.html", "r")
		pageString = pageFile.read()
		self.page += pageString



	#Gets html from billPageTemplate.html, fills in the info of the bill passed
	#to it, and appends to the page variable. 
	def makeBillPage(self, bill):
		self.readTemplate()
		billFile = open("Website/BillPageTemplate.html", "r")
		billString = billFile.read()

		votes = len(bill.getYea_Votes()) + " yea | " + len(bill.getNay_Votes()) + " nay | " + len(bill.getAbstaining()) + " abstain | " + len(bill.getAbsent()) + " absent"

		bill_table = ""
		for s in bill.getYea_Votes():
			bill_table += "<tr><td>Yea</td><td>" + s.getSenatorLink()
			bill_table += "</td><td>" + s.getParty()
			bill_table += "</td><td>" + s.getStateLink() + "</td></tr>"
		for s in bill.getNay_Votes():
			bill_table += "<tr><td>Nay</td><td>" + s.getSenatorLink()
			bill_table += "</td><td>" + s.getParty()
			bill_table += "</td><td>" + s.getStateLink() + "</td></tr>"
		for s in bill.getAbstaining():
			bill_table += "<tr><td>Abstain</td><td>" + s.getSenatorLink()
			bill_table += "</td><td>" + s.getParty()
			bill_table += "</td><td>" + s.getStateLink() + "</td></tr>"
		for s in bill.getAbsent():
			bill_table += "<tr><td>Absent</td><td>" + s.getSenatorLink()
			bill_table += "</td><td>" + s.getParty()
			bill_table += "</td><td>" + s.getStateLink() + "</td></tr>"

		fill_tags = {"BillName": bill.getQuestion(), "BillType": bill.getType(), "BillSession": bill.getSession(), "BillDate": bill.getVoteDate(), "BillVotes": votes, "SenatorTable": bill_table}
		content_string = billString.format(**fill_tags)
		self.replacements[results] = content_string

	#Gets html from committeeTemplate.html, fills in info, and appends to the 
	#page variable.
	def makeCommitteePage(self, committee):
		self.readTemplate()
		committeeFile = open("Website/CommitteePageTemplate.html", "r")
		committeeString = committeeFile.read()

		commitee_table = ""
		for s in commitee.getSenators():
			commitee_table += "<tr><td>" + s.getSenatorLink()
			commitee_table += "</td><td>" + s.getParty()
			commitee_table += "</td><td>" + s.getStateLink() + "</td></tr>"

		fill_tags = {"Supercommittee": committee.getSuperCommittee().getCommitteeLink(), "SenatorTable": committee_table}
		content_string = committeeString.format(**fill_tags)
		self.replacements[results] = content_string

	#Gets html from senatorPageTemplate.html, fills in the senator’s info, and
	#appends to the page variable.
	#Things to pass in: {SenatorData} and {BillTable}
	def makeSenatorPage(self, senator):
		self.readTemplate()
		templateFile = open("Website/SenatorPageTemplate.html", "r")
		subtemplateString = templateFile.read()
		subreplacements = {}


		#TODO get the committes working
		subreplacements["CommitteeMemberList"] = " "
		subreplacements["BillTable"] = " "

		subreplacements["SenatorName"] = senator.getName()
		subreplacements["SenatorParty"] = senator.getParty()
		subreplacements["SenatorBirthday"] = senator.getBirthday().strftime("%B %d, %Y")
		
		#getting the real state name for the senator
		i = STATE_ABBREVIATION_LIST.index(senator.getState())
		subreplacements["SenatorState"] = STATE_LIST[i]

		if senator.isCurrent() == True:
			subreplacements["Currently"] = "Currently in office."
		else:
			subreplacements["Currently"] = "Not Currently in Office"

		content_string = subtemplateString.format(**subreplacements)
		self.replacements["results"] = content_string
		page = page.format(**self.replacements)
		return page


	def makeSenatorIndexPage(self, senator_list):
		self.readTemplate()
		senatorIndexFile = open("Website/SenatorIndexPageTemplate.html", "r")
		senatorIndexString = senatorIndexFile.read()

		table_string = ""
		for senator in senator_list:
			table_string += "<tr><td>" + senator.getSenatorLink()
			table_string += "</td><td>" + senator.getParty()
			table_string += "</td><td>" + senator.getStateLink() + "</td></tr>"

		fill_tags = {"SenatorTable": table_string}
		content_string = senatorIndexString.format(**fill_tags)
		self.replacements[results] = content_string

	#Makes a page with a big list of all bills ever.
	#Things to pass in: {BillTableRows}
	def makeBillIndexPage(self, bill_list):
		self.readTemplate()
		billIndexFile = open("Website/BillIndexPageTemplate.html", "r")
		billIndexString = billIndexFile.read()

		table_string = ""
		for bill in bill_list:
			table_string += "<tr><td>" + bill.getVoteDate()
			table_string += "</td><td>" + bill.getRoll()
			table_string += "</td><td>" + bill.getBillLink() + "</td></tr>"

		fill_tags = {"BillData": table_string}
		content_string = billIndexString.format(**fill_tags)
		self.replacements[results] = content_string

	#Gets html from statePageTemplate.html, fills in the state name and senator
	#list, and appends to the page variable.
	def makeStatePage(self, state_name, senator_list):
		self.readTemplate()
		stateFile = open("Website/StatePageTemplate.html", "r")
		stateString = stateFile.read()

		table_string = ""
		for s in senator_list:
			table_string += "<tr><td>" + s.isCurrent()
			table_string += "</td><td>" + s.getSenatorLink()
			table_string += "</td><td>" + s.getParty() + "</td></tr>"

		fill_tags = {"StateName": state_name, "SenatorTable": table_string}
		content_string = stateString.format(**fill_tags)
		self.replacements[results] = content_string

	#Gets html from congressPage.html and adds into it a list of all the
	#senators from the session and the last few bills from the session 
	def makeSessionPage(self, session_id,senator_list,bill_list):
		self.readTemplate()
		sessionFile = open("Website/SessionPageTemplate.html", "r")
		sessionString = sessionFile.read()

		s_table_string = ""
		for s in senator_list:
			s_table_string += "<tr><td>" + s.getSenatorLink()
			s_table_string += "</td><td>" + s.getParty()
			s_table_string += "</td><td>" + s.getStateLink() + "</td></tr>"

		b_table_string = ""
		for b in bill_list:
			b_table_string += "<tr><td>" + b.getVoteDate()
			b_table_string += "</td><td>" + b.getRoll()
			b_table_string += "</td><td>" + b.getBillLink() + "</td></tr>"

		fill_tags = {"sessionID": session_id, "SenatorTable": s_table_string, "BillTable": b_table_string}
		content_string = sessionString.format(**fill_tags)
		self.replacements[results] = content_string

	#Gets a general-purpose error page.
	def makeErrorPage(self):
		self.readTemplate()
		errorFile = open("Website/ErrorPageTemplate.html", "r")
		errorString = errorFile.read()
		self.replacements["results"] = errorString

	#Returns the finished page.
	def getPage(self):
		self.page = self.page.format(**self.replacements)
		return self.page