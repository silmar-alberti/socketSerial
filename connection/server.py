import socket
# host = ''        # Symbolic name meaning all available interfaces
# port = 12345     # Arbitrary non-privileged port
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# s.listen(1)
# conn, addr = s.accept()
# print('Connected by', addr)

class Server():
    port = 12345
    host = ''

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host,self.port))
        self.s.listen(1)
    # def listen(self):
    #     self.s.listen(1)

    def recv(self):
        self.conn,self.addr = self.s.accept()
        return self.conn.recv(1024)
    def send(self,data):
        self.conn.sendall(data)

    def __del__(self):
        self.conn.close()

# while True:
#     data = conn.recv(1024)
#
#     if not data: break
#     conn.sendall(data)
#     print (repr(data))
# conn.close()