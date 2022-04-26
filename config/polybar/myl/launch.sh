#!/bin/zsh

# Terminate already running bar instances
DIR="$HOME/.config/polybar/myl"
killall -q polybar
# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done
polybar -rq wm -c "$DIR"/config.ini &
polybar -rq time -c "$DIR"/config.ini &
polybar -rq tray -c "$DIR"/config.ini &
echo "Polybar launched..."
