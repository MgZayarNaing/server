# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

path = '/home/aungaung321/django_blog'
if path not in sys.path:
  sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_blog.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
