YEAR = "{{YEAR}}"

YEARS_LIST = ["2025", "2024", "2023", "2022"]

# Year-specific content (except MENUITEMS)
YEARS = {
    "2025": {
        "ETAPES": [
            ("8 Juin ~ Étape 1", "Saulieu ➔ Précy-sous-Thil"),
            ("8 Juin ~ Étape 2", "Pouillenay ➔ MuseoParc d’Alésia"),
            ("9 Juin ~ Étape 3", "Pouilly-en-Auxois ➔ Semur-en-Auxois"),
        ],
        "LOGO": "/images/logo.svg",
        "LIVRET": "/images/livret-2025.pdf",
    },
    "2024": {
        "ETAPES": [
            ("8 Juin ~ Étape 1", "Saulieu ➔ Précy-sous-Thil"),
            ("8 Juin ~ Étape 2", "MuséoParc d’Alésia  ➔ Vitteaux"),
            ("9 Juin ~ Étape 3", "Pouilly-en-Auxois ➔ Semur-en-Auxois"),
        ],
        "LOGO": "/2024/images/logo.svg",
        "LIVRET": "/2024/images/livret-2024.pdf",
    },
    "2023": {
        "ETAPES": [
            ("15 Avril ~ Étape 1", "Saulieu ➔ Précy-sous-Thil"),
            ("16 Avril ~ Étape 2", "Époisses ➔ Époisses"),
            ("16 Avril ~ Étape 3", "Pouilly-en-Auxois ➔ Semur-en-Auxois"),
        ],
        "LOGO": "/2023/images/logo.svg",
        "LIVRET": "2023/images/Livret-public-COCJ-2023.pdf",
    },
    "2022": {
        "ETAPES": [
            ("16 Avril ~ Étape 1", "Darois ➔ Précy-sous-Thil"),
            ("17 Avril ~ Étape 2", "Crugey ➔ Vandenesse-en-Auxois"),
            ("17 Avril ~ Étape 3", "Pouilly-en-Auxois ➔ Semur-en-Auxois"),
        ],
        "LOGO": "/2022/images/logo.svg",
        "LIVRET": "/2022/images/livret_public.pdf",
    },
}

# Inject MENUITEMS dynamically into YEARS
for year in YEARS_LIST:
    menuitems = []
    for other_year in YEARS_LIST:
        if year == other_year:
            continue
        if other_year == YEARS_LIST[0]:
            slug = "/index.html"
        else:
            slug = f"/{other_year}/index.html"

        menuitems.append((f"Épreuve {other_year}", slug))

    YEARS[year]["MENUITEMS"] = menuitems


MENUITEMS = [
    ("Présentation", "pages/presentation.html"),
    ("Étape 1", "pages/etape1.html"),
    ("Étape 2", "pages/etape2.html"),
    ("Étape 3", "pages/etape3.html"),
    ("Infos", "pages/infos.html"),
    ("Partenaires", "pages/partenaires.html"),
    ("Livret Public", YEARS[YEAR]["LIVRET"]),
    ("Contact", "contact.html"),
]

MENUITEMS.extend(YEARS[YEAR]["MENUITEMS"])
LOGO = YEARS[YEAR]["LOGO"]

ETAPES = YEARS[YEAR]["ETAPES"]
HERO = []

for i, (title, text) in enumerate(ETAPES):
    if YEAR == YEARS_LIST[0]:
        etape_url = f"/pages/etape{i+1}.html"
        image_url = f"/images/hero/background-{i+1}.jpg"
    else:
        etape_url = f"/{YEAR}/pages/etape{i+1}.html"
        image_url = f"/{YEAR}/images/hero/background-{i+1}.jpg"

    HERO.append(
        {
            "image": image_url,
            "title": title,
            "text": text,
            "links": [{"icon": "icon-code", "url": etape_url, "text": "Détails"}],
        }
    )

#
# Below is the common parts
#
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
