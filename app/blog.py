# blog.py --- 
# 
# Filename: blog.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Wed Dec 20 22:31:26 2017 (-0600)
# Version: 
# Last-Updated: Sat Jan 20 13:53:47 2018 (-0600)
#           By: yulu
#     Update #: 82
# 

from app import app
from flask import render_template
from flask_flatpages import FlatPages

flatpages = FlatPages(app)

def countCategory():
    categoryName = [p['category'] for p in flatpages]
    category = {c: categoryName.count(c) for c in set(categoryName)}
    return category

@app.route('/blog/')
def posts():
    posts = [p for p in flatpages] 
    posts.sort(key = lambda item: item['date'], reverse = False)
    categoryStats = countCategory()
    return render_template('blog.html', posts = posts, categoryStats = categoryStats)


@app.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(name, name)
    post = flatpages.get_or_404(path)

    posts = [p for p in flatpages] 
    posts.sort(key = lambda item: item['date'], reverse = False)
    categoryStats = countCategory()
    
    return render_template('post.html', post = post, posts = posts, categoryStats = categoryStats)


