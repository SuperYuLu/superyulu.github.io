# home.py --- 
# 
# Filename: home.py
# Description: 
#            render homepage
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Wed Dec 13 21:20:28 2017 (-0600)
# Version: 
# Last-Updated: Sun Jan 21 21:28:02 2018 (-0600)
#           By: yulu
#     Update #: 25
# 


from app import app
from flask import render_template
from app.blog import flatpages


#@app.route('/home/')
@app.route('/')
def home():
    posts = [p for p in flatpages] 
    posts.sort(key = lambda item: item['date'], reverse = False)
    recentPostsInfo = [[post['title'],post['category'], post['date']] for i, post in enumerate(posts) if i < 10]
    return render_template('home.html', recentPostsInfo=recentPostsInfo)
