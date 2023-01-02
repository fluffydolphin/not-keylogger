# not keylogger - is a simple encrypted keylogger

## What is keylogger?
not logger is basically a keylogging script using sockets to communicate with the attacker and pynput.keyboard that listens for keystrokes then sends them to the attacker through sockets.

1. The server binds sockets together so that the client and nodes can connect.
2. After the node has started and connected to the server it then listens with pynput
3. Then the server saves all the keystrokes to a log file on the server side

# How to install and run?

## Docker install

https://hub.docker.com/repository/docker/fluffydolphin/logger-server

## How to install git for cloning

1. Install git
   ```sh
   sudo apt install git
   ```



## Cloning using git.

1. Clone the repo
   ```sh
   git clone https://github.com/fluffydolphin/not-keylogger.git
   ```
   
2. Cd into not-keylogger
   ```sh
   cd not-keylogger
   ```
   
2. Cd into server, client or nodes
   ```sh
   cd server
   ```
   ```sh
   cd client
   ```
   ```sh
   cd node
   ```
3. Run command for either server, client or bot
   ```sh
   python3 server
   ```
   ```sh
   python3 client
   ```
   ```sh
   python3 node
   ```
  
That's all it takes to install and run not keylogger.
