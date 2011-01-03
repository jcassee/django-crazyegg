"""
Crazy Egg template tag.
"""

import re

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import Context, loader


ACCOUNT_RE = re.compile(r'^\d{8}$')
HTML_CODE = """
    <script>
      (function() {
        var ce = document.createElement("script");
        ce.src = document.location.protocol + '//dnn506yrbagrg.cloudfront.net/pages/scripts/%(account_number_1)s/%(account_number_2)s.js';
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(ce, s);
      })();
    </script>
"""


register = template.Library()

@register.simple_tag
def track_crazyegg():
    """
    Grazy Egg visit tracking template tag. Renders Javascript code to track
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
    return HTML_CODE % vars
