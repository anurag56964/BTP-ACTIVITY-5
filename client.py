
# COMPLETED BY 
# /////////////////////////////////////////////
# ANURAG DAS
# STUDENT ID 126031228
# EMAIL- adas35@myseneca.ca
# /////////////////////////////////////////////


import socket
import random

def main():
    try:
        # CREATE SOCKET OBJECT
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"ERROR IN SOCKET CREATION: {e}")
        return
    host = '127.0.0.1'
    port = 27000
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(f"Failed to connect to server: {e}")
        client_socket.close()
        return

    print("SERVER CONNECTED!!!! . Type 'exit' to quit.")
    while True:
        message = input("Enter message to send or 'exit' to quit: ")
        if message == 'exit':
            break
        print(f"Sending: {message}")
        try:
            # SEND MSG TO SERVER
            client_socket.sendall(message.encode())
            # RCV RESPONS
            response = client_socket.recv(128).decode()
            print(f"RECIEVED : {response}")
        except socket.error as e:
            print(f"ERROR SENDING DATA : {e}")
            break

    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
