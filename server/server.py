'''server.py
Author: Rhea Benedicta Dsouza
This is the Server program that runs in a Docker container and handles client connections. Receives messages, adds timestamps,
and sends them back to clients.'''

import socket
import time
import threading

def handle_client(client_socket, client_address, client_number):
    """
    Handle an individual client connection.
    Receives a message, adds a timestamp, and sends it back.
    
    Arguments:
        client_socket: Socket for this client connection
        client_address: Client's address information
        client_number: Unique identifier for this client
    """
    with client_socket:  # Socket will automatically close when done
        try:
            # Get the message from client and decode it
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received from client {client_number}: {data}")

            # Create response by adding current timestamp
            response = f"{data} | Received at: {time.ctime()}"

            # Send timestamped message back to client
            client_socket.sendall(response.encode('utf-8'))
            print(f"Sent response to client {client_number}: {response}")
        except Exception as e:
            print(f"Error handling client {client_number}: {e}")

def run_server(host='0.0.0.0', port=65432):
    """
    Start the server and listen for client connections.
    
    Args:
        host: IP to listen on (0.0.0.0 means all available interfaces)
        port: Port number to listen on (default: 65432)
    """
    # Create a TCP socket for the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind to the specified host and port
        server_socket.bind((host, port))
        # Listen for up to 5 queued connections
        server_socket.listen(5)
        print(f"Server started on {host}:{port}. Waiting for connections...")
        
        client_number = 1  # To identify different clients
        
        # Main server loop - keep accepting new connections
        while True:
            try:
                # Wait for a client to connect
                client_socket, client_address = server_socket.accept()
                print(f"Connected to client {client_number} at {client_address}")
                
                # Create a new thread for this client
                # This allows handling multiple clients simultaneously
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(client_socket, client_address, client_number),
                    daemon=True  # Thread will close when main program exits
                )
                client_thread.start()
                client_number += 1
            except Exception as e:
                print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    print("Starting server...")
    run_server()