import os
import subprocess

name = "timecard"

current_hash = os.popen('git rev-parse HEAD').readlines()[0]
# Update to the latest version
for line in os.popen('go get -u github.com/brotherlogic/' + name).readlines():
    print line.strip()
new_hash = os.popen('git rev-parse HEAD').readlines()[0]

    
# Move the old version over
for line in os.popen('cp ' + name + ' old' + name).readlines():
    print line.strip()

# Rebuild
for line in os.popen('go build ./...').readlines():
    print line.strip()

# Rebuild
for line in os.popen('go build').readlines():
    print line.strip()

running = len(os.popen('ps -ef | grep ' + name).readlines()) > 3

              
if not running:
    subprocess.Popen(['./' + name])
