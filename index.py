from djAlphaRib.wsgi import app

import os
import sys
import pymysql  # import pymysql
from django.core.wsgi import get_wsgi_application

pymysql.install_as_MySQLdb()  # call this method before any Django import
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djAlphaRib.settings')
application = get_wsgi_application()
