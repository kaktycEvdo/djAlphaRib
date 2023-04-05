from djAlphaRib.wsgi import app

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djAlphaRib.settings')
application = get_wsgi_application()
