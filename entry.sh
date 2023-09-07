#!/bin/sh

# Enter to project working directory
echo "Enter to project working directory......"

# Verify healthy before applying migrations
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"
