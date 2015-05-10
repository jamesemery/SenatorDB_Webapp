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

	def testCommitteeFirstConstructor(self):
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

	def testCommitteeSecondConstructor(self):
		#Same thing with super-committee as in the first constructor test.
		params = [100, "Committee to Discuss Commit Messages in Git",
			"super-committee", 113, ["sen1", "sen2", "sen3"]]
		com = Committee(params)
		self.assertEqual(com.getId(), 100)
		self.assertEqual(com.getName(), "Committee to Discuss Commit Messages in Git")
		self.assertEqual(com.getSuperCommittee(), "super-committee")
		self.assertEqual(com.getSession(), 113)
		self.assertEqual(com.getSenators(), ["sen1", "sen2", "sen3"])

	def testCommitteeLinkGenerator(self):
		htmlLink = ""
		params = [100, "Committee to Discuss Commit Messages in Git",
			"super-committee", 113, ["sen1", "sen2", "sen3"]]
		com = Committee(params)
		

	def testSenatorConstructor(self):
		#do stuff







if __name__ == '__main__':
    unittest.main()