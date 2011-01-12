"""
Template tag tests.
"""

from django.test import TestCase

from django_crazyegg.templatetags.crazyegg import track_crazyegg, \
        set_uservar, CrazyEggException
from django_crazyegg.tests.utils import TestSettingsManager


class TrackCrazyEggTagTestCase(TestCase):
    """
    Tests for the `track_crazyegg` template tag.
    """

    def setUp(self):
        self.settings_manager = TestSettingsManager()

    def tearDown(self):
        self.settings_manager.revert()

    def test_no_id(self):
        self.settings_manager.delete('CRAZYEGG_ACCOUNT_NUMBER')
        self.assertRaises(CrazyEggException, track_crazyegg)

    def test_wrong_id(self):
        self.settings_manager.set(CRAZYEGG_ACCOUNT_NUMBER='1234567')
        self.assertRaises(CrazyEggException, track_crazyegg)
        self.settings_manager.set(CRAZYEGG_ACCOUNT_NUMBER='123456789')
        self.assertRaises(CrazyEggException, track_crazyegg)

    def test_rendering(self):
        self.settings_manager.set(CRAZYEGG_ACCOUNT_NUMBER='12345678')
        r = track_crazyegg()
        self.assertTrue('/1234/5678.js' in r, r)


class SetUserVarTagTestCase(TestCase):
    """
    Tests for the `set_uservar` template tag.
    """

    def test_normal(self):
        r = set_uservar(2, 'test')
        self.assertTrue("CE2.set(2,'test');" in r, r)

    def test_string_int_var(self):
        r = set_uservar('2', 'test')
        self.assertTrue("CE2.set(2,'test');" in r, r)

    def test_not_int_var(self):
        self.assertRaises(CrazyEggException, set_uservar, 't', 'test')

    def test_low_var(self):
        r = set_uservar(1, 'test')
        self.assertTrue("CE2.set(1,'test');" in r, r)
        self.assertRaises(CrazyEggException, set_uservar, 0, 'test')

    def test_high_var(self):
        r = set_uservar(5, 'test')
        self.assertTrue("CE2.set(5,'test');" in r, r)
        self.assertRaises(CrazyEggException, set_uservar, 6, 'test')

    def test_long_value(self):
        s1 = "X" * 100
        s2 = "X" * 101
        r = set_uservar(3, s1)
        self.assertTrue("CE2.set(3,'%s');" % s1 in r, r)
        self.assertRaises(CrazyEggException, set_uservar, 3, s2)

    def test_escaped_quote(self):
        s = "test'test"
        e = "test\\'test"
        r = set_uservar(4, s)
        self.assertTrue("CE2.set(4,'%s');" % e in r, r)
