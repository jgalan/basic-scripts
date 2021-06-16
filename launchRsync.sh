#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern. 

if pgrep -x "rsync" > /dev/null
then
	echo "rsync is running. I do nothing"
	rsyncCmdOut=`ps -A | grep rsync`
	hour=`echo $rsyncCmdOut | cut -d ':' -f 2`
	var='02'
	if [ "$hour" = "$var" ]; then
		echo "rsync was already running for 2 hours!"
		echo "Killing the process!"
		pkill rsync
	fi
else
	echo "Launching copy to REMOTE system"
	rsync -ai -e "ssh -i /home/USER/.ssh/id_rsa" /path/to/loca/data/ --exclude="lost+found" USER@REMOTE:/path/at/remote/data/
fi
