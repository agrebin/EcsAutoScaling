#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./server.py [<port>]

Send a GET request::
    curl http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
#import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        msg = json.dumps(['protoserver', {'contents': ('version', 1.0)}])
        self.wfile.write(msg)

    def do_HEAD(self):
        self._set_headers()
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
