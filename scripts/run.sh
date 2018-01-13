#!/bin/bash
# run.sh

docker-compose up -d
#curl 
#echo $(curl -s $(docker port ngrok_tunnel 4040)/api/tunnels | grep -P "http://.*?ngrok.io" -oh)