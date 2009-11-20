# fork from original django basic apps for packaging purposes

from setuptools import setup, find_packages

setup(name='django-basic-apps',
    version='0.6',
    description='Basic Django applications',
    long_description='fork of djang-basic-apps to package it with setuptools',
    author='Nathan Borror',
    #author_email='',
    classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    #url='http://code.google.com/p/django-basic-apps/',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    #package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'Django',
      'django-tagging',
      'beautifulsoup',
    ],
    entry_points="""""",
    )
