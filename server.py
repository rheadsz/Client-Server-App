# server side of the code
# Submitted by Rhea Benedicta Dsouza

import socket
import time
import threading
from tkinter import Tk, Text, Scrollbar, Frame, Label, Button, END

def start_server(host='127.0.0.1', port=65432):
    def handle_client(client_socket, client_address, client_number):
        with client_socket:
            try:
                # Receive data from the client
                data = client_socket.recv(1024).decode('utf-8')
                log_message(f"Received from client {client_number}: {data}")

                # Add the current time to the message
                response = f"{data} | Received at: {time.ctime()}"

                # Send the modified message back to the client
                client_socket.sendall(response.encode('utf-8'))
                log_message(f"Sent response to client {client_number}: {response}")
            except Exception as e:
                log_message(f"Error handling client {client_number}: {e}")

    def log_message(message):
        # Display messages in the GUI log
        log_area.config(state='normal')
        log_area.insert(END, message + "\n")
        log_area.config(state='disabled')
        log_area.yview(END)

    def start():
        # Start the server in a new thread
        threading.Thread(target=run_server, daemon=True).start()

    def run_server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(5)
            log_message(f"Server started on {host}:{port}. Waiting for connections...")
            client_number = 1
            while True:
                client_socket, client_address = server_socket.accept()
                log_message(f"Connected to client {client_number} at {client_address}")
                threading.Thread(target=handle_client, args=(client_socket, client_address, client_number), daemon=True).start()
                client_number += 1

    # Create the GUI
    root = Tk()
    root.title("Server GUI")

    # Log area
    log_area = Text(root, state='disabled', wrap='word', height=20, width=60)
    log_area.grid(row=0, column=0, padx=10, pady=10)

    # Scrollbar
    scrollbar = Scrollbar(root, command=log_area.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    log_area.config(yscrollcommand=scrollbar.set)

    # Start button
    start_button = Button(root, text="Start Server", command=start)
    start_button.grid(row=1, column=0, pady=10)

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    # Initialize the GUI
    start_server()