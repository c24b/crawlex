#!/usr/bin/env python
# -*- coding: utf-8 -*-


from config import CMD
from packages.docopt import docopt
from worker import *
import os, sys

ABSPATH = os.path.dirname(os.path.abspath(sys.argv[0]))

if __name__== "__main__":
	try:		
		w = Worker(docopt(CMD))		
	except KeyboardInterrupt:
		sys.exit()
