#!/bin/sh

python manage.py migrate --no-input
echo "ENTRYPOINT: migrations complete"

python manage.py collectstatic --no-input
echo "ENTRYPOINT: collected static"

exec "$@"
