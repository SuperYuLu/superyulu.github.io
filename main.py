# main.py --- 
# 
# Filename: main.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Wed Dec 13 21:22:35 2017 (-0600)
# Version: 
# Last-Updated: Sun Dec 24 21:45:52 2017 (-0600)
#           By: yulu
#     Update #: 39
# 

import sys
from app import app
from flask_frozen import Freezer
#from flask import Flask, render_template
#from flask_flatpages import FlatPages, pygments_style_defs

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

#app = Flask(__name__)
#flatpages = FlatPages(app)

#app.config.from_object(__name__)
freezer = Freezer(app)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] =='build':
        freezer.freeze()
    else:
        app.run(host="127.0.0.1", port = 5000, debug = True)

