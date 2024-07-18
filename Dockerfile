# Use an official Python runtime as a parent image 
FROM python:3.12.4
RUN pip install --upgrade pip
 
# Set the working directory in the container 
WORKDIR /app 
 
# Copy the current directory contents into the container at /app 
COPY . /app 

# Define environment variables for file paths
ENV TRAIN_PATH="/Users/hmd/hmd_project/git-python/Data/ML_basic/train.csv"
ENV TEST_PATH="/Users/hmd/hmd_project/git-python/Data/ML_basic/test.csv"
ENV OUTPUT_PATH="/app/images"

# Create directory for output images
RUN mkdir -p $OUTPUT_PATH
 
# Install any needed packages specified in requirements.txt 
# (You can remove this if your Python script doesn't have dependencies) 
RUN pip install --no-cache-dir -r requirements.txt 

# Make port 4000 available to the world outside this container 
EXPOSE 4000:4000
#docker build -t image_name .
#docker run -p 4000:4000 image_name

# Define environment variable 
ENV NAME basic_ml
 
# Run app.py when the container launches 
CMD ["python", "app.py"] 