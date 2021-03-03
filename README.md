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

## Pipeline Classification of a MNIST dataset

In order to use this very simple app, you need to meet the following steps :

### 1) Install Docker
Please check the previous paragraph.

### 2) (Optional) Download the MNIST dataset from Yann LeCun
You will have to download the MNIST dataset [2]. This dataset contains four files.
- train-images-idx3-ubyte.gz is the training set of images (60,000 images)
- train-labels-idx1-ubyte.gz is the training set of labels (labels of the training set)
- t10k-images-idx3-ubyte.gz is the test set of images (10,000 images)
- t10k-labels-idx1-ubyte.gz is the test of labels (labels of the test set)

Since these sets are compressed, you have to unzip the files. Check if your zipper hasn't renamed the files with **..** instead of **-**. You need :
- train-images-idx3-ubyte
- train-labels-idx1-ubyte
- t10k-images-idx3-ubyte
- t10k-labels-idx1-ubyte

Create a new folder *train* with the training sets of images and labels and another one *test* with the test sets of images and labels.

Now you are able to use the training and test sets of MNIST images. You can modify them and print them with libraries such as matplotlib. However, we prefer using directly the method mnist from keras.datasets which can be installed by downloading the right versions of TensorFlow and keras. Hence, is is mandatory to download the MNIST datasets.

[2] : http://yann.lecun.com/exdb/mnist/

### 3) Clone this GitHub repository
Follow the instructions on GitHub to clone this repository. 

Optional : Put the *train* and *test* folders in it if you want to use them. [3]

[3] : The *train* and *set* folders have not been add to the GitHub repository because of the weigth of the files.

### 4) Open a new terminal 
Go to the directory where you have cloned to GitHub repository.
And just execute these commands :

- **docker build -t your-docker-image .** Do not forget the point at the end and precise the name of your docker image at your-docker-image.
- **docker images** to check if the image has been correctly created
- **docker run your-docker-image** to run the python file and to print the output in the terminal. Because we gave the python algorithm the test image 8.jpg (an image of a 8), you should see printed : 
- \begin{center} {zizi \end{center}

   "accuracy": "0.966",
   
   "image": "8.jpg",
   
   "prediction": "8"
   
}  \end{center}

  

### 5) Use your own images and get the JSON file
Download your image of a handwritten number in the folder containing all the files and get the result !

You can modify the image to be predicted directly by clicking on app.py. There is no problem if you do not have Python installed on your device. Just open it with text and replaced the last code line by **image.jpg** who must have been downloaded following these instructions :
- download the image in the folder containing the GitHub repository
- name it image.jpg
- if the image is not in the jpg format, you must convert it to jpg before using the Docker app

You can test this Docker app on the three images available in the repository. Don't forget to understand the code (there are few minors details to fix when passing from .jpg to .png).

### To know more ...
Fore more information about the code, open the explanation_code.ipynb on Jupyter Notebook (Anaconda) or Visual Studio Code (Python extension) to understand better the writing of the code.

### Special Thanks
Yann LeCun

Georges Ryssen, CEO, DeepMove
