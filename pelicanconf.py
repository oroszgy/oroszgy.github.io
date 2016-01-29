#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'György Orosz'
SITENAME = 'random.sample(Gyuri())'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

STATIC_PATHS = ['images', 'pdfs']

DEFAULT_LANG = 'en'
THEME = "/Users/gyorgyorosz/Documents/crowsfoot"
PROFILE_IMAGE_URL = "images/wordcloud.png"
SHOW_ARTICLE_AUTHOR = False
EMAIL_ADDRESS = "oroszgy@itk.ppke.hu"
#MENUITEMS = [("Teaching (hu)", "teaching.html"), ("About", "about.html")]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
