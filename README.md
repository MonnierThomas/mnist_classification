# docker-image_classification
This GitHub repository aims to classify images thanks to a pipeline algorithm trained and tested on the MNIST dataset of Yann LeCun. Hence, this very simple Docker app can classify images and return a JSON file containing the result. 

## Docker

### What is Docker ?
"Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production." [1]

Docker is used in many firms and brands because it makes virtualization very easy to manipulate. Instead of installing a virtual machine on your computer - which needs lots of RAM permanently -, you only need to install Docker lcoally. It is called **lightweight virtualization**. Now you can work locally and share your files to others, even if they don't have the same environment : MacOs, Linux, Windows ... Life gets to be easier than ever !

[1] : https://docs.docker.com/get-started/overview/

### How to install Docker ?

You need to follow some operations in order to make Docker functional on your laptop. Please check this website to install Docker Engine on Ubuntu (approx. 10 minutes) : https://docs.docker.com/engine/install/ubuntu/

If you work in a Windows environment, then you will have to meet the following prerequisites : you need one of the Windows version among Windows Professional, Windows Education and Windows Enterprise. Then you can get Docker Desktop on Windows : https://docs.docker.com/docker-for-windows/install/

If your work in a MacOs environment, please check the prerequisites and install Docker Desktop for Mac : https://docs.docker.com/docker-for-mac/install/
