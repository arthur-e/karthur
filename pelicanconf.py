#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'K. Arthur Endsley'
SITENAME = 'K. Arthur Endsley'
SITEURL = ''
#SITEURL = 'http://karthur.org'
THEME = 'themes/karthur'

PLUGIN_PATHS = ['/usr/local/pelican/pelican-plugins']
PLUGINS = ['thumbnailer']

DISPLAY_PAGES_ON_MENU = True
MY_UNICODE_EMAIL_ADDR = '&#101;&#110;&#100;&#115;&#108;&#101;&#121;&#64;&#117;&#109;&#105;&#99;&#104;&#46;&#101;&#100;&#117;'

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
STATIC_PATHS = ['images', 'static']
PAGE_PATHS = ['pages']

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
LINKS = (('Michigan Tech Research Institute', 'http://www.mtri.org/'),
        ('UMich School of Natural Resources and Environment', 'http://snre.umich.edu/'),
        ('North Slope Science Initiative', 'http://northslope.org/'),)

PORTFOLIO = (('Carbon Flux Visualization', 'http://spatial.mtri.org/flux/'),
        ('Bering Glacier Monitoring', 'http://www.beringglacier.org/gass/'),
        ('Great Lakes Remote Sensing', 'http://greatlakesremotesensing.org/'),
        ('Great Lakes Submerged Aquatic Vegetation Map', 'http://geodjango.mtri.org/static/sav/'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/arthur-e/'),
        ('LinkedIn', 'www.linkedin.com/in/endsley'),
        ('BitBucket', 'http://bitbucket.org/kaendsle'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Image thumbnails plug-in
IMAGE_PATH = 'images' # /images in the output folder; /static/images is NOT for thumbnailers
THUMBNAIL_DIR = 'images/thumbs'

# Theme info
BANNER = 'theme/images/kml_globe.jpg'
BANNER_TITLE = 'Computational Geoscience & Remote Sensing'
BANNER_SUBTITLE = '''
I write about systematic observation, modeling, and analysis of the Earth's surface changes&mdash;<a href="http://spatial.mtri.org/flux/">I study the visualization of spatially and temporally varying phenomena <i class="fa fa-external-link-square"></i></a>
'''
BOOTSTRAP_THEME = 'sandstone'
CC_LICENSE = 'CC-BY-NC-SA'
CUSTOM_CSS = 'theme/css/custom.css'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_INLINE = True
PYGMENTS_STYLE = 'solarizeddark'
