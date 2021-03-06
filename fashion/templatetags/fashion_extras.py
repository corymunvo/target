from django import template
from django.utils.text import normalize_newlines
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()

def remove_newlines(text):
    """
    Removes all newline characters from a block of text.
    """
    # First normalize the newlines using Django's nifty utility
    normalized_text = normalize_newlines(text)
    # Then simply remove the newlines like so.
    return mark_safe(normalized_text.replace('\n', ' '))
    
remove_newlines.is_safe = True
remove_newlines = stringfilter(remove_newlines)
register.filter(remove_newlines)

@register.simple_tag()
def multiply(qty, unit_price):
    # you would need to do any localization of the result here
    return qty * unit_price

