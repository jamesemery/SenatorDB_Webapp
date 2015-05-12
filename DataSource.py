#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgitb
cgitb.enable()
import os.path
import sys
import psycopg2
import cgitb
import datetime
from Bill import Bill
from Senator import Senator
from Committee import Committee


class DataSource:
    #Constructor for the DataSource database interface class.


    def __init__(self):
        USERNAME = 'emeryj'
        DB_NAME = 'emeryj'
        try:
            #f = open('testpassfileworkaround')
            f = open(os.path.join('/cs257', USERNAME)) ###TODO DELETE THIS
            PASSWORD = f.read().strip()
            f.close()
        except:
            print "failed to connect to the database directory"
        global db_connection
        try:
            db_connection = psycopg2.connect(user=USERNAME,
                                             database=DB_NAME,
                                             password=PASSWORD)
        except:
            print "psycopg2 failed to load the directory"

    #Returns a bill object corresponding to id of the bill it is given withouth
    #any vote information
    def getBill(self, bill_id):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT id, session, roll, vote_date, type, question FROM bills WHERE id = (%s);',
            (bill_id, ))
        bills = []
        for row in cursor:
            bills.append(Bill(row))
        if len(bills)==1:
            return bills[0]
        else: return None 
        #except:
        #    print "failed to retieve item from the database"
        #    return None



    #Returns a bill object corresponding to id of the bill it is given as well
    #as returning lists of senator objects corresponding to the voters on said
    #bill
    def getBillWithVotes(self, bill_id):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM bills WHERE id = (%s);',
            (bill_id, ))
        bills = []
        for row in cursor:
            yea = []
            nay = []
            present = []
            not_voting = []
            for senator in row[6]:
                yea.append(self.getSenator(senator))
            for senator in row[7]:
                nay.append(self.getSenator(senator))
            for senator in row[8]:
                present.append(self.getSenator(senator))
            for senator in row[9]:
                not_voting.append(self.getSenator(senator))

            bil = list(row)[:6] + list([yea, nay, present, not_voting])
            bills.append(Bill(bil))
        if len(bills)==1:
            return bills[0]
        else: return None 
        #except:
        #    print "failed to retieve item from the database"
        #    return None


    #Returns a Senator object corresponding to id of the bill it is given
    def getSenator(self, senator_id):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM senators WHERE id = (%s);',
            (senator_id,))
        senators = []
        for row in cursor:
            senators.append(Senator(row))
        if len(senators)==1:
            return senators[0]
        else: 
            print senator_id
            return None 
        #except:
        #    print "failed to retieve item from the database"
        #   return None

    #Returns a Senator object corresponding to the Senator id it was passed
    #except with a list of committee objects correspoinding to the committees
    #that the senator has been part of
    def getSenatorWithCommittees(self, senator_id):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM senators WHERE id = (%s);',
            (senator_id,))
        rows = []
        for row in cursor:
            rows.append(row)
        
        #if only one senator was found, it searches the committee_membership_pair table to find all the committees the senator is a part of and builds a committee object
        if len(rows)==1:
            cursor.execute('''SELECT * FROM committee_membership_pair 
                WHERE senator = (%s);''',
                (senator_id,))
            committees = []
            for pair in cursor:
                committees.append([self.getCommittee(pair[0]), pair[2]])
            subrow = rows[0]
            sen_row = [subrow[0], subrow[1], subrow[2], subrow[3], subrow[4],
                  subrow[5], subrow[6], subrow[7], subrow[8], committees]
            return Senator(sen_row)
        else: return None 
        #except:
        #    print "failed to retieve item from the database"
        #    return None

    #Returns a list of the id numbers of all senators in the senate vote
    #database.
    def getSenatorList(self):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM senators;')
        senators = []
        for row in cursor:
            senators.append(Senator(row))
        return senators
        #except:
        #    print "failed to retieve item from the database"
        #    return None  


    #Returns a list of the id numbers of all bills in the senate vote database.
    def getBillList(self):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM bills;')
        bills = []
        for row in cursor:
            bills.append(Bill(row))
        return bills
        #except:
        #    print "failed to retieve item from the database"
        #    return None


    #Returns a list of senators corresponding to the members of the specified congress
    def getSenatorsInSession(self, session):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('''SELECT senators FROM sessions 
            WHERE number = (%s);''',  (session, ))
        senators = []
        for row in cursor:
            senators.append(self.getSenator(row[0]))
        return senators
        #except:
        #    print "failed to retieve item from the database"
        #    return None

    #Returns a double list of containing the last number (or all votes in the
    #database number =0) chronological votes that the senator has participated
    #in. The first value in the tuple is an int corresponding the the ID number
    #of the bill in question and the second value is a string representing the
    #senators vote
    def getVotesBySenator(self, senator_id, number):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('''SELECT number,senators 
            FROM sessions 
            ORDER BY number DESC;''')
        
        #determines what congress the senator belongs and stores the ID of
        #the congress in a list
        member_congresses = []
        for row in cursor:
            list_senators = row[1]
            for ident in list_senators:
                if ident == int(senator_id):
                    member_congresses.append(row[0])
        if len(member_congresses) == 0: 
            return []
##TODO FIGURE OUT ISSUE HERER
        #loops through the bills in the congress, then loops through the 
        #votes in the congress looking for places where the particular 
        #senator appears on the voting roll 
        bills_voted = []
        for session in member_congresses:
            cursor.execute('''SELECT id, yea_votes, nay_votes, present, not_voting FROM bills  
                where session = (%s)
                ORDER BY vote_date DESC;''',
                (session,))
            for row in cursor:
                for ident in row[1]:
                    if ident == int(senator_id):
                        bills_voted.append([self.getBill(row[0]),"yea"])
                for ident in row[2]:
                    if ident == int(senator_id):
                        bills_voted.append([self.getBill(row[0]),"nay"])
                for ident in row[3]:
                    if ident == int(senator_id):
                        bills_voted.append([self.getBill(row[0]),"present"])
                for ident in row[4]:
                    if ident == int(senator_id):
                        bills_voted.append([self.getBill(row[0]),"not_voting"])
                #if (number != 0)&(len(bills_voted) <= number):
                #    break
        return bills_voted
        #except: 
        #    print "failed to retieve item from the database"
        #    return None
            

    #Returns a list of the id numbers for the last number bills in congress in
    #reverse chronological. Specifying more bills than are in the congress
    #returns all availible bills, and specifying zero bills returns all bills.
    def getBillsInCongress(self, congress, number):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT bills FROM sessions WHERE number = (%s);', 
            (congress,))
        bills = []
        for row in cursor:
            for bill_id in row[0]:
                bills.append(self.getBill(bill_id))
            if (number != 0)&(len(bills) >= number): break
        return bills
        #except:
        #    print "failed to retieve item from the database"
        #    return None



    #Returns a list that corresponds to the id number for each senator in a
    #given state with the name for each state given as a string.
    def getSenatorsInState(self, state_name):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM senators WHERE state = (%s);', 
            (state_name,))
        senators = []
        for row in cursor:
            senators.append(Senator(row))
        return senators
        #except:
        #    print "failed to retieve item from the database"
        #    return None

    
    #Returns a Committee object corresponding to the ID number it gets with a
    #populated list of senator objects corresponding to its members
    def getCommittee(self, committee_id):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('''SELECT id, name, super_committee, session 
            FROM committees WHERE id = (%s);''', 
            (committee_id,))
        committees = []
        for row in cursor:
            committees.append(Committee(row))
        if len(committees) == 1: return committees[0]
        else: return None
        #except:
        #    print "failed to retieve item from the database"
        #    return None


    #Returns a Committee object corresponding to the ID number it gets with a
    #populated list of senator objects corresponding to its members
    def getCommitteeWithMembers(self, committee_id):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM committees WHERE id = (%s);', 
            (committee_id,))
        committees = []
        for row in cursor:
            #grabbing the senators in the nested array stored in the
            #database and gets a senator object out of them
            members = []
            for member in row[4]:
                senator = self.getSenator(int(member[0]))
                members.append([senator,member[1]])
            args = [row[0], row[1], row[2], row[3], members]
            committees.append(Committee(args))
        if len(committees) == 1: return committees[0]
        else: return None
        #except:
        #    print "failed to retieve item from the database"
        #    return None


    #Returns a list of committee objects correspoinding to the committees in a
    #given year
    def getCommitteeBySession(self, congress):
        #try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM committees WHERE session = (%s);', 
            (congress,))
        committees = []
        for row in cursor:
            committees.append(Committee(row))
        return committees
        #except:
        #    print "failed to retieve item from the database"
        #    return None

