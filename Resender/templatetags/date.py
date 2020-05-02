from django import template
from django.conf import settings
import datetime


register = template.Library()


@register.filter
def transform_date(value):
    date = (value + datetime.timedelta(hours=3)).strftime("%H:%M") 
    return date
