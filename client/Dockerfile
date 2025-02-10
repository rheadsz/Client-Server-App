# Use Python 3.9 slim image as base to keep container size small
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy our client code into the container
COPY client.py .

# Command to run when container starts
CMD ["python3", "client.py"]