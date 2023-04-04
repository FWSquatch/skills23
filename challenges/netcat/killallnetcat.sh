#!/bin/bash

kill -9 $(ps aux | grep "/opt/netcat/netcat1.sh" | grep -v "grep" | awk '{ print $2}') 2>&1 > /dev/null
kill -9 $(ps aux | grep "/opt/netcat/netcat2.sh" | grep -v "grep" | awk '{ print $2}') 2>&1 > /dev/null
kill -9 $(ps aux | grep "/opt/netcat/netcat3.sh" | grep -v "grep" | awk '{ print $2}') 2>&1 > /dev/null
/usr/bin/pkill nc 2>&1 > /dev/null
