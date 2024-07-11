# Use an official Python runtime as a parent image 
FROM python:3.12.4
RUN pip install --upgrade pip
 
# Set the working directory in the container 
WORKDIR /app 
 
# Copy the current directory contents into the container at /app 
COPY . /app 
 
# Install any needed packages specified in requirements.txt 
# (You can remove this if your Python script doesn't have dependencies) 
RUN pip install --no-cache-dir -r requirements.txt 

# Make port 80 available to the world outside this container 
EXPOSE 4000:4000 
 
# Define environment variable 
#ENV NAME Youtube_scrape_text
 
# Run app.py when the container launches 
CMD ["python", "app.py"] 