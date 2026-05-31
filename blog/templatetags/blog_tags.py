from django import template
import datetime
from blog.models import Comments

register = template.Library()


@register.simple_tag
def salam():
    return "salam Django "

@register.simple_tag
def multiply(a, b):
    return a * b

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def mahboob_post():
    all_posts = Comments.objects.all() 
    return {'posts': all_posts}