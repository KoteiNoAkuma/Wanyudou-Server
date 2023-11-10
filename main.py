import socket
import time
import subprocess
import threading


def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 6665))
    sock.listen()
    print("\n\n\nOUÇA COM ATENÇÃO...TEM ALGO LÁ FORA?")
    conne, addr = sock.accept()
    with conne:
        print(f"TE OUVI!! ALI!")
        multiThread(conne)

def receivingData(session):
    while True:
        data = session.recv(1024)
        print(data.strip().decode())

def sendingData(session):
    while True:
        command = input()
        session.sendall(command.encode())

def multiThread(session):
    threading.Thread(target=receivingData(session)).start()
    threading.Thread(target=sendingData(session)).start()




if __name__ == '__main__':
    listZombies = []
    print('WELCOME TO WANYUDOU!! (THE GOOD SIDE)')
    print("""
      |_|   ,
     ('.') ///
     <(_)`-/'
 <-._/J L /  -WANYUDOU-""")
    listen()
