import socket
import threading
from _thread import *
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((“192.168.43.236”,6666))
ThreadCount = 0
s.listen()
print(‘Socket is listening..’)

def receiving(*arg):
session = arg[0]
while True:
data = session.recv(2048)
print(data.decode())
print(‘\n’)

def sending(*arg):
session = arg[0]
address = arg[1]
while True:
response = input()
response_reframe = ‘192.168.43.236: ‘ + response
session.send(response_reframe.encode())

def multi_threaded_client(session,address):
threading.Thread(target=receiving, args=(session, )).start()
threading.Thread(target=sending, args=(session,address )).start()

while True:
session, address = s.accept()
print(‘Connected to: ‘ + address[0] + ‘:’ + str(address[1]))
start_new_thread(multi_threaded_client,(session,address[0] ))
ThreadCount += 1
print(‘Thread Number: ‘ + str(ThreadCount))