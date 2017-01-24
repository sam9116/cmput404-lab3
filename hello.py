#!/usr/bin/env python
import os
from pprint import pprint
import json
import urlparse
from templates import *

import sys

print "Content-Type: text/html;"

#print "hello,world!"

#params = urlparse.parse_qs(os.environ['QUERY_STRING'])
#agent = os.environ['HTTP_USER_AGENT']
#print params
#print agent

username = 'sam'
password = 'cmput404'

length = os.environ['CONTENT_LENGTH']
cookie = os.environ['HTTP_COOKIE']
logged_in = False




content = ''

if 'logged-in=True' cookie:
    logged_in = True


elif length:
    bytes_to_read = int(length)

    content = sys.stdin.read(bytes_to_read)
    params= urlparse.parse_qs(content)


    if (params['username'][0] == username and params['password'][0] ==password):
        print "Set-Cookie: logged-in=true;"
        logged_in=True


print

if logged_in != True:
    print login_page()
elif logged_in != False:
    print secret_page(params['username'][0], params['password'][0]) 
    
