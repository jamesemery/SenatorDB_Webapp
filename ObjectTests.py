#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from Bill import Bill
from Senator import Senator
from Committee import Committee

#Unit tests for the three concrete classes - 
#Bill, Senator, and Committee.
class ObjectTests(unittest.TestCase):
	
	####Constructor Tests####
	#Each of the classes has a short and a long form of the constructor;
	#In practice, this boils down to whether we're getting the object as
	#the subject of an entire page, or just a short blurb to put on
	#another object's page.

	def testBillConstructorShort(self):
		params = [100, 113, 2, "3/5/2012", "bill", "Question"]
		bill = Bill(params)
		self.assertEqual(bill.getId(), 100)
		self.assertEqual(bill.getSession(), 113)
		self.assertEqual(bill.getRoll(), 2)
		self.assertEqual(bill.getVoteDate(), "3/5/2012")
		self.assertEqual(bill.getType(), "bill")
		self.assertEqual(bill.getQuestion(), "Question")
		#we don't have a simple getter for these, so we're grabbing them directly
		self.assertEqual(bill.yea_votes, [])
		self.assertEqual(bill.nay_votes, [])
		self.assertEqual(bill.abstaining, [])
		self.assertEqual(bill.absent, [])

	def testBillConstructorLong(self):
		#The last 4 parameters should be lists of Senator objects, but b/c of
		#Python's typing it doesn't matter for testing purposes. We're just
		#making them strings.
		params = [100, 113, 2, "3/5/2012", "bill", "Question", 
					["Rich White", "Richard Whiter"],
					["John Brown"],
					[],
					["George Washington"]]
		bill = Bill(params)
		self.assertEqual(bill.getId(), 100)
		self.assertEqual(bill.getSession(), 113)
		self.assertEqual(bill.getRoll(), 2)
		self.assertEqual(bill.getVoteDate(), "3/5/2012")
		self.assertEqual(bill.getType(), "bill")
		self.assertEqual(bill.getQuestion(), "Question")
		self.assertEqual(bill.yea_votes, ["Rich White", "Richard Whiter"])
		self.assertEqual(bill.nay_votes, ["John Brown"])
		self.assertEqual(bill.abstaining, [])
		self.assertEqual(bill.absent, ["George Washington"])

	def testCommitteeConstructorShort(self):
		params = [100, "Committee to Discuss Commit Messages in Git",
			"super-committee", 113] #The super-committee should be another
			#Committee object, but the type isn't actually going to matter for
			#testing purposes
		com = Committee(params)
		self.assertEqual(com.getId(), 100)
		self.assertEqual(com.getName(), "Committee to Discuss Commit Messages in Git")
		self.assertEqual(com.getSuperCommittee(), "super-committee")
		self.assertEqual(com.getSession(), 113)
		self.assertEqual(com.getSenators(), [])

	def testCommitteeConstructorLong(self):
		#Same thing with super-committee as in the first constructor test.
		params = [100, "Committee to Discuss Commit Messages in Git",
			"super-committee", 113, ["sen1", "sen2", "sen3"]]
		com = Committee(params)
		self.assertEqual(com.getId(), 100)
		self.assertEqual(com.getName(), "Committee to Discuss Commit Messages in Git")
		self.assertEqual(com.getSuperCommittee(), "super-committee")
		self.assertEqual(com.getSession(), 113)
		self.assertEqual(com.getSenators(), ["sen1", "sen2", "sen3"])

	def testSenatorConstructorShort(self):
		params = [10, "White", "Rich", "05/12/2015", "Male", "Republican",
			"WikiURL", True]
		senator = Senator(params)
		self.assertEqual(senator.getId(), 10)
		self.assertEqual(senator.getLast(), "White")
		self.assertEqual(senator.getFirst(), "Rich")
		self.assertEqual(senator.getBirthday(), "05/12/2015")
		self.assertEqual(senator.getGender(), "Male")
		self.assertEqual(senator.getParty(), "Republican")
		self.assertEqual(senator.getWiki(), "WikiURL")
		self.assertEqual(senator.isCurrent(), True)
		self.assertEqual(senator.getCommittees(), [])

	def testSenatorConstructorLong(self):
		#A list of Committee objects should theoretically go in the last entry,
		#but we're using strings for test purposes.
		params = [10, "White", "Rich", "05/12/2015", "Male", "Republican",
			"WikiURL", True, ["Committee", "Committee 2", "Committee 3"]]
		senator = Senator(params)
		self.assertEqual(senator.getId(), 10)
		self.assertEqual(senator.getLast(), "White")
		self.assertEqual(senator.getFirst(), "Rich")
		self.assertEqual(senator.getBirthday(), "05/12/2015")
		self.assertEqual(senator.getGender(), "Male")
		self.assertEqual(senator.getParty(), "Republican")
		self.assertEqual(senator.getWiki(), "WikiURL")
		self.assertEqual(senator.isCurrent(), True)
		self.assertEqual(senator.getCommittees(), ["Committee", "Committee 2", "Committee 3"])

	####Link Generator Tests####
	#Each class has a method that generates a link to that object's page, of
	#the form <a href="URL"> Object Name </href> or similar.

	def testCommitteeLinkGenerator(self):
		htmlLink = "thisWillFail"
		params = [100, "Committee to Discuss Commit Messages in Git",
			"super-committee", 113, ["sen1", "sen2", "sen3"]]
		com = Committee(params)
		self.assertEqual(com.getCommitteeLink(), htmlLink)

	def testBillLinkGenerator(self):
		htmlLink = "thisWillFail"
		params = [100, 113, 2, "3/5/2012", "bill", "Question"]
		bill = Bill(params)
		self.assertEqual(bill.getBillLink(), htmlLink)

	def testSenatorLinkGenerator(self):
		htmlLink = "thisWillFail"
		params = [10, "White", "Rich", "05/12/2015", "Male", "Republican",
			"WikiURL", True, ["Committee", "Committee 2", "Committee 3"]]
		senator = Senator(params)
		self.assertEqual(senator.getSenatorLink(), htmlLink)

	def testBillVoteTally(self):
		#because Python doesn't care about typing, we're just going to pass in
		#strings instead of Senator objects for testing purposes. The method
		#should work the same either way.
		params = [100, 113, 2, "3/5/2012", "bill", "Question", 
					["Rich White", "Richard Whiter"],
					["John Brown"],
					[],
					["George Washington"]]
		bill = Bill(params)
		expected = [["Rich White", "Richard Whiter", "John Brown", "George Washington"],
					["Yea", "Yea", "Nay", "Absent"]]
		self.assertEqual(bill.getVoteTally(), expected)






if __name__ == '__main__':
    unittest.main()