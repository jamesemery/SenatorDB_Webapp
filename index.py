#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The basic frontend of our webapp; takes in cgi parameters, sanitizes them,
	and passes them off to the rest of the app.
 Joe Adkisson
 Jamie Emery
 Michael Stoneman
 """

print 'Content-type: text/html\r\n\r\n'
print '<html><head></head><body>'

import cgi
from UserInputParser import UserInputParser
import cgitb
cgitb.enable()

def main():
	params = getParameters()
	print "Super 1 \n"
	backend = UserInputParser(params)
	print "Super 2 \n"
	htmlPage = backend.generateHtmlPageOutput()
	print "Super 3 \n"
	print htmlPage
	print '</body></html>'

def getParameters():
	params = {}
	form = cgi.FieldStorage()
	param_list = ['senator', 'bill', 'state', 'session', 'committee']
	for entry in param_list:
		if entry in form:
			params[entry] = sanitizeInput(form[entry].value)
		else:
			params[entry] = ''

	#Page_type gets special treatment b/c we want to default to the homepage/
	if 'page_type' in form:
		params['page_type'] = sanitizeInput(form['page_type'])
	else:
		params['page_type'] = 'home'

	#old code. just in case switching over to the for loop screwed things up
	#TODO delete this comment at some point.
	#if 'page_type' in form:
	#	params['page_type'] = sanitizeInput(form['page_type'].value)
	#else:
	#	params['page_type'] = 'error'
	return params

def sanitizeInput(yarn):
	chars_to_remove = ";,\\/:'\"<>@"
	for ch in chars_to_remove:
		yarn = yarn.replace(ch, '');
	return yarn


if __name__ == '__main__':
	main()