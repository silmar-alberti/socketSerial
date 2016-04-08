__author__ = 'SILMAR'

import serial
import threading


class Porta:
    porta = '/dev/ttyAMA0'
    velocidade = 115200
    timeout = 10
    mensagem = ''
    use_serial = threading.Lock()


    def __init__(self,):
        self.sport = serial.Serial(self.porta,self.velocidade)
        Porta.use_serial.acquire()
        self.sport.close()
        Porta.use_serial.release()


    def send(self,mensagem):
        Porta.use_serial.acquire()
        self.sport.open()
        try:
            self.sport.flush()
            self.sport.write(mensagem.encode())
        except:
            pass
        self.sport.close()
        Porta.use_serial.release()
    def receive(self):
        Porta.use_serial.acquire()
        self.sport.open()
        # try:
        self.sport.flush()
        retorno = (self.sport.readline()).decode()
        self.sport.close()
        Porta.use_serial.release()
        return retorno

    def close(self):
        self.sport.close()
