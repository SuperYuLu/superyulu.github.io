# flaskPreRenderer.py --- 
# 
# Filename: flaskPreRenderer.py
# Description: 
#            A pre-renderer to use flask to render markdown
#            content before flatpages take over.
#            with out this renderer flatpage won't understand
#            flask template command {{... }}
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Mon Dec 25 13:49:32 2017 (-0600)
# Version: 
# Last-Updated: Mon Dec 25 13:54:03 2017 (-0600)
#           By: yulu
#     Update #: 3
# 

from flask import render_template_string
from flask_flatpages import pygmented_markdown

def flaskPreRenderer(mdContent):
    """
    let flask to prerender before hand it to flatpages
    so that flask template command in markdown can be 
    rendered properly
    """
    prerendered_body = render_template_string(mdContent)
    return pygmented_markdown(prerendered_body)
