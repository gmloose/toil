# Toil documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 25 12:37:16 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import sys
import os
import inspect
import re
from datetime import datetime
import toil.version
import time

# This makes the modules located in docs/vendor/sphinxcontrib available to import
sphinxPath = os.path.abspath(os.path.join(os.path.pardir, os.path.dirname('docs/vendor/sphinxcontrib/')))
sys.path.append(sphinxPath)
import fulltoc


def fetch_parent_dir(filepath: str, n: int = 1):
    '''
    Returns a parent directory, n places above the input filepath.

    Equivalent to something like: '/home/user/dir'.split('/')[-2] if n=2.
    '''
    filepath = os.path.realpath(filepath)
    for i in range(n):
        filepath = os.path.dirname(filepath)
    return os.path.basename(filepath)

path_to_dir = os.path.dirname(os.path.abspath(__file__))

# Example of toil.version.__file__ on sphinx:
# /home/docs/checkouts/readthedocs.org/user_builds/toil/envs/3.13.0/local/lib/python2.7/site-packages/toil-3.13.0a1-py2.7.egg/toil/version.pyc
envPath = os.path.abspath(toil.version.__file__)

# Example of __file__ on sphinx:
# /home/docs/checkouts/readthedocs.org/user_builds/toil/checkouts/3.13.0/docs/conf.py
wdPath_version = fetch_parent_dir(__file__, 2)
# Expected output: 3.13.0

assert wdPath_version in envPath, "Another Toil installation seems to have precedence over this working directory."
toilVersion = toil.version.baseVersion

# -- General configuration ------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'fulltoc',
]

intersphinx_mapping = {'python': ('https://docs.python.org/3', None),}

# Link definitions available everywhere so we don't need to keep repeating ourselves.
rst_epilog = """
.. _Common Workflow Language: http://www.commonwl.org/
"""

def skip(app, what, name, obj, skip, options):
    return name != '__init__' and (skip
                                   or inspect.isclass(obj)
                                   or name.startswith('_') and not inspect.ismodule(obj))

def setup(app):
    app.connect('autodoc-skip-member', skip)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.  Specify multiple suffix as list of string:
# Example: source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Toil'
build_date = datetime.utcfromtimestamp(int(os.environ.get('SOURCE_DATE_EPOCH', time.time())))
copyright = f'2015 – {build_date.year} UCSC Computational Genomics Lab'
author = 'UCSC Computational Genomics Lab'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = re.split('[A-Za-z]', toilVersion)[0]
# The full version, including alpha/beta/rc tags.
release = toilVersion

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, 2do and 2doList produce output, else they produce nothing.
todo_include_todos = True

# Include doc string for __init__ method in the documentation
autoclass_content = 'class'
autodoc_member_order = 'bysource'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'
html_theme_options = {
    "github_banner": True,
    "github_user": "BD2KGenomics",
    "github_repo": "toil",
    "caption_font_size": "24px"
}

# The name of an image file (relative to this directory) to place at the top of the sidebar.
html_logo = "_static/logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'Toildoc'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {}
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'Toil.tex', 'Toil Documentation', author, 'manual')]

# -- Options for manual page output ---------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'toil', 'Toil Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [(master_doc, project, 'Toil Documentation', author, project, project, 'Miscellaneous')]
