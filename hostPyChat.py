#MIT License
#Isaac D. Arcilla (twitter.com/newtoniaan)


import time
import socket
import sys

print("Welcome to PyChat(v1.1-newt)")
print("")
print("Initializing server...")
time.sleep(1)

s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
print("")
print(host)
print("")
name=input(str("Enter your username > "))
           
s.listen(1)
print("")
print("   [+] Waiting for incoming connections...")
conn,addr=s.accept()
print("   [+] Connection received.")

s_name=conn.recv(1024)
s_name=s_name.decode()
print("   [+] ",s_name,"has connected to the PyChat.")
print("")
conn.send(name.encode())

while 1:
           message=input(str("Type your message > "))
           print("")
           conn.send(message.encode())
           print("   [+] Message sent.")
           message=conn.recv(1024)
           message=message.decode()
           print("")
           print(name,":",message)
           print("")
                         
