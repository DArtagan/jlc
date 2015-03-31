#!/usr/bin/env python
"""Pelican configuration file."""
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'William Weiskopf'
SITENAME = 'JLC Counseling, LLC'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Theme
THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DIRECT_TEMPLATES = ['index']
