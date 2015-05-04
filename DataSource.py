#!/usr/bin/python
# -*- coding: utf-8 -*-



class DataSource:
    #Constructor for the DataSource database interface class.
    def __init__(self):
        #do stuff
       
    #Returns a list of the id numbers of all senators in the senate vote
    #database.
    def getSenatorList(self):
        #do stuff

    #Returns a list of the id numbers of all bills in the senate vote database.
    def getBillList(self):
        #do stuff

    #Returns a list of the id number for every senator in the specified congress
    #for example, 114 would return all current senators)
    def getSenatorsInCongress(self, congress):
        #do stuff

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