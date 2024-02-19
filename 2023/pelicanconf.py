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
LOGO = "/2023/images/logo.svg"

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
RELATIVE_URLS = True

# special content
HERO = [
    {
        "image": "/images/hero/background-1.jpg",
        "title": "15 Avril ~ Étape 1",
        "text": "Saulieu ➔ Précy-sous-Thil",
        "links": [
            {"icon": "icon-code", "url": "/pages/etape1.html", "text": "Détails"}
        ],
    },
    {
        "image": "/images/hero/background-2.jpg",
        "title": "16 avril ~ Étape 2",
        "text": "Époisses ➔ Époisses",
        "links": [
            {"icon": "icon-code", "url": "/pages/etape2.html", "text": "Détails"}
        ],
    },
    {
        "image": "/images/hero/background-3.jpg",
        "title": "16 Avril ~ Étape 3",
        "text": "Pouilly-en-Auxois ➔ Semur-en-Auxois",
        "links": [
            {"icon": "icon-code", "url": "/pages/etape3.html", "text": "Détails"}
        ],
    },
]

ABOUT = {
    "mail": "cotedorclassicjuniors@gmail.com",
    "phone": "07.68.97.14.35",
    "text": "Contacter Anthony",
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = False
DISPLAY_PAGES_ON_HOME = False
DISPLAY_CATEGORIES = False
DISPLAY_TAGS = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = "order"


MENUITEMS = [
    ("Présentation", "pages/presentation.html"),
    ("Étape 1", "pages/etape1.html"),
    ("Étape 2", "pages/etape2.html"),
    ("Étape 3", "pages/etape3.html"),
    ("Infos", "pages/infos.html"),
    ("Partenaires", "pages/partenaires.html"),
    ("Livret Public", "images/Livret-public-COCJ-2023.pdf"),
    ("Contact", "contact.html"),
    ("A propos", "pages/mentions.html"),
    ("Épreuve 2024", "/index.html"),
    ("Épreuve 2022", "/2022/index.html"),
]

DIRECT_TEMPLATES = [
    "index",
    #'tags',
    #'categories',
    #'authors',
    #'archives',
    "search",  # needed for tipue_search plugin
    "contact",  # needed for the contact form
]

SOCIAL = (
    ("Facebook", "https://www.facebook.com/lacotedorclassicjuniors"),
    ("Instagram", "https://instagram.com/lacotedorclassicjuniors"),
)


GOOGLE_MAPS_KEY = False  #'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'
