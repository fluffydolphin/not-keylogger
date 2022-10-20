import socket
from threading import Thread
import random
import argparse
import sys
import os


parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets"
)

parser.add_argument(
    "-p", "--port", default=422, help="Port of the Server", type=int
)


args = parser.parse_args()
host =  "0.0.0.0"


name = "server"

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
            with open("log.txt", "w") as file1:
                file1.writelines(f"{msg} \n")
        except Exception as e:
                client_socket.close()
                client_sockets.remove(client_socket)      
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_sockets:
            client_socket.send(msg.encode())


nodes = []


while True:
    client_sockets = set()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, args.port))
    s.listen(5)
    print(f"[*] Listening as {host}:{args.port}")
    separator_token = "<SEP>"
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.") 
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()


for cs in client_sockets:
    cs.close()

s.close()

