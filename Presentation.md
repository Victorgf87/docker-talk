Docker
What is Docker?
Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.

What is a Container?
https://www.docker.com/wp-content/uploads/2021/11/docker-containerized-appliction-blue-border_2.png


"A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings."
To be put in another way, an image is a definition, and a container is like a virtual Machine that contains a Operating System with dependencies encapsulated, and it can be used to run processes in a platform agnostic way.

Why use Docker?
Consistent and Isolated Environment. You can have each image with only the dependencies 


.....Docker containers make it easy to put new versions of software, with new business features, into production quickly and to quickly roll back to a previous version if you need to. They also make it easier to implement strategies like blue/green deployments (when you deliver new features to a subset of users, and it makes it easier to test)

------------------------------ Begin
# A: 10 mins
In this workshop we are going to see how to go from the situation where you have your scripts and run them manually, to the point where you have an awesome collection of Docker images that contain your scripts and can run anywhere.

What is Docker?
https://www.docker.com/
Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.

What is a Container?
https://www.docker.com/wp-content/uploads/2021/11/docker-containerized-appliction-blue-border_2.png
Docker containers make it easy to put new versions of software, with new business features, into production quickly and to quickly roll back to a previous version if you need to. They also make it easier to implement strategies like blue/green deployments (when you deliver new features to a subset of users, and it makes it easier to test)

What is an image?
An image is a set of instructions that define what your container is going to have and execute. Images are built with layers, where each line is a layer. These layers are cached, so if you build your image again, it only has to build from the first change, using cached layers as a base. This makes Docker a very fast and efficient tool. They are built using Dockerfiles.
*Show fcm-python and 

### B: 10 mins.
*Show docker hub
This is Docker hub, a Docker Image repository where people can upload their images for anybody else to use them.
Show https://hub.docker.com/_/ubuntu Mention that only companies like this are allowed to have images without their username. 
Mention Tags
Open tags, and open an image.
Is there any other image you want to see?
https://hub.docker.com/_/python
https://hub.docker.com/_/ruby
https://hub.docker.com/_/node
https://hub.docker.com/u/victorgf87
### B

Create a folder anywhere, we will use it as the root of our exercises.
1st exercise:
- Create a folder and enter it
- Download busybox
docker pull busybox
docker run -it --rm busybox
- Create a file with some content
echo "hola hola" > hola.txt
- exit the image
- open the image
- see, the file is not there. This is because containers are ephimeral, which means they don't preserve anything. But we can do something to do that
Meet the volumes.
Volumes are spaces in your hard drive that are used for persistance between container instances. They have their own place in your Docker installation, but for simplicity sake, we are going to define them in our folder. Anyway, none of those two ways is better than the other. 

- Go to your exercises root and create a folder called volumes, and then a folder called one, with a file inside called host.txt(or anything). Go to the root in case you moved.
- docker run --rm -it -v ${PWD}/volumes/one:/files busybox (In this command, rm option removes the container after it finishes, it means interactive, and v is for volume)
- Create a file with some content.
- echo "hola hola" > /files/hola.txt
- Now look at your files in your computer, hola.txt is there.

***Questions***

Now that you understand the concepts, let's get to something less manual.
Dockerfile.
Dockerfile is a file where you define instructions that will make your image.
The basic structure is like this:
1: Base image, that we use as the base to build.
2: Installations, downloads, configurations.
3: Execution.

Let's create a simple docker image that will contain a simple Node app.
- Go to root folder
- Create a folder called node-app, with a Dockerfile inside
* Open node-app folder
* Open Dockerfile


### Encapsulate a python script
Show starwars-api-people

### Ultimate purpose: developing a Python script using containers and volumes, using host computer visual studio

### Extensions to make your life easier: Visual Studio Code Node extensions



#### Extra: Docker compose
Docker compose is a tool that is intended to run multicontainer applications, making it easy to deploy and create an application with several services that can interact with each other.
But one of the biggest reasons I like it is because it makes easy to do what we have already done by describing a yaml file and not having to remember every command and parameter you need for running your stuff. You can define the ports, the volumes, the container names, the image names, volumes info, etc.
Let's use compose for node-app


----------------------------------------------------- END
How to create an image:
Docker images have a very reduced amount of instructions, which are very easy to learn.

How to run an image:



Volumes...



Todo before:
Create docker hub

