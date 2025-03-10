#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas','nltk >= 3.6.5','Sastrawi >= 1.0.1','spacy >= 3.3.1']

test_requirements = ['pytest>=3', ]

setup(
    author="Arief Akbar Hidayat",
    author_email='hidayat.ariefakbar@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

    ],
    description="Easy NLP implementation for Indonesian Language",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='straycat',
    name='straycat',
    packages=find_packages(include=['straycat', 'straycat.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hradkafeira/straycat',
    version='0.1.9',
    zip_safe=False,
)