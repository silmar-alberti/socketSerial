# from serial.serial import *
from connection.server import *

# s = Porta()
# s.send('1')
# response = s.receive()
# print (response)
response = 'teste'
server = Server()
while True:
    data = server.recv()
    print (data)
    server.send(response.encode())

# host = ''        # Symbolic name meaning all available interfaces
# port = 12345     # Arbitrary non-privileged port
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# s.listen(1)
# conn, addr = s.accept()
# print('Connected by', addr)
#
# while True:
#     data = conn.recv(1024)
#
#     if not data: break
#     conn.sendall(data)
#     print (repr(data))
# conn.close()

