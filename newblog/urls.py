from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newblog.views.home', name='home'),
    # url(r'^newblog/', include('newblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
)
