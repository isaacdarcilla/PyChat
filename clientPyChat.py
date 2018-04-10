#MIT License
#Isaac D. Arcilla (twitter.com/newtoniaan)


import time
import socket
import sys

print("Welcome to PyChat (v1.1-newt)")
print("")
print("Initializing client...")
time.sleep(1)

s=socket.socket()
print("")
host=input(str("Enter server address > "))
name=input(str("Enter you name         > "))
port=8080
print("")
print("   [+] Trying to connect to",host,"at port",port)
time.sleep(1)
s.connect((host,port))
print("   [+]  Connection succesful.")

s.send(name.encode())
s_name=s.recv(1024)
s_name=s_name.decode()

print("   [+] ",s_name,"has joined the PyChat.")

while 1:
    message=s.recv(1024)
    message=message.decode()
    print("")
    print(name,":",message)
    print("")
    message=input(str("Type your message > "))
    s.send(message.encode())
    print("")
    print("   [+] Message sent.")
    
