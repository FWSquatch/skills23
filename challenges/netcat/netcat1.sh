#!/bin/bash
PORT=5656
SCRIPT=/opt/netcat/flag1.sh

if pgrep -f "nc -l -p $PORT -e $SCRIPT" > /dev/null ; then
	:
else
	while true ; do
		nc -l -p $PORT -e $SCRIPT
		sleep 1
	done
fi
