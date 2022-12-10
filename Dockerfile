# Use the official Python image as the base image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the source code to the working directory
COPY . .

# Compile the Python code using the Makefile
RUN make

# Run the executable when the container starts
CMD ["./system-hardware-info"]
