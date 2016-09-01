#!/usr/bin/env python3

# Copyright (c) 2016, the jobbot authors.
# Please see the AUTHORS file for details.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys, os
import socket
import requests

try:
	url = os.environ['JOBBOT_WEBHOOK_URL']
except Exception as e:
	print("Webhook URL not found. Please set 'JOBBOT_WEBHOOK_URL' environment variable.")
	sys.exit(-1)

user = None
if "USER" in os.environ:
	user = os.environ['USER']

machine = socket.gethostname()

msg = "Done."
if len(sys.argv) > 1:
	msg = sys.argv[1]

r = requests.post(url, json = {'text': 'Job for user `{}` on machine `{}`: _{}_'.format(user, machine, msg), 'channel': '#servers'})

if r.status_code != 200:
	print('Server communication error: ' + r.status_code)
	sys.exit(-1)
