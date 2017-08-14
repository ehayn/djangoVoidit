from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timesince import timesince
from django import template

register = template.Library()

@register.filter
def timesincemin(value):
    return timesince(value).split(', ')[0]