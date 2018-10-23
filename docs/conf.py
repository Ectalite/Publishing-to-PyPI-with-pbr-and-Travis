import datetime
import sphinx_rtd_theme

now = datetime.datetime.now()

project = 'Automate your publishing to PyPI with PBR and Travis'
copyright = '2018-{}, 73VW'.format(now.year)
author = '73VW'

version = '1.0'
release = version

extensions = [
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

exclude_patterns = ['_build']

htmlhelp_basename = 'AutomateYourPublishingToPyPIWithPBRAndTravis'

latex_documents = [
    (master_doc, 'AutomateyourpublishingtoPyPIwithPBRandTravis.tex', 'Automate your publishing to PyPI with PBR and Travis Documentation',
     author, 'manual'),
]

man_pages = [
    (master_doc, 'AutomateyourpublishingtoPyPIwithPBRandTravis', 'Automate your publishing to PyPI with PBR and Travis Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'AutomateyourpublishingtoPyPIwithPBRandTravis', 'Automate your publishing to PyPI with PBR and Travis Documentation',
     author, 'AutomateyourpublishingtoPyPIwithPBRandTravis', 'One line description of project.',
     'Miscellaneous'),
]

language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'style_external_links': True,
}