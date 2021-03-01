from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from mnist import MNIST

from math import sqrt
import numpy as np

import json
from PIL import Image



mndata = MNIST(r'train')
X_train, Y_train = mndata.load_training()

mndata = MNIST('test')
X_test, Y_test = mndata.load_testing()


def number_of_pixels(train : list, test : list) -> int:
    """
    This function calls the training images and test images and returns the square root of the number of pixels of each image.
    The postulate is that every images of the training set and the test set have the same number of pixels.
    It if is not the case between the training and testing sets, then an error is printed to warn the user.
    """
    
    try:
        if len(train[1]) == len(test[1]):
            nb_pixels = len(train[1])
            return int(sqrt(nb_pixels))
    except:
        print("The numbers of pixels of images in the train dataset and the test dataset are not the same, thus it is abnormal")

def get_numpy(Y_train : list, Y_test : list):
    """
    This function calls the training labels and test labels and converts those lists into arrays.
    This function returns the arrays corresponding to those lists.
    """
    return np.array(Y_train), np.array(Y_test)

def pipeline_classification():
    """
    This function executes the pipeline method of scikit-sklearn.
    See more information on https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
    """
    nb_pixels = number_of_pixels(X_train, X_test)
    pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())]) # initialisation of the method
    Y_train_r, Y_test_r = get_numpy(Y_train, Y_test)
    pipe.fit(X_train, Y_train_r)                                    # fitting the pipline to the training images and labels
    return pipe, pipe.score(X_test, Y_test_r)                       # score obtained by applying the pipeline to the test images and labels

def data_fit(data):
    """
    This function calls an array of an image and converts it to a list fitting the MNIST model.
    If the array contains 4 values (RGB + Greyscale) for each pixel, the function returns only the list of the Greyscale part of the image.
    Else, it returns the list of the average of the three values (RGB) for each pixel.
    """
    nb_pixels = number_of_pixels(X_train, X_test)
    if len(data[0][0]) == 4:
        return [data[i][j][3] for j in range(nb_pixels) for i in range(nb_pixels)]
    else:
        data_final = []
        for i in range(nb_pixels):
            for j in range(nb_pixels):
                x = 0
                for k in range(3):
                    x += data[i][j][k]
                    data_final.append(x/3)
        return data_final

def invert_image(data):
    """
    This function calls an array of an image and returns the the inverted values of pixels.
    For instance, 0 -> 255 and 185 -> 70
    """
    data_reverse = []
    for x in data:
        data_reverse.append(abs(x - 255))
    return data_reverse

def get_classification(path, pipe):
    """
    This function calls the path of an image, open it thanks to the library PIL and the method Image.
    Then the function converts the image to a numpy array.
    Finally the function predicts the classification of the image thanks to the pipeline method
    """
    nb_pixels = number_of_pixels(X_train, X_test)
    image = Image.open(path).resize((nb_pixels, nb_pixels)) # resize the image in order to fit the MNIST sets
    data = np.asarray(image)                             # convert the image to an array containing the pixels of the image
    data_fixed = data_fit(data)
    data_final = invert_image(data_fixed)                    # images are very often inverted in terms of values in comparison to MNIST images so don't forget to check
    return pipe.predict(np.array(data_final).reshape(1, -1))

def res_to_json(path):
    """
    This function calls the path of an image and returns the prediction of its classification in a JSON file containing
    its path, its classification and the accuracy of the method used.
    """
    pipe, accuracy = pipeline_classification()
    res = get_classification(path, pipe)[0]
    
    json_d = {
        "image": f'{path}',
        "prediction": f'{res}',
        "accuracy": f'{accuracy}'
    }
    return json.dumps(dictionnary, indent = 3, sort_keys = True)

#print(res_to_json(r"8.jpg"))
print(number_of_pixels(X_train, X_test))
