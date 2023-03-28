#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'K. Arthur Endsley'
SITENAME = "K. Arthur Endsley"
SITE_TITLE = "K. Arthur Endsley: On Computational Geoscience and Remote Sensing"
SITEURL = ''
THEME = 'themes/karthur'

# Until pelican-plugins/render_math is fixed (or new render-math is fixed);
#   use an older version of pelican-plugins:
#   git checkout 560b6ad61ade9e73d7482abdf4d8287032817631
PLUGIN_PATHS = ['/usr/local/pelican/pelican-plugins']
PLUGINS = ['feed_summary', 'related_posts', 'sitemap', 'thumbnailer', 'tag_cloud', 'render_math']

# Enable smart quotes
TYPOGRIFY = False

DISPLAY_PAGES_ON_MENU = True
MY_EMAIL_ADDR = 'endsley@umich.edu'
MY_UNICODE_EMAIL_ADDR = '&#101;&#110;&#100;&#115;&#108;&#101;&#121;&#64;&#117;&#109;&#105;&#99;&#104;&#46;&#101;&#100;&#117;'
MY_GOOGLE_SCHOLAR = 'https://scholar.google.com/citations?user=BVkU3hcAAAAJ&hl=en'

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
STATIC_PATHS = ['images', 'static']
PAGE_PATHS = ['pages']

# After upgrading the additional menu bar items disappeared...
MENUITEMS = [
    ('About Me', '/pages/about-me.html'),
    ('CV', '/pages/cv.html')
]

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
LINKS = (('Numerical Terradynamic Simulation Group', 'https://ntsg.umt.edu/'),
        ('W.A. Franke College of Forestry and Conservation', 'https://www.cfc.umt.edu/'),
        ('Rapid Response Erosion Database', 'http://geodjango.mtri.org/geowepp/'),
        ('Great Lakes Remote Sensing', 'http://www.greatlakesremotesensing.org/'),
        ('Bering Glacier Monitoring', 'http://www.beringglacier.org/'),)

# Should be (date, title, URL, journal name)
PUBLICATIONS = (
    ('2023-01', 'Carbon uptake in Eurasian Boreal forests...', 'https://onlinelibrary.wiley.com/doi/10.1111/gcb.16553', 'Global Change Biology'),
    ('2022-03', 'Soil respiration phenology...in northern hemisphere', 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021MS002804', 'JAMES'),
    ('2021-05', 'Impacts of climate and wildfire on GPP...in Alaska', 'https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2020JG006078', 'JGR: Biogeosciences'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/arthur-e/'),
    ('BitBucket', 'http://bitbucket.org/endsley'),
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
I write about systematic observation, modeling, and analysis of the Earth's surface changes&mdash;<a href="https://eos.org/research-spotlights/a-global-look-at-surface-soil-organic-carbon">I currently study patterns and trends in the terrestrial carbon cycle <i class="fa fa-external-link-square"></i></a>
'''
BOOTSTRAP_THEME = 'sandstone'
CC_LICENSE = 'CC-BY-SA'
CUSTOM_CSS = 'theme/css/custom.css'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_INLINE = True
PYGMENTS_STYLE = 'custom-pygments'
