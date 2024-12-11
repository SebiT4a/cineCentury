#!/bin/bash
# Comando para iniciar la aplicación Django usando Gunicorn
exec gunicorn --bind 0.0.0.0:8000 Cinema.wsgi:application
