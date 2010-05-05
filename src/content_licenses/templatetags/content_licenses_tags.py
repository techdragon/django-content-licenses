# -*- coding: utf-8 -*-
#
#  This file is part of django-content-licenses.
#
#  django-content-licenses provides licensing for content.
#
#  Project development web site:
#
#      http://www.codetrax.org/projects/django-content-licenses
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

"""
In order to use these template tags you need to use the following in your templates

{% load content_licenses_tags %}

"""

from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.inclusion_tag('content_licenses/default.html', takes_context=True)
def embed_license(context):
    """
    
    THIS IS AN EXAMPLE.
    
    CREATE A TEMPLATE TAG LIKE THIS IN YOUR APP.
    
    rel-license Profile
    
    <head profile='http://microformats.org/profile/rel-license'>
    
    http://microformats.org/wiki/rel-license
    
    """
    entry = context['entry']
    return {
        'content_title': entry.title,
        'content_url': entry.get_absolute_url(),
        'author_name': author_name(entry.author),
        'author_url': reverse('author_profile', args=[entry.author.username]),
        'license_name': entry.license.name,
        'license_url': entry.license.url,
        'extra_perms_title': settings.PB_EXTRA_LICENSE_PERMISSIONS_PAGE_TITLE,
        'extra_perms_url': settings.PB_EXTRA_LICENSE_PERMISSIONS_PAGE_URL,
        'template_name': entry.license.template_name,
        'pubdate': entry.date_published,
    }

