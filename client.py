# client.py
# Author: [Your Name]

import socket
import tkinter as tk
from tkinter import ttk, messagebox

def start_client(host='127.0.0.1', port=65432):
    def send_message():
        try:
            # Get the client number and message from the input fields
            client_number = client_number_entry.get()
            message = message_entry.get()

            if not client_number or not message:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            # Create a socket and connect to the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((host, port))
                full_message = f"Client {client_number}: {message}"
                client_socket.sendall(full_message.encode('utf-8'))

                # Receive the response from the server
                response = client_socket.recv(1024).decode('utf-8')
                messagebox.showinfo("Response from Server", response)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    # Create the GUI
    root = tk.Tk()
    root.title("Client GUI")

    # Client number label and entry
    client_number_label = ttk.Label(root, text="Client Number:")
    client_number_label.grid(row=0, column=0, padx=10, pady=10)
    client_number_entry = ttk.Entry(root)
    client_number_entry.grid(row=0, column=1, padx=10, pady=10)

    # Message label and entry
    message_label = ttk.Label(root, text="Message:")
    message_label.grid(row=1, column=0, padx=10, pady=10)
    message_entry = ttk.Entry(root)
    message_entry.grid(row=1, column=1, padx=10, pady=10)

    # Send button
    send_button = ttk.Button(root, text="Send", command=send_message)
    send_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    start_client()