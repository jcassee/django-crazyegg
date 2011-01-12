from distutils.core import setup, Command

import django_crazyegg


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os
        os.environ['DJANGO_SETTINGS_MODULE'] = 'django_crazyegg.tests.settings'
        from django_crazyegg.tests.utils import run_tests
        run_tests()


setup(
    name = 'django-crazyegg',
    version = django_crazyegg.__version__,
    license = django_crazyegg.__license__,
    description = 'Crazy Egg heatmaps for Django projects',
    long_description = django_crazyegg.__doc__,
    author = django_crazyegg.__author__,
    author_email = django_crazyegg.__email__,
    packages = [
        'django_crazyegg',
        'django_crazyegg.templatetags',
        'django_crazyegg.tests',
    ],
    keywords = ['django', 'heatmap', 'crazy egg'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = 'http://github.com/jcassee/django-crazyegg',
    download_url = 'http://github.com/jcassee/django-crazyegg/archives/master',
    cmdclass = {'test': TestCommand},
)
