"""
================================
Crazy Egg integration for Django
================================

The django-crazyegg application integrates `Crazy Egg`_ heatmaps into a
Django_ project.

.. _`Crazy Egg`: http://www.crazyegg.com/
.. _Django: http://www.djangoproject.com/


Overview
========

Crazy Egg is an easy to use hosted web application that generates
heatmaps from webpage visitor clicks.  It allows you to discover the
areas of web pages that are most important to your visitors.  This
Django application provides template tags that make integration of
Crazy Egg very simple.


Installation and configuration
==============================

To install django-crazyegg, simply place the ``django_crazyegg``
package somewhere on the Python path.  The application is configured in
the project ``settings.py`` file.  In order to use the template tags,
the ``django_crazyegg`` package must be present in the
``INSTALLED_APPS`` list::

    INSTALLED_APPS = [
        ...
        'django_crazyegg',
        ...
    ]

You set your Crazy Egg account number in the ``CRAZYEGG_ACCOUNT_NUMBER``
setting::

    CRAZYEGG_ACCOUNT_NUMBER = '12345678'


Usage
=====

The django-crazyegg application provides two template tags: one to track
visitor clicks, and one to register user variables.  In order to use the
tags in a template, first load the django-crazyegg template library by
adding ``{% load crazyegg %}`` at the top.


Tracking visitor clicks
-----------------------

Crazy Egg uses Javascript to track every visitor click. The
``track_crazyegg`` tag inserts the tracking code in the HTML page.  The
Crazy Egg web pages recommend adding the code directly before the
closing ``</body>`` HTML tag::

        ...
        {% track_crazyegg %}
    </body>
    </html>

.. note::

    Versions of django-crazyegg prior to 2.0.0 used asynchronous
    loading to allow the tag to be added to the HTML head section.
    Unfortunately, that caused problems if you wanted to set user
    variables (see below).

Even if you only track clicks on a specific page, you can still insert
the tracking tag into your base template.  The code will only install
the Javascript event handler on URLs that you have created snapshots
for.

Often you do not want to track clicks from your development or internal
IP addresses.  For this reason you can set the ``CRAZYEGG_INTERNAL_IPS``
to a list or tuple of addresses that the template tag will not be
rendered on::

    CRAZYEGG_INTERNAL_IPS = ['192.168.45.2', '192.168.45.5']

If you already use the ``INTERNAL_IPS`` setting, you could set the
Crazy Egg internal addreses to this value.  This will be the default
from version 3.0.0 upwards.

.. note::

    The template tag can only access the visitor IP address if the
    HTTP request is present in the template context as the ``request``
    variable.  For this reason, the ``CRAZYEGG_INTERNAL_IPS`` settings
    only works if you add this variable to the context yourself when you
    render the template, or you use the ``RequestContext`` and add the
    ``django.core.context_processors.request`` context processor to the
    ``TEMPLATE_CONTEXT_PROCESSORS`` setting::

        TEMPLATE_CONTEXT_PROCESSORS = [
            ...
            'django.core.context_processors.request',
            ...
        ]


User variables
--------------

Crazy Egg can segment clicks based on `user variables`_.  If you want to
set a user variable, use the ``set_uservar`` tag.  It takes two
arguments: the variable number (between 1 and 5) and the value (a
string).  The tag must come after the tracking code, and can be used
multiple times::

        ...
        {% track_crazyegg %}
        {% set_uservar 1 "some string" %}
        {% set_uservar 2 some_context_variable %}
    </body>
    </html>

.. _`user variables`: https://www.crazyegg.com/help/Setting_Up_A_Page_to_Track/How_do_I_set_the_values_of_User_Var_1_User_Var_2_etc_in_the_confetti_and_overlay_views/


Changelog
=========

2.1.1
    Stopped development.  Added Crazy Egg module to django_analytical_.

2.1.0
    Added the ``CRAZYEGG_INTERNAL_IPS`` setting.

2.0.0
    Added the ``set_uservar`` template tag to set Crazy Egg user
    variables.  These can be used to segment clicks on the confetti and
    layout views.

    Because variables can only be set after the tracking code has been
    loaded, the tracking template tag has been reverted to the code that
    Crazy Egg recommends and is no longer asynchronous.

1.0.1
    Fixed links to the Github project pages in the ``setup.py`` script.

1.0.0
    Project created from code used in the `IPv6 Ready`_ project.

.. _django-analytical: http://packages.python.org/django-analytical
.. _`IPv6 Ready`: http://www.ipv6ready.nl/

------------------------------------------------------------------------

django-crazyegg was written by Joost Cassee <joost@cassee.net>

Development was made possible by `Bateau Knowledge`_.  Thanks go to
Crazy Egg for their support.

.. _`Bateau Knowledge`: http://www.bateauknowledge.nl/

"""

__author__ = "Joost Cassee"
__email__ = "joost@cassee.net"
__version__ = "2.1.1"
__copyright__ = "Copyright (C) 2010-2011 Joost Cassee"
__license__ = "MIT License"
