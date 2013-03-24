from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed


class BlogFeed(Feed):
    title = "MySite"
    descriprion = "Some ramblings of mine"
    link = "/blog/feed/"

    def items(self):
	return Post.objects.all().order_by("-created")[:2]
    def item_title(self, item):
	return item.title
    def item_description(self, item):
	return item.body
    def item_link(self, item):
	return u"/blog/%d" % item.id


urlpatterns = patterns('blog.views',
    # Examples:
    url(r'^$', ListView.as_view(
                              queryset=Post.objects.all().order_by("-created")[:2],
                              template_name="blog.html"), name='blog'),

    url(r'^(?P<pk>\d+)$', 'show_post',),

    url(r'^archives/$', ListView.as_view(
                              queryset=Post.objects.all().order_by("-created"),
                              template_name="archives.html")),

    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', BlogFeed()),
    
    
    url(r'^(?P<post_id>\d+)/del$', 'delete', name="delete_post"),
    url(r'^(?P<comment_id>\d+)/del$', 'delete', name="delete_comment"),

    
)
