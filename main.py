from serial_port.serial import *
from connection.server import *
from  threading import Thread

server = Server()
server.iniciar()

def responder(data,conn,addr):
    serial = Porta()
    connect = Server()
    connect.conn = conn
    connect.addr =addr
    # print (data)

    serial.send(data.decode())
    response =serial.receive()
    connect.send(response.encode())



while True:
    # print ('aguardadndo conexao...\n')
    conn,addr,data = server.recv()
    # print ('conexao aceita' + str(data))
    # conn.sendto("teste".encode(),addr)
    Thread(target = responder,args=(data,conn,addr)).start()


