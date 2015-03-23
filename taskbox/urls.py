from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),


    url(r'^$', 'socialauth.views.login'),
    url(r'^home/$', 'socialauth.views.home'),
    url(r'^logout/$', 'socialauth.views.logout'),

)
