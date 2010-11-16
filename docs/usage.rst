
=====
Usage
=====

This section contains information, including examples, about how to use
*django-content-licenses* in your existing Django projects or applications.



1. Put 'content_licenses' module in PYTHON PATH

Configuration
-------------
settings.py:

INSTALLED_APPS = [
    'content_licenses',
]

Run: python manage.py syncdb

Import initial data with:

python manage.py loaddata content_licenses

( Dumped with:  python manage.py dumpdata --indent=4 content_licenses.License > content_licenses.json )

USAGE

Provides a modelfield:  LicenseField


Expected context (template variables)

content_title
content_url
author_name
author_url
license_name
license_url
extra_perms_title
extra_perms_url
template_name
pubdate
semantics

