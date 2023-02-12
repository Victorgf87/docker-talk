FROM victorgf87/docker-node-simple

# If not exposed, the port will not be accessible from outside the container
EXPOSE 8080 

CMD [ "node", "server.js" ] # This is the command that will be executed when the container is run. It is not executed when the image is built.

# docker build -t victorgf87/node-app . (Change the username)
# docker run victorgf87/node-app
# docker run --rm --name=node-app -p 8081:8080 victorgf87/node-app (In my computer, port 8080 is already in use for other service, so I need to change it to 8081)
# Open browser and go to http://localhost:8081
# docker ps. docker rm 
# docker stop container-id