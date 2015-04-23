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
 	makeHtmlPage(asdlfj)


 def printHtmlPage(senator, state, template_name):
 	#Load the template file
 	try:
 		f = open(template_name)
 		text = f.read()
 		f.close()
 	except Exception, e:
 		text = "Cannot read template file <tt>%s</tt>. " % (template_name)

 	replacements = {}

 	#Build results string, save in dictionary
 	results = ""
 	if senator:
 		results += "<p>Searching for Senator %s</p>\n" % (senator)
 	if state:
 		results += "<p>Finding senators from %s</p>\n" % (state)
 	#indentation stuff...................................................................................................
 	replacements["results"] = results

	outputText = text.format(**replacements)

	print 'Content-type: text/html\r\n\r\n'
	print outputText


 def getParameters():
 	params = {}
 	form = cgi.FieldStorage()
 	if 'senator' in form:
 		params['senator'] = sanitizeInput(form['animal'].value)
 	if 'state' in form:
 		params['state'] = sanitizeInput(form['animal'].value)
 	return params



 def sanitizeInput(yarn):
 	chars_to_remove = ";,\\/:'\"<>@"
 	for ch in chars_to_remove:
 		yarn = yarn.replace(ch, '');
 	return yarn


if __name__ == '__main__':
    main()