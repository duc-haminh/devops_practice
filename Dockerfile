# Use an official Python runtime as a parent image
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a directory for data files and copy them
RUN mkdir -p /app/Data/ML_basic
COPY /Data/ML_basic/train.csv /app/Data/ML_basic/train.csv
COPY /Data/ML_basic/test.csv /app/Data/ML_basic/test.csv


# Define environment variables for file paths
ENV TRAIN_PATH="/app/Data/ML_basic/train.csv"
ENV TEST_PATH="/app/Data/ML_basic/test.csv"
ENV OUTPUT_PATH="/app/images"

# Create directory for output images
RUN mkdir -p $OUTPUT_PATH

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run app.py when the container launches
#CMD ["python", "app.py"]"""

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]