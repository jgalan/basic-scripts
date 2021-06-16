Basic scripts that might be handy or used as reference to create other scripts.

* **monitorDirectory.py**: It will check if a given path contents are increasing every a given period of time. If it doesnt, it will create a slack message and send a warning to a slack channel. Two variables need to be locally modified `data_path` and `webhook_url` in order to adapt for a particular directory supervision, and connect to a particular slack application.

* **launchRsync.sh**: A simple script to syncronize a remote path with the local path. It includes some protection to avoid multiple `rsync` instances. In case `rsync` gets stuck, it will kill the process so that it is relaunched again by a cronjob. The cronjob definition will be something like `1,6,11,16,21,26,31,36,41,46,51,56 * * * * /home/usertrex/scripts/launchRsync.sh` to atempt a copy every 5 minutes.
