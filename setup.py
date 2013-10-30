from distutils.core import setup

import digg_paginator

setup(
    name = "django-digg-paginator",
    version = digg_paginator.__version__,
    packages = ["django-digg-paginator"],
    url = 'https://github.com/alrusdi/django_digg_paginator',
    author = 'pixel',
    author_email = 'ivan.n.sergeev@gmail.com',
    maintainer = 'pixel',
    maintainer_email = 'ivan.n.sergeev@gmail.com',
    license = 'GPL3',
    description = 'Digg-like Paginator from Django Snippets',
    long_description = open('README', 'r').read(),
    download_url = 'https://github.com/alrusdi/django_digg_paginator/archive/master.zip',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
