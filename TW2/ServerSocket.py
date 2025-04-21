import socket
import os

def start_server():
    host = "127.0.0.1"
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Server is listening")

    while True:
        conn,addr=server_socket.accept()
        print(f"connections from{addr}established.")
        file_name=conn.recv(1024).decode()
        print(f"client requsted file:{file_name}")

        if os.path.exists(file_name):
            with open(file_name,'r') as file:
                conn.sendall(file.read().encode())
                print(f"file'{file_name}'sent to client.")
        else:
            conn.sendall(f"file'{file_name}'not found.".encode())
            print(f"file'{file_name}'not found.")

            conn.close()
            print("connection closed.")
       

if __name__=='__main__':
    start_server()