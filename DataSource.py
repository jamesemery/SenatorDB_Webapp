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
        try:
            f = open(os.path.join('/cs257', USERNAME))
            PASSWORD = f.read().strip()
            f.close()
        except:
            sys.exit()
        try:
            db_connection = psycopg2.connect(user=USERNAME,
                                             database=DB_NAME,
                                             password=PASSWORD)
        except:
            sys.exit()

    #Returns a bill object corresponding to id of the bill it is given
    def getBill(self, ident):
        try:
            cursor = db_connection.cursor()
            cursor.execute('SELECT * FROM bills WHERE id = (%s);',
                (ident, ))
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
            cursor = db_connection.cursor()
            cursor.execute('SELECT * FROM senators WHERE id = (%s);'
                (ident,))
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
            cursor = db_connection.cursor()
            cursor.execute('SELECT * FROM senators;')
            senators = []
            for row in cursor:
                senators.append(Senator(row))
            return senators
        except:


    #Returns a list of the id numbers of all bills in the senate vote database.
    def getBillList(self):
        try:
            cursor = db_connection.cursor()
            cursor.execute('SELECT * FROM bills;')
            bills = []
            for row in cursor:
                bills.append(Bill(row))
            return bills
        except:

    #Returns a list of the id number for every senator in the specified congress
    #(for example, 114 would return all current senators)
    def getSenatorsInCongress(self, congress):
        try:
            cursor = db_connection.cursor()
            cursor.execute('''SELECT senators FROM sessions 
                WHERE number = (%s);''',  (congress, ))
            senators = []
            for row in cursor:
                senators.append(getSenator(row[0]))
            return senators
        except:

    #Returns a tuple list of containing the last number (or all votes in the
    #database number =0) chronological votes that the senator has participated
    #in. The first value in the tuple is an int corresponding the the ID number
    #of the bill in question and the second value is a string representing the
    #senators vote
    def getVotesBySenator(self, senator_id, number):
        try:
            cursor = db_connection.cursor()
            cursor.execute('''SELECT number,senators 
                FROM sessions 
                ORDER BY number DESC;''')
            
            #determines what congress the senator belongs and stores the ID of
            #the congress in a list
            member_congresses = []
            for row in cursor:
                list_senators = row[1]
                if senator_id in list_senators:
                    member_congresses.append(row[0])
            
            if len(member_congresses) == 0: return None

            #loops through the bills in the congress, then loops through the 
            #votes in the congress looking for places where the particular 
            #senator appears on the voting roll 
            bills_voted = []
            for session in member_congresses:
                cursor.execute('''SELECT id, yea_votes, nay_votes, present, not_voting FROM bills 
                    WHERE session = (%s) 
                    ORDER BY date DESC;''', 
                    (session, ))
                for row in cursor:
                    if senator_id in row[1]: 
                        bills_voted.append([row[0],"yea"])
                    elif senator_id in row[2]: 
                        bills_voted.append([row[0],"nay"])
                    elif senator_id in row[3]: 
                        bills_voted.append([row[0],"present"])
                    elif senator_id in row[4]: 
                        bills_voted.append([row[0],"not_voting"])
                    
                    if (number != 0)&(len(bills_voted) >= number):
                        break
            return bills_voted


    #Returns a tuple of committees (historical and current) that the senator
    #has been a member of where the first value corresponds to the class of
    #the committee and the second value is a string that corresponds to what
    #type of member the senator is
    def getCommitteesBySenator(self,senator_id):
        try:
            cursor = db_connection.cursor()
            cursor.execute('''SELECT number,senators 
                FROM sessions 
                ORDER BY number DESC;''')
            
            #Narrowing the search by locating what congresses to search first
            member_congresses = []
            for row in cursor:
                list_senators = row[1]
                if senator_id in list_senators:
                    member_congresses.append(row[0])
#####ASK ABOUT STRUCTURE########
            

    #Returns a list of the id numbers for the last number bills in congress in
    #reverse chronological. Specifying more bills than are in the congress
    #returns all availible bills, and specifying zero bills returns all bills.
    def getBillsInCongress(self, congress, number):
        try:
            cursor = db_connection.cursor()
            cursor.execute('SELECT bills FROM sessions WHERE number = (%s);' 
                (congress,))
            bills = []
            for row in cursor:
                bills.append(getBill(row[0]))
                if (number != 0)&(len(bills) >= number): break
            return bills
        except:

    #Returns a two dimensional list of strings that coresponds to the to a
    #Senator_ID and their vote on the specified bill (Tentatively: Yea, Nay,
    #Abstain, Absent).
    def getVotesForBill(self, bill_id):


    #Returns a list that corresponds to the id number for each senator in a
    #given state with the name for each state given as a string.
    def getSenatorsInState(self, state_name):
        try:
            cursor = db_connection.cursor()
            cursor.execute('SELECT * FROM senators WHERE state = (%s);' 
                (state_name,))
            senators = []
            for row in cursor:
                senators.append(Senator(row))
            return senators
        except:

    #Returns a Committee object corresponding to the ID number it gets with a
    #populated list of senator objects corresponding to its members
    def getCommittee(self, committee_id):
        try:
            cursor = db_connection.cursor()
            cursor.execute('SELECT * FROM committees WHERE id = (%s);' 
                (committee_id,))
            committee = []
            for row in cursor:
                members = []
                for member in row[4]:
                    senator = getSenator(int(member[0]))
                    members.append([senator,member[1]])
                args = [row[0], row[1], row[2], row[3], members]
                committees.append(Committee())
            if len(committees) == 1: return committees[0]
            else: return None
        except:

#####JOE: make Committee class  ########

    #Returns a list of committee objects correspoinding to the committees in a
    #given year
    def getCommitteeBySession(self, congress):
        try:
            cursor = db_connection.cursor()
            cursor.execute('SELECT * FROM committees WHERE number = (%s);' 
                (congress,))
            committees = []
            for row in cursor:
                committees.append(Committee(row))
            return committees
        except:

