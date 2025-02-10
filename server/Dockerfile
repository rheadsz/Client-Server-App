# Use Python 3.9 slim image as base to keep container size small
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy our server code into the container
COPY server.py .

# Tell Docker that our server will use this port
EXPOSE 65432

# Command to run when container starts
CMD ["python3", "server.py"]