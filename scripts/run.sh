#!/bin/bash
# run.sh


docker build -t python_env .
#docker run --rm -ti --name python_env python_env /bin/bash

docker build -t natural_git app/
docker run --rm -ti --name natural_git -p 5000:5000 natural_git

#docker-compose up -d
#curl 
#echo $(curl -s $(docker port ngrok_tunnel 4040)/api/tunnels | grep -P "http://.*?ngrok.io" -oh)
