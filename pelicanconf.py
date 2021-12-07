AUTHOR = 'Amélie De Vecchi'
SITENAME = "Côte d'Or Classic Juniors"
SITEURL = ''

PATH = 'content'
DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']  #, 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = 'theme/pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = 'theme/pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'fr_FR'
DEFAULT_LANG = 'fr'
LOCALE = 'fr_FR'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# special content
HERO = [
  {
    'image': '/images/hero/background-1.jpg',
    'title': '16 Avril 2022 ~ Étape #1',
    'text': 'Darois - Précy-sous-Thil',
    'links': [
      {
        'icon': 'icon-code',
        'url': '#',
        'text': 'Détails'
      }
    ]
  }, {
    'image': '/images/hero/background-2.jpg',
    'title': '17 avril ~ Étape #2',
    'text': 'CLM  par équipe, 19 km  : Crugey - Vandenesse-en-Auxois',
    'links': [
      {
        'icon': 'icon-code',
        'url': '#',
        'text': 'Détails'
      }
    ]

  }, {
    'image': '/images/hero/background-3.jpg',
    'title': '18 Avril 2022 ~ Étape 3',
    'text': 'Pouilly-en-Auxois - Semur-en-Auxois',
'links': [
      {
        'icon': 'icon-code',
        'url': '#',
        'text': 'Détails'
      }
    ]


  },
  ]

