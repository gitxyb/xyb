from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rogue.views.home', name='home'),
    # url(r'^rogue/', include('rogue.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
	url(r'^regist/$','blog.views.user_regist'),
	url(r'^login/$','blog.views.user_login'),
	url(r'^index/$','blog.views.index'),
	url(r'^logout/$','blog.views.user_logout'),
	url(r'^post/(\d+)/$','blog.views.post'),
	url(r'^post_show/(\d+)/$','blog.views.post_show'),
	url(r'^replay/(\d+)/$','blog.views.replay'),
	url(r'^replay_show/(\d+)/','blog.views.replay_show'),
	url(r'^replay_user_show/(\d+)/$','blog.views.replay_user_show'),
)
