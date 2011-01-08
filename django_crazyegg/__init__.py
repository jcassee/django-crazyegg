"""
Crazy Egg integration for Django
================================

The django-crazyegg application integrate `Crazy Egg`_ heatmaps into a
Django_ project.

.. _`Crazy Egg`: http://www.crazyegg.com/
.. _Django: http://www.djangoproject.com/


Overview
--------

Crazy Egg is an easy to use hosted web application that generates
heatmaps from webpage visitor clicks.  It allows you to discover the
areas of web pages that are most important to your visitors.  This
Django application provides template tags that make integration of
Crazy Egg very simple.


Installation and configuration
------------------------------

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
-----

In your template, load the django-crazyegg template tags by adding
``{% load crazyegg %}`` at the top of the template.  Then use the
``track_crazyegg`` tag to insert the Javascript tracking code.  The
Crazy Egg web pages recommend adding the code directly before the
closing ``</body>`` HTML tag::

        ...
        {% track_crazyegg %}
    </body>
    </html>

*Note:* Versions of django-crazyegg prior to 2.0.0 used asynchronous loading to
allow the tag to be added to the HTML head section.  Unfortunately, that
caused problems if you wanted to set user variables (see below).

Even if you only track clicks on a specific page, you can still insert
the tracking tag in your base template.  Crazy Egg will only install the
Javascript event handler on URLs that you have created snapshots for.

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


------------------------------------------------------------------------

django-crazyegg was written by Joost Cassee <joost@cassee.net>

Development was made possible by `Bateau Knowledge`_.  Thanks go to
Crazy Egg for their support.

.. _`Bateau Knowledge`: http://www.bateauknowledge.nl/

"""

__author__ = "Joost Cassee"
__email__ = "joost@cassee.net"
__version__ = "2.0.0alpha"
__copyright__ = "Copyright (C) 2010 Joost Cassee"
__license__ = "MIT License"
