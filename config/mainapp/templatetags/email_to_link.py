from django import template
from django.utils.safestring import mark_safe
from datetime import datetime


register = template.Library()


@register.filter
def email_to_link(value):
    return mark_safe(f"<a href='mailto:{value}'>{value}</a>")