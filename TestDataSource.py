#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cgitb
import datetime
from DataSource import DataSource
from Bill import Bill
from Senator import Senator
from Committee import Committee


#Unit tests for DataSource.py. assumes certian values about the database that are specified at the top
class TestDataSource(unittest.TestCase):
    
    global db_source
    db_source = DataSource()
    #for testing purpouses I will rely on several specific datapoints hardcoded
    #into the test code, here are the databse entries for the particular objects
    #I will be testing so it is clear to see what I am emulating in code

    #Bill example = (100, 109, 188, datetime.date(2005, 7, 14), 'amendment', 'On
    #the Amendment S.Amdt. 1222 to H.R. 2360 (Department of Homeland Security
    #Appropriations Act, 2006)', [300001, 300005, 300006, 300008, 300009,
    #300011, 300016, 300018, 300019, 300022, 300026, 300028, 300032, 300034,
    #300037, 300038, 300042, 300043, 300051, 300056, 300057, 300058, 300059,
    #300060, 300061, 300063, 300064, 300065, 300066, 300067, 300068, 300076,
    #300078, 300077, 400629, 300080, 300081, 300082, 300084, 400619, 300086,
    #300087, 300093, 300100], [300002, 300003, 300004, 300007, 300010, 300013,
    #300014, 300015, 400054, 300020, 300021, 400576, 300023, 300024, 300025,
    #300027, 300029, 300030, 300033, 300035, 300036, 300040, 300041, 300045,
    #300047, 300048, 300049, 300050, 300052, 300054, 300055, 400194, 300062,
    #300070, 400621, 300071, 300072, 300075, 300083, 300085, 300088, 300089,
    #300090, 300091, 300092, 300094, 300095, 300096, 300097, 400546, 400418,
    #300098, 300099], [], [400105, 300069, 300073])

    #senator example = (407661, 'Metcalfe', 'Thomas', datetime.date(1780, 3, 20), 'M', 'KY', 'Whig', 'Thomas Metcalfe (Kentucky)', False)

    global test_senator
    test_senator = Senator([412390, 'Coons', 'Chris', datetime.date(2063, 9, 9), 'M', 'DE', 'Democrat', 'Chris Coons', True])


    short_bill_list = [100, 109, 188, datetime.date(2005, 7, 14), 'amendment', 'On the Amendment S.Amdt. 1222 to H.R. 2360 (Department of Homeland Security Appropriations Act, 2006)']
    global test_billnv
    test_billnv = Bill(short_bill_list)

    #note, this is not entirely accurate as what db_source really passes to the
    #constructor are lists of senator objects but in this case it is still
    #possible to test by comparing the id integer to senator.getId()
    
    global test_billwv
    test_billwv = Bill([100, 109, 188, datetime.date(2005, 7, 14), 'amendment', 'On the Amendment S.Amdt. 1222 to H.R. 2360 (Department of Homeland Security Appropriations Act, 2006)', [300001, 300005, 300006, 300008, 300009, 300011, 300016, 300018, 300019, 300022, 300026, 300028, 300032, 300034, 300037, 300038, 300042, 300043, 300051, 300056, 300057, 300058, 300059, 300060, 300061, 300063, 300064, 300065, 300066, 300067, 300068, 300076, 300078, 300077, 400629, 300080, 300081, 300082, 300084, 400619, 300086, 300087, 300093, 300100], [300002, 300003, 300004, 300007, 300010, 300013, 300014, 300015, 400054, 300020, 300021, 400576, 300023, 300024, 300025, 300027, 300029, 300030, 300033, 300035, 300036, 300040, 300041, 300045, 300047, 300048, 300049, 300050, 300052, 300054, 300055, 400194, 300062, 300070, 400621, 300071, 300072, 300075, 300083, 300085, 300088, 300089, 300090, 300091, 300092, 300094, 300095, 300096, 300097, 400546, 400418, 300098, 300099], [], [400105, 300069, 300073]])


    ## testing that GetBill does indeed return the expectd bill object
    def testGetBill(self):
        actual = db_source.getBill(100)
        self.assertEquals(test_billnv.getId(), actual.getId())
        self.assertEquals(test_billnv.getSession(), actual.getSession())
        self.assertEquals(test_billnv.getRoll(), actual.getRoll())
        self.assertEquals(test_billnv.getVoteDate(), actual.getVoteDate())
        self.assertEquals(test_billnv.getType(), actual.getType())
        self.assertEquals(test_billnv.getQuestion(), actual.getQuestion())

    # testing that GetBillWithVotes works properly, makes the assumption that a senator object that gets built and passed works properly and that a matching id is all that's necessary
    def testGetBillWithVotes(self):
    	actual = db_source.getBill(100)
        self.assertEquals(test_billwv.getId(), actual.getId())
        self.assertEquals(test_billwv.getSession(), actual.getSession())
        self.assertEquals(test_billwv.getRoll(), actual.getRoll())
        self.assertEquals(test_billwv.getVoteDate(), actual.getVoteDate())
        self.assertEquals(test_billwv.getType(), actual.getType())
        self.assertEquals(test_billwv.getQuestion(), actual.getQuestion())
        yea = []
        nay = []
        present = []
        not_voting = []
        print actual.getYeaVotes()
        for senator in actual.getYea_Votes():
        	yea.append(senator.getId())
        for senator in actual.getNay_Votes():
        	nay.append(senator.getId())
        for senator in actual.getAbstaining():
        	present.append(senator.getId())
        for senator in actual.getAbsent():
        	not_voting.append(senator.getId())
        self.assertEqual(tuple(test_billwv.getYea_Votes()),tuple(yea))
        self.assertEqual(tuple(test_billwv.getNay_Votes()),tuple(nay))
        self.assertEqual(tuple(test_billwv.getAbstaining()),tuple(present))
        self.assertEqual(tuple(test_billwv.getAbsent()),tuple(not_voting))



    def testGetSenator(self):
    	actual = db_source.getSenator(412390)
    	self.assertEquals(test_senator.getId(), actual.getId())
    	self.assertEquals(test_senator.getFirst(), actual.getFirst())
    	self.assertEquals(test_senator.getLast(), actual.getLast())
    	self.assertEquals(test_senator.getBirthday(), actual.getBirthday())
    	self.assertEquals(test_senator.getGender(), actual.getGender())
    	self.assertEquals(test_senator.getParty(), actual.getParty())
    	self.assertEquals(test_senator.getWiki(), actual.getWiki())
    	self.assertEquals(test_senator.isCurrent(), actual.isCurrent())


    def testGetSenatorWithCommittees(self):
    	self.assertEquals(false)
    	#TODO adsf asd fa 




if __name__ == '__main__':
    unittest.main()
