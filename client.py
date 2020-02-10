from socket import *
from msg import *
from log import *

class Client:
    def __init__(self, ip:str, port_number:int):
        #server start.
        self.ip = ip
        self.port = port_number
        self.run = False

    def connect(self):
        if self.run:
            return
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))

    def close(self):
        if not self.run:
            return
        self.client_socket.close()

    def send(self, msg:str):
        self.client_socket.send(msg.encode('utf-8'))

    def recv(self):
        recv_msg = self.client_socket.recv(1024)
        return recv_msg.decode('utf-8')

class Othello:
    def __init__(self, ip, port):
        self.client_socket = Client(ip, port)
        self.log = Log()

        self.client_socket.connect()
        self.log.write('Server Connection Success!')

        accept_msg = self.client_socket.recv()
        try:
            code, data = parse_msg(accept_msg)
        except:
            self.log.write('ERROR: parse error ' + accept_msg)
            sys.exit(-1)

        if code != 'accept':
            self.log.write('ERROR: accept msg error: ' + code + ' ' + str(data))
            sys.exit(-1)
        
        self.color = data['color']
        self.token = data['token']
        self.board = data['board']
        
        self.log.write('Color: {color}, Token: {token}, Board: {board}'.format(color=self.color, token=self.token, board=self.board))
    
    def wait_for_turn(self):
        while True:
            msg = self.client_socket.recv()
            try:
                code, data = parse_msg(msg)
            except:
                self.log.write('ERROR: parse error ' + msg)
                sys.exit(-1)

            if code == 'turn':
                self.log.write("turn: " + data['available'])
                return code, data
            elif code == 'update':
                self.board = data['board']
                self.log.write("update: " + data['board'])
                return code, data             
            elif code == 'end':
                self.log.write("game end: " + data['status'] + " " + data['score'])
                self.log.write('final board: ' + data['board'])
                return code, data
            else:
                self.log.write('ERROR: invaild code error: ' + code + ' ' + str(data))
                sys.exit(-1)

    def move(self, cell_corr):
        msg = gen_move_msg(cell_corr, self.token)
        self.client_socket.send(msg)