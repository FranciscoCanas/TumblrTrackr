from django.conf.urls import patterns, include, url
import handlers
import tracker
import testquery

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# ex: /blog
	url(r'^blog$', handlers.add_blog),
        # ex: /blog/deezcouches/trends

	url(r'^blog/(?P<blog_name>.+)/trends$', handlers.get_blog_trends),

	# ex: /blogs/trends
	url(r'^blogs/trends$', handlers.get_trends),

	# Used for manually starting a tracking go go machine sandwich
	url(r'^track$', tracker.track), 
        url(r'^testq$', testquery.testquery),
        url(r'^ping$', handlers.ping) 
)



