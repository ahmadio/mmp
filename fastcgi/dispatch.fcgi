#!/usr/bin/env python
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/envo")
sys.path.insert(0, "/envo/demo")

# Switch to the directory of your project. (Optional.)
# os.chdir("/home/userid/djangoproject")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "demo.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(daemonize="false")
