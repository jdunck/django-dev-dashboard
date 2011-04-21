from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'dashboard.views.index', name="dashboard-index"),
    url(r'^admin/', include(admin.site.urls)),
)
