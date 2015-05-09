#!/usr/bin/python

# cgitb is for DEBUG PURPOSES ONLY!  Comment out these lines once your app is
# "in production".
# We print out the ContentType HTTP header first because cgitb produces its
# error output in HTML.
print 'Content-type: text/html\r\n\r\n'
print '<html><head></head><body>'
import cgitb
cgitb.enable()
# Note that cgitb works by catching uncaught exceptions.  In the code below I
# use a bunch of try/except blocks, which is correct practice that you should
# follow in the code that you write for this project.
#   HOWEVER!  If I work really hard at catching my own exceptions during
# development, I lose out on the chance for cgitb to tell me details about
# them.  So consider leaving out the exception handling when you're first
# developing your stuff.  (You could leave "# TODO" comments for yourself to
# make sure you go back and fill them in.)

import os.path
import sys
import psycopg2

# CHANGE THESE LINES!                                      <~~~~~~~~~~~~~~~ Hey!
USERNAME = 'emeryj'
DB_NAME = 'emeryj'

print 'Hello!<br>'

# Step 1: Read your password from the secure file.
print 'Reading your password...'
try:
    f = open(os.path.join('/cs257', USERNAME))
    PASSWORD = f.read().strip()
    f.close()
    print 'Success!<br>'
    # UNCOMMENT THIS LINE TO SEE YOUR PASSWORD!            <~~~~~~~~~~~~~~~ Hey!
    #print 'Your database password is %s.<br>' % PASSWORD
except:
    print 'Failed. =(<br>'
    sys.exit()

# Step 2: Connect to the database.
print 'Connecting to database %s...' % DB_NAME
try:
    db_connection = psycopg2.connect(user=USERNAME,
                                     database=DB_NAME,
                                     password=PASSWORD)
    print 'Success!<br>'
except:
    print 'Failed. =(<br>'
    sys.exit()

# Step 3: Create a "cursor".  When you execute a
# query with a cursor, you can get the rows of the
# output in a for-loop (like scrolling a cursor
# through a text document).
print 'Creating a database cursor...'
try:
    cursor = db_connection.cursor()
    print 'Success!<br>'
except:
    print 'Failed. =(<br>'
    sys.exit()

# Step 4: Read the rows of the output and act
# on them.
try:
    cursor.execute('SELECT * FROM senators;')
    print '<pre>'
    for row in cursor:
        print str(type(row))
        print row
    print '</pre>'
except:
    print 'Problem with select query. =(<br>'

print '</body></html>'










