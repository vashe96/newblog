from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from simplereg.forms import LoginForm
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.views import search, search_form, post, add_comment
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),
    # url(r'^newblog/', include('newblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   url(r'^add_comment/(\d+)/$', add_comment, name='add_comment'),
   url(r'^blog/', include('blog.urls'),),
   url(r'^search-form/$', search_form, name='search'),
   url(r'^search/$', search),
   url(r'^create/$', post, name='create'),

   url(r'^admin/', include(admin.site.urls)),
   
   url(r'^registration/$', 'simplereg.views.registration', {
            'template_name': 'registration.html',
            'autologin': True,
            'callback': None
        }, name='registration'),
   url(r'^login/$', 'django.contrib.auth.views.login', {
            'authentication_form': LoginForm
        }, name='login'),


)
