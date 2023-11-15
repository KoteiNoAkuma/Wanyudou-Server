import socket
import time
import subprocess
import threading


def testes():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("172.16.236.21", 45678))
    while True:
        data = sock.recv(1024).decode()
        print(data)