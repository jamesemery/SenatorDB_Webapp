#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The basic frontend of our webapp; takes in cgi parameters, sanitizes them,
	and passes them off to the rest of the app.
 Joe Adkisson
 Jamie Emery
 Michael Stoneman
 """

import cgi
from UserInputParser import UserInputParser

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
	else:
		params['page_type'] = 'error'
	return params

def sanitizeInput(yarn):
	chars_to_remove = ";,\\/:'\"<>@"
	for ch in chars_to_remove:
		yarn = yarn.replace(ch, '');
	return yarn


if __name__ == '__main__':
	main()