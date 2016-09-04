import os
import subprocess

name = "timecard"


current_hash = ""
if os.path.isfile('hash'):
    current_hash = open('hash').readlines()[0]
new_hash = os.popen('git rev-parse HEAD').readlines()[0]
open('hash','w').write(new_hash)
    
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
