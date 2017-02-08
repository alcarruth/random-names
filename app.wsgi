#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, json

app_dir = '/opt/git/random-names'
os.chdir(app_dir)
sys.path.insert(0, app_dir)

from names import random_name

template = """
<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title> Random Name Generator </title>
<link rel="stylesheet" href="/style.css">
</head>

<body>
<div id="main">
<h2> Random Name Generator </h2>
<h3 id="random-name"> %s </h3>
<a href="/random-names"> random.name.next() </a>
<h3> Sources </h3>

<p>
 The generator code is a really simple python program that randomly
selects
<ul>
<li>  a first name from a list containing 1000 female and 1000 male
first names, </li>
<li> and a surname from a list containing 1000 surnames.</li>
</ul>

These lists were obtained from 
<a href="http://names.mongabay.com/data/1000.html" target="_blank">
http://names.mongabay.com/data/1000.html </a> </p>

</div>
</body>

</html>
"""

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

