# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Expose port 7777
EXPOSE 7777

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make main.py executable
RUN chmod +x scanner.py

# Run the command when the container launches
ENTRYPOINT ["/usr/local/bin/python3", "/app/scanner.py"]