#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import sys
import psycopg2

class DataSource:
    #Constructor for the DataSource database interface class.
    global USERNAME = 'emeryj'
    global DB_NAME = 'emeryj'
    global db_connection
    

    def __init__(self):

        # Step 1: Read your password from the secure file.
        try:
            f = open(os.path.join('/cs257', USERNAME))
            PASSWORD = f.read().strip()
            f.close()

        except:
            sys.exit()

        # Step 2: Connect to the database.
        try:
            db_connection = psycopg2.connect(user=USERNAME,
                                             database=DB_NAME,
                                             password=PASSWORD)
        except:
            sys.exit()

        # Step 3: Create a "cursor".  When you execute a
        # query with a cursor, you can get the rows of the
        # output in a for-loop (like scrolling a cursor
        # through a text document)

    #Returns a bill object corresponding to id of the bill it is given
    def getBill(self, ident):
        try:
            cursor.execute('SELECT * FROM bills WHERE id =%s;'
                % ident)
            bills[]
            for row in cursor:
                bills.append(Bill(row))
            if len(bills)==1:
                return bills[0]
            else: return None 
        except:

    #Returns a senator object corresponding to id of the bill it is given
    def getSenator(self, ident):
        try:
            cursor.execute('SELECT * FROM senators WHERE id =%s;'
                % ident)
            senators[]
            for row in cursor:
                senators.append(Senator(row))
            if len(senators)==1:
                return senators[0]
            else: return None 
        except:

    #Returns a list of the id numbers of all senators in the senate vote
    #database.
    def getSenatorList(self):
        try:
            cursor.execute('SELECT * FROM senators;')
            senators = []
            for row in cursor:
                senators.append(Senator(row))
            return senators
        except:


    #Returns a list of the id numbers of all bills in the senate vote database.
    def getBillList(self):
        try:
            cursor.execute('SELECT * FROM bills;')
            bills = []
            for row in cursor:
                bills.append(Bill(row))
            return bills
        except:

    #Returns a list of the id number for every senator in the specified congress
    #for example, 114 would return all current senators)
    def getSenatorsInCongress(self, congress):
        try:
            cursor.execute('SELECT senators FROM sessions WHERE number=%s;' 
                % congress)
            senators = []
            for row in cursor:
                senators.append(getSenatorList(row[0]))
            return senators
        except:

    #Returns an ordered list of strings containing all of the biographical data
    #on the senator including, name, state, party affiliation, years in office,
    #and an arbitrary number of objects at the end which correspond to the
    #congresses that this senator is affiliated with.
    def getBiographyForSenator(self, senator_id):
        #do stuff

    #Returns a list of the last number Bill_id's that the senator has voted on
    #(with an Absent being ignored). If the number field is left as 0 it scans
    #the entire database for all the bills voted on by the senator.
    def getVotesBySenator(self, senator_id, number):
        #do stuff

    #Returns a list of the id numbers for the last number bills in congress in
    #reverse chronological. Specifying more bills than are in the congress
    #returns all availible bills, and specifying zero bills returns all bills.
    def getBillsInCongress(self, congress, number):
        #do stuff

    #Returns an ordered string list that contains the bill name, the bill HR
    #number, its congress, date voted on, and its description for being placed
    #into a bill class.
    def getBillBiography(self, bill_id):
        #do stuff

    #Returns a two dimensional list of strings that coresponds to the to a
    #Senator_ID and their vote on the specified bill (Tentatively: Yea, Nay,
    #Abstain, Absent).
    def getVotesForBill(self, bill_id):
        #do stuff


    #Returns a list that corresponds to the id number for each senator in a
    #given state with the name for each state given as a string.
    def getSenatorsInState(self, state_name):
        #do stuff