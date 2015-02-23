#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'K. Arthur Endsley'
SITENAME = 'K. Arthur Endsley'
SITEURL = ''
#SITEURL = 'http://karthur.org'
THEME = 'themes/karthur'

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Michigan Tech Research Institute (MTRI)', 'http://www.mtri.org/'),
        ('UMich School of Natural Resources and Environment', 'http://snre.umich.edu/'),)

PORTFOLIO = (('Bering Glacier Monitoring', 'http://www.beringglacier.org/gass/'),
        ('Great Lakes Remote Sensing', 'http://greatlakesremotesensing.org/'))

# Social widget
SOCIAL = (('GitHub', 'http://github.com/arthur-e/'),
        ('LinkedIn', 'www.linkedin.com/in/endsley'),
        ('BitBucket', 'http://bitbucket.org/kaendsle'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme info
BOOTSTRAP_THEME = 'sandstone'
CC_LICENSE = 'CC-BY-NC-SA'
CUSTOM_CSS = 'theme/css/custom.css'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_INLINE = True
PYGMENTS_STYLE = 'solarizeddark'
