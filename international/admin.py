# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Zone)
admin.site.register(Tariff)