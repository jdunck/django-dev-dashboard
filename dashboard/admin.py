from __future__ import absolute_import

from django.contrib import admin
from .models import TracTicketMetric, Datum

admin.site.register(TracTicketMetric, 
    list_display = ('name', 'query'),
    prepopulated_fields = {'slug': ['name']},
)

admin.site.register(Datum, 
    list_display = ('timestamp', 'metric', 'measurement'),
)