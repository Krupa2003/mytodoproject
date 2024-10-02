# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the application files
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Run the Python app
CMD ["python", "app.py"]

