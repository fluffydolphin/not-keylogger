import socket
from threading import Thread
import random
import argparse
import sys


parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets"
)

parser.add_argument(
    "-p", "--port", default=422, help="Port of the Server", type=int
)


args = parser.parse_args()
host =  "0.0.0.0"


client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, args.port))
s.listen(5)
print(f"[*] Listening as {host}:{args.port}")
separator_token = "<SEP>"

name = "server"



def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            client_socket.close()
            client_sockets.remove(client_socket)
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_sockets:
            client_socket.send(msg.encode())
            

c = socket.socket()
print(f"[*] Connecting to {host}:{args.port}...")
c.connect((host, args.port))
print("[+] Connected.")
    
keys = None

def listen_for_messages(cs):
    global keys
    while True:
        message = c.recv(1024).decode()
        if "!quit!" in message:
            client_socket.close()
            client_sockets.remove(client_socket)
        else:
            with open("log.txt", "w") as file1:
                file1.writelines(f"{message} \n")

nodes = []


while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.") 
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()
    l = Thread(target=listen_for_messages, args=(client_socket,))
    l.daemon = True
    l.start()
    for client_socket in client_sockets:
        for i in range(1, 100000):
            if i in nodes:
                continue
            else:
                nodes.append(i)
                i = str(i)
                c.send(i.encode())
                break
                
    


for cs in client_sockets:
    cs.close()

s.close()

