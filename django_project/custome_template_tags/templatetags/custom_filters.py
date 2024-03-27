from django import template

register = template.Library()

@register.filter
def to_upper(value):
    return value.upper()

@register.filter
def add(value):
    return value+100