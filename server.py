import socket

s = socket.socket()
print("socket create")

s.bind(('localhost',9999))

s.listen(3)

print("wait for connection")

while True:
    c,address = s.accept()
    
    name = c.recv(1024).decode()

    print("connected with", address,name)

    c.send(bytes('welcome to the server', 'utf-8'))

    c.close()
