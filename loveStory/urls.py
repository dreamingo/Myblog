from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loveStory.views.home', name='home'),
    # url(r'^loveStory/', include('loveStory.foo.urls')),
    url(r'^$', 'myblog.views.userViews.index'),
    url(r'^index/$', 'myblog.views.userViews.index'),
    url(r'^article/$', 'myblog.views.articleViews.article'),
    url(r'^article/cat/(\d*)/$', 'myblog.views.articleViews.cat'),
    url(r'^addarticle/$', 'myblog.views.articleViews.addarticle'),
    url(r'^login/$', 'myblog.views.userViews.login'),
    url(r'^logout/', 'myblog.views.userViews.logout'),
    url(r'^delete?', 'myblog.views.articleViews.deleteblog'),
    url(r'^modify?', 'myblog.views.articleViews.modifyblog'),
    url(r'^showBlog?', 'myblog.views.articleViews.showblog'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
