"""
Crazy Egg integration for Django
================================

The django-crazyegg application integrates `Crazy Egg`_ heatmaps into a
Django_ project.

.. _`Crazy Egg`: http://www.crazyegg.com/
.. _Django: http://www.djangoproject.com/


Overview
--------

Crazy Egg is an easy to use hosted web application that generates
heatmaps from webpage visitor clicks.  It allows you to discover the
areas of web pages that are most important to your visitors.  This
Django application provides a template tag that make integration of
Crazy Egg very simple.


Installation and configuration
------------------------------

To install django-crazyegg, simply place the ``django_crazyegg``
package somewhere on the Python path.  The application is configured in
the project ``settings.py`` file.  In order to use the template tag, the
``django_crazyegg`` package must be present in the ``INSTALLED_APPS``
list::

    INSTALLED_APPS = [
        ...
        'django_crazyegg',
        ...
    ]

You set your Crazy Egg account number in the ``CRAZYEGG_ACCOUNT_NUMBER``
setting::

    CRAZYEGG_ACCOUNT_NUMBER = '12345678'

That's it!


Usage
-----

In your template, load the django-crazyegg template tag by adding
``{% load crazyegg %}`` at the top of the template.  Then use the
``track_crazyegg`` tag to insert the Javascript code.  The Crazy Egg
web pages recommend adding the code directly before the closing
``</body>`` HTML tag, but the code added by this tag is designed not to
hold up loading the page.  You can safely add it to the head of the HTML
document::

    <head>
        ...
        {% track_crazyegg %}
        ...
    </head>

Even if you only track clicks on a specific page, you can still insert
the tag in your base template.  Crazy Egg will only install the
Javascript event handler on a URL that you have created a snapshot for.


------------------------------------------------------------------------

django-crazyegg was written by Joost Cassee <joost@cassee.net>

Development was made possible by `Bateau Knowledge`_.  Thanks go to
Crazy Egg for their support.

.. _`Bateau Knowledge`: http://www.bateauknowledge.nl/

"""

__author__ = "Joost Cassee"
__email__ = "joost@cassee.net"
__version__ = "1.0.1"
__copyright__ = "Copyright (C) 2010 Joost Cassee"
__license__ = "MIT License"
