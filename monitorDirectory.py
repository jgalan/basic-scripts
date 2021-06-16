#!/usr/bin/python2
from urllib import request, parse
import json
import sys
import time
#### webhook to slack channel
webhook_url = "https://hooks.slack.com/services/A/SPECIFIC/CODE/FROM/SLACKAPPLICATION"

#### directory to be monitored
data_path = '/path/to/directory/to/be/monitored/'

import os
total_size = 0
for path, dirs, files in os.walk(data_path):
    for f in files:
        fp = os.path.join(path, f)
        total_size += os.path.getsize(fp)

print("Directory size: " + str(total_size))

directorySize = total_size

slack_data = [
        { 'type':'divider' },
        {'type':'section', 'text': {
                'type':'mrkdwn',
                'text':'A problem occured. Data directory is no longer registering data!'
                }
            },
        ]

#print('data to send:', json.dumps(slack_data))

while True:
    time.sleep(300)

    total_size = 0
    for path, dirs, files in os.walk(data_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)

    print("Directory size: " + str(total_size))

    if total_size > directorySize:
        directorySize = total_size
    else:
        print("Not registering data!")
        try:
            req = request.Request(
                    webhook_url,
                    data = json.dumps({'blocks':slack_data}).encode(),
                    headers={'Content-Type' : 'application/json'}
                    )
            resp = request.urlopen(req)
            print('Request to slack reported: %s' % resp.status)
            if resp.status != 200:
                raise ValueError('Request to slack reported error: %s' % resp.status)
            sys.exit()

        except Exception as e:
            print(e)

print('end script')
