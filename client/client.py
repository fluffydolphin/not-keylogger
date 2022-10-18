import socket
import random
from threading import Thread
import argparse
import sys
import getpass


parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets"
)

parser.add_argument("host", nargs="?", help="Address of the Server")

parser.add_argument(
    "-p", "--port", default=422, help="Port of the Server, default 5000", type=int
)


args = parser.parse_args()


if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.host:
    print("Host required! \n")
    parser.print_help()
    sys.exit(1)


s = socket.socket()
print(f"[*] Connecting to {args.host}:{args.port}...")
s.connect((args.host, args.port))
print("[+] Connected.")
    

print("""
              _     _              _                             
             | |   | |            | |                            
  _ __   ___ | |_  | | _____ _   _| | ___   __ _  __ _  ___ _ __ 
 | '_ \ / _ \| __| | |/ / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|
 | | | | (_) | |_  |   <  __/ |_| | | (_) | (_| | (_| |  __/ |   
 |_| |_|\___/ \__| |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|   
                              __/ |         __/ | __/ |          
                             |___/         |___/ |___/           
                  not keylogger v 1.0 | fluffydolphin
""")


password = getpass.getpass('Password: ')



def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()


while True:
    if password != '1212':
        print('Password is incorrect, restart and try again \n')
        sin = "!quit!"
        s.send(sin.encode())
        s.close()
        sys.exit()
    else: print("\nconnected\n")
    to_send =  input()
    to_send = f"{to_send}"
    if '!help!' in to_send:
        print("""
!help!               Shows you this

!connected!          Shows you how many and which nodes are connected'

""")
    else: s.send(to_send.encode())
    if "!quit!" in to_send:
        s.close()
        sys.exit()


s.close()
