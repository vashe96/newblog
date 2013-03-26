from django import template
#from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from blog.views import search, search_form

register = template.Library()

def do_search_form(parser, token):
    return SearchForm()

register.tag('search_form', do_search_form)

class SearchForm(template.Node):
    def render(self, context):
      #  request = context.get('request')
       # assert request, 'ddasdas'
        return render_to_string('search.html')



