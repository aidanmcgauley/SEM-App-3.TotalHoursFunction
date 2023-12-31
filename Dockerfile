# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the local src directory contents into the container at /app
COPY src/ /app

# Install Flask and flask-cors
RUN pip install Flask flask-cors

# Make port available to the world outside this container
EXPOSE 8001

# Define environment variable to tell Flask where to find the app
ENV FLASK_APP=index.py

# Run Flask app when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=8001"]