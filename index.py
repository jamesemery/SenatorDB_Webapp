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
	param_list = ['senator', 'bill', 'state', 'session', 'committee',
			'bill_index', 'error']
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