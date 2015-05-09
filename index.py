#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A simplistic webapp that enters in data from a form; we should have both a 
 drop-down menu, to (in our final app) select states, and a text input field,
 which we'll use to enter in names of senators and/or bills.

 Joe Adkisson
 Jamie Emery
 Michael Stoneman

 Adapted from Jadrian Miles' webapp.py, which in turn was adapted from Jeff
 Ondich's earlier versions.
 """

import cgi

def main():
	params = getParameters()
	backend = UserInputParser(params)
	htmlPage = backend.generateHtmlPageOutput()
	print htmlPage

def getParameters():
	params = {}
	form = cgi.FieldStorage()
	if 'senator' in form:
		params['senator'] = sanitizeInput(form['senator'].value)
	else:
		params['senator'] = ''
	if 'state' in form:
		params['state'] = sanitizeInput(form['state'].value)
	else:
		params['state'] = ''
	if 'page_type' in form:
		params['page_type'] = sanitizeInput(form['page_type'].value)
	return params

def sanitizeInput(yarn):
	chars_to_remove = ";,\\/:'\"<>@"
	for ch in chars_to_remove:
		yarn = yarn.replace(ch, '');
	return yarn


if __name__ == '__main__':
	main()