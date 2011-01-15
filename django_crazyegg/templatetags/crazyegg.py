"""
Crazy Egg template tag.
"""

import re

from django import template
from django.conf import settings
from django.template import Node, TemplateSyntaxError


ACCOUNT_RE = re.compile(r'^\d{8}$')
TRACK_CODE = u"<script type=\"text/javascript\">document.write(unescape('%%3Cscript type=\"text/javascript\" src=\"'+document.location.protocol+'//dnn506yrbagrg.cloudfront.net/pages/scripts/%(account_number_1)s/%(account_number_2)s.js\"%%3E%%3C%%2Fscript%%3E'))</script>"
SET_CODE = u"<script type=\"text/javascript\">CE2.set(%(variable)d,'%(value)s');</script>"


register = template.Library()

def track_crazyegg(parser, token):
    """
    Crazy Egg visit tracking template tag.

    Renders Javascript code to track page visits.  You must supply your
    Crazy Egg account number (as a string) in the
    ``CRAZYEGG_ACCOUNT_NUMBER`` setting.
    """
    bits = token.split_contents()
    if len(bits) > 1:
        raise TemplateSyntaxError("'%s' takes no arguments" % bits[0])
    return TrackCrazyEggNode()

class TrackCrazyEggNode(Node):
    def __init__(self):
        try:
            account_number = settings.CRAZYEGG_ACCOUNT_NUMBER
        except AttributeError:
            raise CrazyEggException(
                    "CRAZYEGG_ACCOUNT_NUMBER setting not found")
        self.account_number = str(account_number)
        if not ACCOUNT_RE.search(self.account_number):
            raise CrazyEggException("CRAZYEGG_ACCOUNT_NUMBER setting must be "
                    "a string containing an eight-digit number: %s"
                        % account_number)
        self.internal_ips = getattr(settings, 'CRAZYEGG_INTERNAL_IPS', ())

    def render(self, context):
        try:
            request = context['request']
            remote_ip = request.META.get('HTTP_X_FORWARDED_FOR',
                    request.META.get('REMOTE_ADDR', ''))
            if remote_ip in self.internal_ips:
                return ""
        except KeyError:
            pass
        vars = {
            'account_number_1': self.account_number[:4],
            'account_number_2': self.account_number[4:],
        }
        return TRACK_CODE % vars

register.tag('track_crazyegg', track_crazyegg)


@register.simple_tag
def set_uservar(variable, value):
    """
    Crazy Egg user variable setting template tag.

    Renders Javascript code to set a user variable.  The `variable`
    argument is a number between 1 and 5.  The `value` argument is a
    string of no more than 100 characters.
    """
    try:
        var_num = int(variable)
    except ValueError:
        raise CrazyEggException("not a numeric variable: %s" % variable)
    if not 1 <= var_num <= 5:
        raise CrazyEggException("variable must be between 1 and 5: %s"
                % variable)
    val_str = str(value)
    if len(val_str) > 100:
        raise CrazyEggException(
                "value must be no longer than 100 character: %s" % value)
    vars = {
        'variable': var_num,
        'value': val_str.replace("'", "\\'"),
    }
    return SET_CODE % vars


class CrazyEggException(Exception):
    """
    Indicates an error with the Crazy Egg set-up.

    This exception is silenced in Django templates.
    """

    silent_variable_failure = True
