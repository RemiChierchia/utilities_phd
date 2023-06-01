# Utils

When using nerfstudio local server viewer, need to kill the process

`sudo lsof -iTCP:7007 -sTCP:LISTEN` to get the PID and then `kill <PID>`
