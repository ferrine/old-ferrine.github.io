from pelican_jupyter import markup as nb_markup
import nbconvert
import re


MARKUP = ("md", "ipynb")

PLUGINS = [nb_markup, "render_math"]
MATH_JAX = {'tex_extensions': ['color.js','mhchem.js']}

IPYNB_SKIP_CSS = True
IGNORE_FILES = [".ipynb_checkpoints"]


class SVGFixPreprocessor(nbconvert.preprocessors.ConvertFiguresPreprocessor):
    from_format = to_format = "image/svg+xml"
    RE_WIDTH_HEIGHT = re.compile(r'(width|height)="[^"]+"')

    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell,
        See base.py
        """

        # Loop through all of the datatypes of the outputs in the cell.
        for output in cell.get("outputs", []):
            if (
                output.output_type in {"execute_result", "display_data"}
                and self.from_format in output.data
            ):

                output.data[self.to_format] = self.convert_figure(
                    self.from_format, output.data[self.from_format]
                )

        return cell, resources

    def convert_figure(self, data_format, data):
        return self.RE_WIDTH_HEIGHT.sub("", data, 2)


IPYNB_PREPROCESSORS = [
    nbconvert.preprocessors.TagRemovePreprocessor(
        remove_cell_tags="remove_cell",
        remove_all_outputs_tags="remove_all_outputs",
        remove_single_output_tags="remove_single_output",
        remove_input_tags="remove_input",
    ),
    SVGFixPreprocessor(),
]

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"

PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}/index.html"
IPYNB_NB_SAVE_AS = ARTICLE_SAVE_AS.replace("index.html", "notebook.ipynb")
IPYNB_EXPORT_TEMPLATE = "theme/templates/nbconvert.html"

AUTHOR = "Maxim Kochurov"
SITENAME = "In Search of the Holy Posterior"
SITEURL = ""

PATH = "content"
THEME = "theme"
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ("Maxim Kochurov", "/pages/maxim-kochurov"),
    ("Teaching", "/pages/practical-bayes"),
    ("Categories", "/categories.html"), 
    ("Tags", "/tags.html"),
    ("Archives", "/archives.html"), 
)
USE_FOLDER_AS_CATEGORY = False
COLOR_SCHEME_CSS = "github.css"
HEADER_COVER = "images/header.jpg"
GRAPHVIZ_COMPRESS = False



TIMEZONE = "Europe/Moscow"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("telegram", "https://t.me/ferres"),
    ("twitter", "https://twitter.com/ferrine96"),
    ("linkedin", "https://www.linkedin.com/in/ferrine"),
    ("github", "https://github.com/ferrine/"),
    ("envelope", "mailto:max.kochurov@pymc-labs.io"),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    "images",
    "extra",
]

EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},  # and this
    "extra/override.css": {"path": "theme/css/override.css"},
}
CSS_OVERRIDE = "theme/css/override.css"
