#!/bin/zsh

icon_enabled=""
icon_disabled="b"
status=`systemctl is-active bluetooth.service`

if [ $status == "active" ]
then
    echo "$icon_enabled"
else
    echo "$icon_disabled"
fi
