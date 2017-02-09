#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, json

app_dir = '/opt/git/random-names'
os.chdir(app_dir)
sys.path.insert(0, app_dir)

from names import random_name

_ = open('app/main.html', 'r')
template = _.read()
_.close()

# The application interface is a callable object
def application ( environ, start_response):

    response_body = template % random_name.next()

    # HTTP response code and message
    status = '200 OK'

    # HTTP headers expected by the client
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    # Send them to the server using the supplied function
    start_response(status, response_headers)

    # Return the response body. Notice it is wrapped
    # in a list although it could be any iterable.

    return [response_body]

