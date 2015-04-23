#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A web application that both displays a form and the result of submitting to
the form.  This program demonstrates a couple simple-minded techniques for
presenting the form and sanitizing user input.

The program does one of two things, depending on its CGI parameters.

1. If neither "animal" nor "badanimal" have been specified as CGI parameters,
   it displays the form for entering data, followed by links for viewing the
   source files.

2. If either of the above parameters have been specified, it displays the form
   PLUS a little response.

It's structured to separate out the front-end presentation (stored in
template.html) from the logical components of the application.

By Jadrian Miles, 2015; adapted from Jeff Ondich's sample, 2012.
"""

import cgi

def main():
    parameters = getCgiParameters()
    printMainPageAsHtml(parameters['animal'],
                        parameters['badanimal'],
                        'template.html')


def printMainPageAsHtml(animal, bad_animal, template_filename):
    """Prints to standard output the main page for this web application, based
    on the specified template file and parameters. The content of the page is
    preceded by a "Content-type: text/html" HTTP header, so that it get served
    up to the client as an HTML page to be rendered.
    """
    # Read the template as a giant string.  We're expecting that it has certain
    # formatting directives (things like {results} and {links}) in it, which
    # we'll replace using Python's name-based formatting engine.
    try:
        f = open(template_filename)
        template_text = f.read()
        f.close()
    except Exception, e:
        template_text = "Cannot read template file <tt>%s</tt>." % (
            template_filename)
    
    # This will be our dictionary of values to plug into the template file.
    # For each "{foo}" directive in the template, we'll need a key called "foo".
    replacements = {}
    
    # Build the animal report (the "results").
    animal_report = ""
    if animal or bad_animal:
        animal_report = "<p>I like %ss, too.</p>\n" % (animal)
        animal_report += "<p>Also, %ss are gross.</p>\n" % (bad_animal)
    animal_report = indent(animal_report, 1)
    replacements["results"] = animal_report
    
    # Build the links.
    source_links = ""
    link_template = '<p><a href="showsource.py?source=%s">%s source</a></p>\n'
    destinations = ["webapp.py", template_filename, "showsource.py"]
    for dest in destinations:
        source_links += link_template % (dest, dest)
    source_links = indent(source_links, 1)
    replacements["links"] = source_links
    
    # We can use that horrid short-circuit evaluation hack to provide default
    # values for the text in the input form fields.
    replacements["animal_hint"] = animal or "Enter an animal"
    replacements["badanimal_hint"] = bad_animal or "Enter an animal"
    
    # Now plug everything into the template...
    outputText = template_text.format(**replacements)
    
    # And finally print it to standard output, which is the CGI way of
    # communicating content back to the web server.
    print 'Content-type: text/html\r\n\r\n',
    print outputText


def getCgiParameters():
    """Returns a dictionary of sanitized, default-populated values for the CGI
    parameters that we care about.
    """
    form = cgi.FieldStorage()
    parameters = {'animal':'', 'badanimal':''}
    
    if 'animal' in form:
        parameters['animal'] = sanitizeUserInput(form['animal'].value)
    
    if 'badanimal' in form:
        parameters['badanimal'] = sanitizeUserInput(form['badanimal'].value)
    
    return parameters


def sanitizeUserInput(s):
    """Strips out scary characters from s and returns the sanitized version.
    """
    # We talked briefly in class about SQL injection.  One common "attack
    # vector" is through CGI parameters, either GET or POST.  If we use the
    # strings we get from the user to construct a database query, then we need
    # to be very careful that the user can't trick us into executing arbitrary
    # commands on our database.  There's actually a great XKCD comic about this,
    # along with a good explanation of the principle:
    #   http://www.explainxkcd.com/wiki/index.php/327:_Exploits_of_a_Mom
    # 
    # There are better ways to sanitize input than the following, but this is a
    # very simple example of the kind of thing you can do to protect your system
    # from malicious user input. Unfortunately, this example turns "O'Neill"
    # into "ONeill", among other things.
    # 
    # One thing to keep in mind about input sanitization is that it must happen
    # on the SERVER SIDE.  Clients who want to mess with your app can always
    # find ways to send it bogus data; you need to be prepared to receive ANY
    # junk they might come up with, and handle it safely.
    chars_to_remove = ";,\\/:'\"<>@"
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s


def indent(s, k):
    """Returns an indented copy of the string, with 4*k spaces prepended to
    each line.
    """
    return "\n".join([" "*(4*k) + line for line in s.splitlines()])


if __name__ == '__main__':
    main()

