from django import template
from newblog.views import search, search_form

register = template.Library()
register.simple_tag(takes_context=True)(search_form)
