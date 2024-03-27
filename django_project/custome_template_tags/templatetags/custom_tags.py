from django import template
import random

register = template.Library()

@register.simple_tag
def random_number():
    return random.randint(1,200)