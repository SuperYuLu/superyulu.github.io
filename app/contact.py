# contact.py --- 
# 
# Filename: contact.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Dec 16 17:39:46 2017 (-0600)
# Version: 
# Last-Updated: Sun Dec 24 21:47:24 2017 (-0600)
#           By: yulu
#     Update #: 8
# 

from app import app
from flask import render_template

@app.route('/contact/')
def contact():
    return render_template('contact.html')

