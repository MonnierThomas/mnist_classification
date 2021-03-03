# Use an official Python TensorFlow runtime as a base image
FROM tensorflow/tensorflow:2.2.0

# Set the working directory to /docker_image_classification
WORKDIR /docker-image_classification

# Copy the current directory contents into the container
COPY app.py ./
COPY requirements.txt ./
COPY 8.jpg ./

# Install any needed packages specified in requirements.txt
RUN python -m pip install -r requirements.txt 

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
