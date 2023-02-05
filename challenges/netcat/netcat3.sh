#!/bin/bash
PORT=48001
SCRIPT=/opt/netcat/flag3.sh

if pgrep -f "nc -l -p $PORT -e $SCRIPT" > /dev/null ; then
		:
else
	while true ; do
		nc -l -p $PORT -e $SCRIPT 
		sleep 1
	done
fi
