#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2010 George Notaras, G-Loaded.eu, CodeTRAX.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  NOTES
#
#  Create source distribution tarball:
#    python setup.py sdist --formats=gztar
#
#  Create binary distribution rpm:
#    python setup.py bdist --formats=rpm
#
#  Create binary distribution rpm with being able to change an option:
#    python setup.py bdist_rpm --release 7
#
#  Test installation:
#    python setup.py install --prefix=/usr --root=/tmp
#
#  Install:
#    python setup.py install
#  Or:
#    python setup.py install --prefix=/usr
#

from setuptools import setup

if __name__=='__main__':
    setup(
        name = 'django-content-licenses',
        version = '0.1.0',
        author = 'George Notaras',
        author_email = 'gnot@g-loaded.eu',
        maintainer = 'George Notaras',
        maintainer_email = 'gnot@g-loaded.eu',
        url = 'https://source.codetrax.org/hgroot/django-content-licenses',
        description = 'Provides a license field.',
        long_description = 'Provides a license field.',
        download_url = 'https://source.codetrax.org/hgroot/django-content-licenses',
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        license = 'Apache License version 2',
        packages = [
            'content_licenses',
        ],
        package_dir = {'': 'src'},
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            'Django',
        ],
    )

