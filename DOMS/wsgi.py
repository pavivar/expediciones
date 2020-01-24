"""
WSGI config for DOMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DOMS.settings")

# expediciones = get_wsgi_application()

# path a donde esta el manage.py de nuestro proyecto Django
sys.path.append('/home/pablo/my_env/expediciones/')

# referencia (en python) desde el path anterior al fichero settings.py
# Importante hacerlo así, si hay varias instancias coriendo (en lugar
# de setdefault)
os.environ['DJANGO_SETTINGS_MODULE'] = "expediciones.settings"
# os.environ.setdefault(“DJANGO_SETTINGS_MODULE”, “proyectodjango.settings”)

#  prevenimos UnicodeEncodeError
os.environ.setdefault("LANG", "en_US.UTF-8")
os.environ.setdefault("LC_ALL", "en_US.UTF-8")

# activamos nuestro virtualenv
activate_this = 'my_env/bin/activate.py'
#  execfile(activate_this, dict(__file__=activate_this))

# obtenemos la aplicación
application = get_wsgi_application()
