import os

__revision__ = "$Id: debug.py 2552 2013-03-05 21:44:40Z febret@gmail.com $"

# If DISTUTILS_DEBUG is anything other than the empty string, we run in
# debug mode.
DEBUG = os.environ.get('DISTUTILS_DEBUG')
