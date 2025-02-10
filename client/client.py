# client.py
# Author: Rhea Benedicta Dsouza
# Description: Client program that connects to a server using Docker containers.
#             Sends test messages and receives timestamped responses.

import socket
import time

def send_message(client_num, message, host='server', port=65432):
    """
    Send a message to the server and receive its response.
    
    Args:
        client_num: An identifier for this client
        message: The message to send
        host: Server hostname (default: 'server' - Docker service name)
        port: Server port number (default: 65432)
    
    Returns:
        Server's response or None if an error occurred
    """
    try:
        # Create a TCP socket and connect to our server container
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"Connecting to {host}:{port}...")
            client_socket.connect((host, port))
            
            # Add client number to message and send it
            full_message = f"Client {client_num}: {message}"
            client_socket.sendall(full_message.encode('utf-8'))
            print(f"Sent message: {full_message}")

            # Wait for and print server's response
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received response: {response}")
            return response
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # List of test messages to send to server
    # Each tuple contains (client_number, message)
    test_messages = [
        (1, "Hello from container!"),
        (2, "Testing connection"),
        (3, "Final test message")
    ]
    
    # Send each test message with a delay between them
    # This makes it easier to see what's happening
    for client_num, message in test_messages:
        print("\n-------------------")
        send_message(client_num, message)
        time.sleep(2)  # 2 second delay between messages

if __name__ == "__main__":
    print("Starting client...")
    main()
