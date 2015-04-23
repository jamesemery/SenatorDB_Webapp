#!/usr/bin/python
# -*- coding: utf-8 -*-



class DataSource:
    def __init__(self):
        """Constructor for the DataSource database interface class.
        """
       
 

    def getSenatorList(self):
        """Returns a list of the id numbers of all senators in the
        senate vote database."""
        # Implementation will eventually go here. In the
        # meantime, just return an object of the right type.
        return []


    def getBillList(self):
        """Returns a list of the id numbers of all bills in the senate vote database"""
        return []


    def getSenatorsInCongress(self, congress):
        """Returns a list of the id number for every senator in the specified congress (for example 114 would return all current senators)"""
        return []


    def getBiographyForSenator(self, senator_id):
        """Returns an ordered list of strings containing all of the biographical data on the senator including, name, state, party affiliation, years in office, and an arbitrary number of objects at the end which correspond to the congresses that this senator is affiliated with"""
        return []


    def getVotesBySenator(self, senator_id, number):
        """Returns a list of the last number Bill_id's that the senator has voted on (with an Absent being ignored). If the number field is left as 0 it scans the entire database for all the bills voted on by the senator"""
        return []


    def getBillsInCongress(self, congress, number):
        """Returns a list of the id numbers for the last number bills in congress in reverse chronological. Specifying more bills than are in the congress returns all availible bills and specifying zero bills returns all bills"""
        return[]


    def getBillBiography(self, bill_id):
        """Returns an ordered string list that contains the bill name, the bill HR number, its congress, date voted on, and its description for being placed into a bill class"""
        return[]


    def getVotesForBill(self, bill_id):
        """Returns a two dimensional list of strings that coresponds to the to a Senator_ID and their vote on the specified bill (Tentativly: Yea, Nay, Abstain, Absent)"""
        return[]



    def getSenatorsInState(self, state_name):
        """Returns a list that corresponds to the id number for each senator in a given state with the name for each state given as a string."""
        return[]

