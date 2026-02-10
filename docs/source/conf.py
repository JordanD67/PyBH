# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# autodoc_mock_imports
# This avoids autodoc breaking when it can't find packages imported in the code.
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_mock_imports # noqa: E501

autodoc_mock_imports = [
    "arviz",
    "lifelines",
    "matplotlib",
    "numpy",
    "pandas",
    "pytensor",
    "patsy",
    "pymc",
    "scipy",
    "seaborn",
    "sklearn",
    "xarray",
]

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PyBH"
copyright = "2025, Jean Van Dyk"
author = "Jean Van Dyk"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "sphinx.ext.mathjax",
    "myst_nb",
]

nb_execution_mode = "off"

source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
    ".myst": "myst-nb",
}

# Enable MyST math support for $...$, $$...$$, and \[...\]
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]
autosummary_generate = True  # génère les fichiers automatiquement
templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
