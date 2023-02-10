#!/bin/bash
python script.py
echo $(date) >> /app/dates.dat
exec "$@"
