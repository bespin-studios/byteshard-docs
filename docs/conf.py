# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'byteShard'
copyright = '2024, Bespin Studios GmbH'
author = 'Lars Hennig, Jonas Bönhoff'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    "display_github": True,
    "github_repo": "https://github.com/bespin-studios/byteshard-docs",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

html_theme_options = {
    "style_external_links": True,
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "titles_only": False,
    "display_github": True,
    "github_repo": "https://github.com/bespin-studios/byteshard-docs"
    "github_version": "main",
    "conf_py_path": "/docs/",
}
