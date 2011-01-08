"""
Crazy Egg template tag.
"""

import re

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import Context, loader


ACCOUNT_RE = re.compile(r'^\d{8}$')
TRACK_CODE = u"<script type=\"text/javascript\">document.write(unescape('%%3Cscript type=\"text/javascript\" src=\"'+document.location.protocol+'//dnn506yrbagrg.cloudfront.net/pages/scripts/%(account_number_1)s/%(account_number_2)s.js\"%%3E%%3C%%2Fscript%%3E'))</script>"
SET_CODE = u"<script type=\"text/javascript\">CE2.set(%(variable)d,'%(value)s');</script>"


register = template.Library()

@register.simple_tag
def track_crazyegg():
    """
    Crazy Egg visit tracking template tag. Renders Javascript code to track
    a page visits.

    You must set CRAZYEGG_ACCOUNT_NUMBER = "XXXXXXXX" in your settings.py, else
    this tag silently renders the empty string.
    """
    account_number = getattr(settings, 'CRAZYEGG_ACCOUNT_NUMBER', '')
    if not account_number:
        return ""
    if not ACCOUNT_RE.search(account_number):
        raise ImproperlyConfigured("CRAZYEGG_ACCOUNT_NUMBER setting must be "
                "a string containing an eight-digit number")
    vars = {
        'account_number_1': account_number[:4],
        'account_number_2': account_number[4:],
    }
    return TRACK_CODE % vars


@register.simple_tag
def set_uservar(variable, value):
    """
    Crazy Egg user variable setting template tag. Renders Javascript code to
    set a user variable. The `variable` argument is a number between 1 and 5.
    The `value` argument is a string of no more than 100 characters.
    """
    try:
        var_num = int(variable)
    except ValueError:
        raise CrazyEggVariableError("not a numeric variable: %s" % variable)
    if not 1 <= var_num <= 5:
        raise CrazyEggVariableError("variable must be between 1 and 5: %s"
                % variable)
    val_str = str(value)
    if len(val_str) > 100:
        raise CrazyEggVariableError(
                "value must be no longer than 100 character: %s" % value)
    vars = {
        'variable': var_num,
        'value': val_str.replace("'", "\\'"),
    }
    return SET_CODE % vars


class CrazyEggVariableError(Exception):
    """
    Indicates an error with the Crazy Egg set-up. This exception is silenced
    in Django templates.
    """

    silent_variable_failure = True
