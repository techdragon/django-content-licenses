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

from django.db import models


class License(models.Model):

    name = models.CharField(max_length=200, unique=True,
        help_text="""The full name of the license.""")
    slug = models.SlugField(unique=True)
    abbreviation = models.CharField(max_length=50, blank=True, null=True,
        help_text="""The short name of the license.""")
    url = models.URLField(verify_exists=True, blank=True, null=True,
        help_text="""The URL to the legal text/online representation of the license.""")
    logo = models.URLField(verify_exists=True, blank=True, null=True,
        help_text=""""A logo/icon/badge that is clearly associated with the license.""")
    description = models.TextField(blank=True, null=True)
    template = models.CharField(max_length=200,
        help_text="""Enter a relative path to the template for this license.""")
    is_active = models.BooleanField(default=True,
        help_text="""Disable, if license shouldn't be available to users any more.""")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = 'license'
        verbose_name_plural = 'licenses'

