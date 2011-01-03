"""
Template tag tests.
"""

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from django_crazyegg.templatetags.crazyegg import track_crazyegg
from django_crazyegg.tests.utils import TestSettingsManager

class TrackCrazyEggTagTestCase(TestCase):
    """
    Tests for the `track_pageview` template tag.
    """

    def setUp(self):
        self.settings_manager = TestSettingsManager()

    def tearDown(self):
        self.settings_manager.revert()

    def test_no_id(self):
        self.settings_manager.delete('CRAZYEGG_ACCOUNT_NUMBER')
        self.assertEqual("", track_crazyegg())

    def test_wrong_id(self):
        self.settings_manager.set(CRAZYEGG_ACCOUNT_NUMBER='wrong')
        self.assertRaises(ImproperlyConfigured, track_crazyegg)

    def test_rendering(self):
        self.settings_manager.set(CRAZYEGG_ACCOUNT_NUMBER='12345678')
        self.assertTrue('/1234/5678.js' in track_crazyegg())
