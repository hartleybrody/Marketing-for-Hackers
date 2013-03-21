from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('landingpage.views',
    url(r'^$', 'index'),
    url(r'^submit/', 'submit'),
    url(r'^thanks/', 'thanks'),
    url(r'^author/', 'author'),
    url(r'^view/leads/', 'view_leads'),
    url(r'^update/leads/', 'update_leads'),
	(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)

