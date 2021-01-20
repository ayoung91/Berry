#!/bin/bash

throttled="$(vcgencmd get_throttled)"
echo -e "$throttled"
if [[ "$throttled" != "throttled=0x0" ]]; then
    /usr/bin/python3 /home/pi/Projects/Berry/WebServer/crontab_shutdown.py
fi