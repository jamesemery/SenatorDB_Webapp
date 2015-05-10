#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from Bill import Bill
from Senator import Senator
from Committee import Committee

#Unit tests for the three concrete classes - 
#Bill, Senator, and Committee.
class ObjectTests(unittest.testCase):

	def testBillConstructor(self):
		#do stuff

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

	def testCommitteeSecondConstructorLong(self):
		#Same thing with super-committee as in the first constructor test.
		params = [100, "Committee to Discuss Commit Messages in Git",
			"super-committee", 113, ["sen1", "sen2", "sen3"]]
		com = Committee(params)
		self.assertEqual(com.getId(), 100)
		self.assertEqual(com.getName(), "Committee to Discuss Commit Messages in Git")
		self.assertEqual(com.getSuperCommittee(), "super-committee")
		self.assertEqual(com.getSession(), 113)
		self.assertEqual(com.getSenators(), ["sen1", "sen2", "sen3"])

	def testSenatorConstructor(self):
		#do stuff

	def testCommitteeLinkGenerator(self):
		htmlLink = ""
		params = [100, "Committee to Discuss Commit Messages in Git",
			"super-committee", 113, ["sen1", "sen2", "sen3"]]
		com = Committee(params)
		self.assertEqual(com.getCommitteeLink(), htmlLink)

	def testBillLinkGenerator(self):
		htmlLink = ""

	def testSenatorLinkGenerator(self):

	def testBillVoteTally(self):
		#because Python doesn't care about typing, we're just going to pass in
		#strings instead of Senator objects for testing purposes. The method
		#should work the same either way.






if __name__ == '__main__':
    unittest.main()