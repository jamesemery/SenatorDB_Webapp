#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The basic frontend of our webapp; takes in cgi parameters, sanitizes them,
	and passes them off to the rest of the app.
 Joe Adkisson
 Jamie Emery
 Michael Stoneman
 """

#import cgitb
#cgitb.enable()

import cgi
from UserInputParser import UserInputParser

def main():
	params = getParameters()
	backend = UserInputParser(params)
	htmlPage = backend.generateHtmlPageOutput()
	print 'Content-type: text/html\r\n\r\n'
	print htmlPage


def getParameters():
	params = {}
	form = cgi.FieldStorage()
	param_list = ['senator', 'bill', 'state', 'session', 'committee']
	for entry in param_list:
		if entry in form:
			params[entry] = sanitizeInput(form[entry].value)
		else:
			params[entry] = ''

	# page_type gets special treatment so that it defaults to the homepage
	if 'page_type' in form:
		params['page_type'] = sanitizeInput(form['page_type'].value)
	else:
		params['page_type'] = 'home'

	return params

def sanitizeInput(yarn):
	chars_to_remove = ";,\\/:'\"<>@"
	for ch in chars_to_remove:
		yarn = yarn.replace(ch, '');
	return yarn


if __name__ == '__main__':
	main()