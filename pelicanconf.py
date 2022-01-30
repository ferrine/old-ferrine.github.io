from pelican_jupyter import markup as nb_markup

MARKUP = ("md", "ipynb")

PLUGINS = [nb_markup]
IPYNB_SKIP_CSS = True
IGNORE_FILES = [".ipynb_checkpoints"]


AUTHOR = 'Maxim Kochurov'
SITENAME = 'In Search of the Holy Posterior'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
MENUITEMS = (
    ("Categories", "categories"),
)
COLOR_SCHEME_CSS = 'github.css'
HEADER_COVER = "images/header.jpg"
GRAPHVIZ_COMPRESS = False


TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ferrine96'),
          ('github', 'https://github.com/ferrine'),
          ('envelope', 'mailto:max.kochurov@pymc-labs.io'))

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'images',
    'extra',  # this
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
}
GOOGLE_ANALYTICS = "UA-98661135-1"
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
