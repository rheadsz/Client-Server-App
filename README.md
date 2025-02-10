## Client-Server-App

## Environment and Programming Language
This project is implemented in Python and uses Docker for containerization. The application consists of a client and server, both running in separate Docker containers.

## Docker Containers and Dockerfiles
Client Container: Built using the "client/Dockerfile". It installs the necessary Python dependencies and runs the "client.py" script.
Server Container: Built using the "server/Dockerfile". It installs the necessary Python dependencies, exposes port 65432, and runs the "server.py" script.

## Running the Containers
To run the application, use Docker Compose. The "docker-compose.yml" file orchestrates the client and server containers.

### Steps to Build and Run
1. Ensure Docker is installed on your system.
2. Navigate to the project directory.
3. Run "docker-compose up --build" to build and start the containers.
4. The server will be accessible on port 65432.

## Results
Upon running the containers, the server will listen for client connections, and the client can send messages to the server. The server responds with a timestamped message.



## References
- [Docker Documentation](https://docs.docker.com/get-started/)
- [Cloud Skills Boost](https://www.cloudskillsboost.google/focuses/1029?parent=catalog)