import socket

def request_file(file_name):
    host = "10.11.1.176"
    port = 8003

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server")

    client_socket.send(file_name.encode())
    data = client_socket.recv(4096).decode()

    if data.startswith("File"):
        print("File not found")
    else:
        print("File Content: ", data, sep="\n")

    client_socket.close()
    print("Connection closed")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    request_file(file_name)