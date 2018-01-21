# __init__.py --- 
# 
# Filename: __init__.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Wed Dec 13 21:18:45 2017 (-0600)
# Version: 
# Last-Updated: Sun Jan 21 13:10:08 2018 (-0600)
#           By: yulu
#     Update #: 74
# 


from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('flasksettings.cfg')

##
# use my own defined makedown prerenderer if there is flask
# syntax in markdown file
##

#from app.flaskPreRenderer import flaskPreRenderer
#app.config['FLATPAGES_HTML_RENDERER'] = flaskPreRenderer

from app import home, contact, blog



