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


class LicenseField(models.ForeignKey):

    def __init__(self, **kwargs):
        super(LicenseField, self).__init__('content_licenses.License',
            related_name='%(class)s_license', **kwargs)

