# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme
# -- Project information

project = 'Doku Adibidea'
copyright = '2023, Iosu Gomez Iturrioz'
author = 'Iosu Gomez'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx_rtd_theme",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ["_static"]

# -- Options for EPUB output
epub_show_urls = 'footnote'
