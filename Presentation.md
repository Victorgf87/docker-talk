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

------------------------------

In this workshop we are going to see how to go from the situation where you have your scripts and run them manually, to the point where you have an awesome collection of Docker images that contain your scripts and can run everywhere.

What is an image?
An image is a set of instructions that define what your container is going to have and execute. Images are built with layers, where each line is a layer. These layers are cached, so if you build your image again, it only has to build from the first change, using cached layers as a base. This makes Docker a very fast and efficient tool.
*Show fcm-python and 

*Show docker hub
This is Docker hub, a Docker Image repository where people can upload their images for anybody else to use them.


1st exercise:
- Download busybox
docker pull busybox
docker run -it --rm busybox
- Install python


How to create an image:
Docker images have a very reduced amount of instructions, which are very easy to learn.

How to run an image:



Volumes...



Todo before:
Create docker hub

