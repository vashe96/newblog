from blog.models import Post
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from blog.forms import PostForm
from blog.forms import CommentForm
from blog.models import Comment
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

def tagpage(request, tag):
     
#    comments = Comment.objects.filter(post=post)
 #   d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
  #  d.update(csrf(request))

    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts":posts, "tag":tag, "author":author},)#, d)

def search_form(request):
    return render_to_response('search.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        post = Post.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'post': post, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
           new_post = form.save(commit=False)
           new_post.author = request.user
           new_post.save()
           return HttpResponseRedirect('/blog')
    else:
        form = PostForm()
    c = {'form': form}
    return render_to_response('create.html', c, context_instance=RequestContext(request))


def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect('/blog/%s' %pk)

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect('/blog')
    
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return HttpResponseRedirect('/blog/')

def show_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    c = {'post': post, 
         'comment_form' : CommentForm(),
         'comment_list' : Comment.objects.filter(post=post)
        }
    return render_to_response('post.html', c, context_instance=RequestContext(request))
    
    

