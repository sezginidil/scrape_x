# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Twitter Scraper'
copyright = '2023, Idil Sezgin.'
author = 'Idil Sezgin'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
     'sphinx.ext.doctest',
     'sphinx.ext.autodoc',
     'sphinx.ext.autosummary',
     'sphinx.ext.intersphinx',
     'sphinx.ext.viewcode',
     'sphinxcontrib.autodoc_pydantic'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

master_doc = 'index'
language = "en"

