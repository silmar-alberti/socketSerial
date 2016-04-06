__author__ = 'SILMAR'

import serial
import time

class Porta:
    porta = '/dev/ttyAMA0'
    velocidade = 115200
    timeout = 10
    mensagem = ''

    def __init__(self,):
        self.sport = serial.Serial(self.porta,self.velocidade)
        self.sport.close()
        self.sport.open()

    def send(self,mensagem):
        try:
            self.sport.flush()
            self.sport.write(mensagem.encode())
        except:
            pass
    def receive(self):

        # try:
        self.sport.flush()
        return (self.sport.readline()).decode()
        # except:
        #     pass

    def close(self):
        self.sport.close()
    # def __del__(self):
    #     self.sport.close()