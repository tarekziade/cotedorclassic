AUTHOR = "Anthony De Vecchi"
SITENAME = "Côte d'Or Classic Juniors"
SITEURL = ""

PATH = "content"
DEFAULT_LANG = "fr"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["blog"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# logo path, needs to be stored in PATH Setting
LOGO = "/images/logo.svg"

DEFAULT_PAGINATION = False

# plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites"]  # , 'tipue_search']
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# theme and theme localization
THEME = "theme/pelican-fh5co-marble"
I18N_GETTEXT_LOCALEDIR = "theme/pelican-fh5co-marble/locale/"
I18N_GETTEXT_DOMAIN = "messages"
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = "Europe/Paris"
DEFAULT_DATE_FORMAT = "%a, %d %b %Y"
I18N_TEMPLATES_LANG = "fr_FR"
DEFAULT_LANG = "fr"
LOCALE = "fr_FR"


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# special content
HERO = [
    {
        "image": "/images/hero/background-1.jpg",
        "title": "16 Avril ~ Étape #1",
        "text": "Darois ➔ Précy-sous-Thil",
        "links": [
            {"icon": "icon-code", "url": "/pages/etape1.html", "text": "Détails"}
        ],
    },
    {
        "image": "/images/hero/background-2.jpg",
        "title": "17 avril ~ Étape #2",
        "text": "Crugey ➔ Vandenesse-en-Auxois",
        "links": [
            {"icon": "icon-code", "url": "/pages/etape2.html", "text": "Détails"}
        ],
    },
    {
        "image": "/images/hero/background-3.jpg",
        "title": "18 Avril ~ Étape 3",
        "text": "Pouilly-en-Auxois ➔ Semur-en-Auxois",
        "links": [
            {"icon": "icon-code", "url": "/pages/etape3.html", "text": "Détails"}
        ],
    },
]

ABOUT = {
  'image': '/images/about/about.jpeg',
  'mail': 'info@gitcd.io',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'Learn more about the creator of this theme or just drop a message.',
    'de': 'Lernen Sie den Author kennen oder hinterlassen Sie einfach eine Nachricht'
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Zürich, Schweiz',
  'phone': '+555-shoe'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = False
DISPLAY_PAGES_ON_HOME = False
DISPLAY_CATEGORIES = False
DISPLAY_TAGS = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'


MENUITEMS = [
  ('Présentation', 'pages/presentation.html'),
  ('Étape 1', 'pages/etape1.html'),
  ('Étape 2', 'pages/etape2.html'),
  ('Étape 3', 'pages/etape3.html'),
  ('Infos', 'pages/infos.html')
]

DIRECT_TEMPLATES = [
  'index',
  #'tags',
  #'categories',
  #'authors',
  #'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'
