#!/usr/bin/env bash
# Render build script. Render runs this once per deploy.
set -o errexit

pip install -r requirements.txt

# Collect all static files into STATIC_ROOT so WhiteNoise can serve them.
python manage.py collectstatic --no-input

# Apply database migrations.
python manage.py migrate --no-input
