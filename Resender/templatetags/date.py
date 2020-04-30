from django import template
from django.conf import settings


register = template.Library()


@register.filter
def transform_date(value):
    return f'{value.hour}:{value.minute}'
