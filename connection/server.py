import socket
# import threading
class Server():
    port = 12345
    host = ''
    conn=None
    addr = None
    # use_conn = threading.Lock()


    def iniciar(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Server.use_conn.acquire()
        self.s.bind((self.host,self.port))
        # Server.use_conn.release()

    def recv(self):
        # Server.use_conn.acquire()
        self.s.listen(1)
        self.conn,self.addr = self.s.accept()
        return self.conn , self.addr,self.conn.recv(1024)
        # Server.use_conn.release()

    def send(self,data):
        # Server.use_conn.acquire()
        self.conn.sendall(data)
        # Server.use_conn.release()

    def close(self):
        self.conn.close()

