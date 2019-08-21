#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'K. Arthur Endsley'
SITENAME = "K. Arthur Endsley"
SITE_TITLE = "K. Arthur Endsley: On Computational Geoscience and Remote Sensing"
SITEURL = ''
THEME = 'themes/karthur'

PLUGIN_PATHS = ['/usr/local/pelican/pelican-plugins']
PLUGINS = ['feed_summary', 'related_posts', 'sitemap', 'thumbnailer', 'render_math', 'tag_cloud']

# Enable smart quotes
TYPOGRIFY = False

DISPLAY_PAGES_ON_MENU = True
MY_EMAIL_ADDR = 'endsley@umich.edu'
MY_UNICODE_EMAIL_ADDR = '&#101;&#110;&#100;&#115;&#108;&#101;&#121;&#64;&#117;&#109;&#105;&#99;&#104;&#46;&#101;&#100;&#117;'

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
STATIC_PATHS = ['images', 'static']
PAGE_PATHS = ['pages']

# After upgrading the additional menu bar items disappeared...
# MENUITEMS = [
#     ('About Me', '/pages/about-me.html'),
#     ('CV', '/pages/cv.html')
# ]

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_USE_SUMMARY = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATED_POSTS_MAX = 3

# Blogroll
LINKS = (('Michigan Tech Research Institute', 'http://www.mtri.org/'),
        ('UMich School for Environment and Sustainability', 'http://seas.umich.edu/'),
        ('Great Lakes Remote Sensing', 'http://www.greatlakesremotesensing.org/'),
        ('Rapid Response Erosion Database', 'http://geodjango.mtri.org/geowepp/'),
        ('Bering Glacier Monitoring', 'http://www.beringglacier.org/'),)

# Should be (date, title, URL, journal name)
PUBLICATIONS = (
        ('2019-01', '...Soil moisture monitoring...in a mountain watershed', 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2018WR023653', 'Water Resources Research'),
        ('2018-04', '...Disparities in urban and metropolitan vegetation', 'https://doi.org/10.1007/s10021-018-0242-4', 'Ecosystems'),
        ('2016-10', 'Rapid-response tools and datasets for post-fire remediation...', 'http://www.publish.csiro.au/wf/WF15162', 'International Journal of Wildland Fire'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/arthur-e/'),
        ('LinkedIn', 'http://www.linkedin.com/in/endsley'),
        ('BitBucket', 'http://bitbucket.org/kaendsle'),
        ('RSS', '/feeds/blog.atom.xml'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

###########
# Plug-ins

# Sitemap plug-in
SITEMAP = {
    'format': 'xml',
    'changefreqs': {
        'articles': 'monthly',
        'pages': 'monthly',
        'indexes': 'monthly'
    }
}

# Image thumbnails plug-in
IMAGE_PATH = 'images' # /images in the output folder; /static/images is NOT for thumbnailers
THUMBNAIL_DIR = 'images/thumbs'

# Theme info
BANNER = 'theme/images/LA_county.jpg'
BANNER_TITLE = 'Computational Geoscience & Remote Sensing'
BANNER_SUBTITLE = '''
I write about systematic observation, modeling, and analysis of the Earth's surface changes&mdash;<a href="https://doi.org/10.1007/s10021-018-0242-4">I currently study the human factors driving urban land-cover changes <i class="fa fa-external-link-square"></i></a>
'''
BOOTSTRAP_THEME = 'sandstone'
CC_LICENSE = 'CC-BY-SA'
CUSTOM_CSS = 'theme/css/custom.css'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_INLINE = True
PYGMENTS_STYLE = 'custom-pygments'
