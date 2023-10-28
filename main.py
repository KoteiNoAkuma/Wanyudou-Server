import socket
import time
import subprocess
import threading


def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("172.16.236.21", 6666))
    conne, addr = sock.accept()
    with conne:
        print(f"Connected by {addr}")
        while True:
            data = conne.recv(1024)
            if not data:
                break
            conne.sendall(data)


if __name__ == '__main__':
    print('WELCOME TO WANYUDOU!! (THE GOOD SIDE)')
    print("""
      |_|   ,
     ('.') ///
     <(_)`-/'
 <-._/J L /  -WANYUDOU-""")
    listen()
