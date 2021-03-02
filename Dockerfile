# Use an official Python runtime as a base image
FROM python:3

# Set the working directory to /docker_image_classification
WORKDIR /docker-image_classification

# Copy the current directory contents into the container at /app
# ADD . /docker-image_classification

# Install any needed packages specified in requirements.txt
RUN python -m pip install -r requirements.txt 

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["app.py"]

ENTRYPOINT ["python3"]
