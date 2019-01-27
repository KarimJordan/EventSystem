import json

from django import template
from django.utils.safestring import mark_safe

from ..utils import decimal_default

register = template.Library()


@register.filter
def jsonify(obj):
    return mark_safe(json.dumps(obj, default=decimal_default))
