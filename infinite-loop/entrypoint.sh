#!/bin/bash
python script.py

while :
do
  echo "Iteration"
	echo $(date) >> /app/dates.dat
	sleep 1
done

exec "$@"
