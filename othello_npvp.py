import sys, os, copy, threading
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import QThread, QTimer

from client import * #네트워크 클라이언트 클래스 불러오기
from msg import *
from log import *

from matching import * #XY > 1A형태, 1A > XY형태 변환 함수 불러오기
from gameactive import * #필요한 변수 및 함수 불러오기

form_class_npvp = uic.loadUiType("ui/dlg_npvp.ui")[0] #UI 불러오기


def GameActive(input_dip, input_dport):
    global player
    global turn_check
    global game_status
    mypass_check = 0
    othello = Othello(input_dip, int(input_dport))
    while True:
        code, data = othello.wait_for_turn()
        if code == 'end': # 게임 끝났을 때
            print("status: " + data['status'] + ' score: ' + data['score'])
            if data['status'] == "win":
                game_status = "win"
            elif data['status'] == "lose":
                game_status = "lose"
            break
        elif code == 'turn': # 턴일 때
            if player == '0':
                if data['available'] == "3D 4C 5F 6E":
                    player = '1'
                    turn_check = '1'
                else:
                    player = '2'
                    turn_check = '2'
            oth_board = ChangeBoard(othello.board)
            (x, y) = Best(oth_board, player)
            best = Matching(x, y)
            input_corr = best
            othello.move(input_corr)
            if mypass_check == 1:
                mypass_check = 5
            else:
                mypass_check = 0
        elif code == 'update': # 업데이트 될 때
            global updated_board
            global lastest
            updated_board = ChangeBoard(data['board'])
            lastest = Matching_rev(data['move'])
            if turn_check == '1' and mypass_check < 2:
                turn_check = '2'
            elif turn_check == '2' and mypass_check < 2:
                turn_check = '1'
            print("mypass_check : ",mypass_check)
            mypass_check += 1

class WindowClassNpvp(QMainWindow, form_class_npvp) : #네트워크 대전 클래스 선언(화면 띄움)
    def __init__(self, parent=None) :
        super(WindowClassNpvp,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Network Game : Player1(AI) vs Player2(AI)")
        self.setWindowIcon(QIcon("res/icon.png"))
        global game_status
        self.btn_connect.clicked.connect(self.connectbuttonFunction)
        self.btn_gameexit.clicked.connect(QApplication.instance().quit)
        if game_status == "win" or game_status == "lose":
            self.close()

    def connectbuttonFunction(self):
        input_dip = self.input_dip.text()
        input_dport = self.input_dport.text()
        game_thread = threading.Thread(target=GameActive, args=(input_dip,input_dport))
        game_thread.start()

    def paintEvent(self, ev):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        painter = QPainter(self)
        self.drawGame(painter)
        

    def drawGame(self, painter):
        global player, updated_board, lastest, turn_check
        pixmap = QPixmap("res/board_green.png")
        cell_size = 50  
        if player == '0': #게임 시작시 초기 돌 셋팅
            for y in range(0, 8):
                for x in range(0, 8):
                    painter.drawPixmap(cell_size*x+cell_size -15, cell_size*y+cell_size + 85, 50, 50,pixmap)
            pixmap1 = QPixmap("res/mal_black.png")
            painter.drawPixmap(cell_size*3+cell_size -15, cell_size*4+cell_size + 85, 50, 50,pixmap1)
            painter.drawPixmap(cell_size*4+cell_size -15, cell_size*3+cell_size + 85, 50, 50,pixmap1)
            pixmap2 = QPixmap("res/mal_white.png")
            painter.drawPixmap(cell_size*3+cell_size -15, cell_size*3+cell_size + 85, 50, 50,pixmap2)
            painter.drawPixmap(cell_size*4+cell_size -15, cell_size*4+cell_size + 85, 50, 50,pixmap2)
        else:
            if player == '1': #흑돌일때
                if turn_check == '1': #턴표시
                    pixmap_turn1 = QPixmap("res/turn_red.png")
                    painter.drawPixmap(cell_size*8+cell_size +5, cell_size*1+cell_size+10, 70, 60,pixmap_turn1)
                elif turn_check == '2':
                    pixmap_turn2 = QPixmap("res/turn_red.png")
                    painter.drawPixmap(cell_size*8+cell_size +5, cell_size*3+cell_size-35, 70, 60,pixmap_turn2)
                pixmap1 = QPixmap("res/mal_black.png")
                painter.drawPixmap(cell_size*12+cell_size -15, cell_size*1+cell_size+25, 50, 50,pixmap1)
                pixmap2 = QPixmap("res/mal_white.png")
                painter.drawPixmap(cell_size*12+cell_size -15, cell_size*3+cell_size-16 , 50, 50,pixmap2)
            elif player == '2': #흰돌일때
                if turn_check == '1': #턴표시
                    pixmap_turn1 = QPixmap("res/turn_red.png")
                    painter.drawPixmap(cell_size*8+cell_size +5, cell_size*3+cell_size-35, 70, 60,pixmap_turn1)
                elif turn_check == '2':
                    pixmap_turn2 = QPixmap("res/turn_red.png")
                    painter.drawPixmap(cell_size*8+cell_size +5, cell_size*1+cell_size+10, 70, 60,pixmap_turn2)
                pixmap1 = QPixmap("res/mal_black.png")
                painter.drawPixmap(cell_size*12+cell_size -15, cell_size*3+cell_size-16, 50, 50,pixmap1)
                pixmap2 = QPixmap("res/mal_white.png")
                painter.drawPixmap(cell_size*12+cell_size -15, cell_size*1+cell_size+25, 50, 50,pixmap2)
            for y in range(0, 8):
                for x in range(0, 8):
                    painter.drawPixmap(cell_size*x+cell_size -15, cell_size*y+cell_size + 85, 50, 50,pixmap)
                    if updated_board[y][x] == '1':
                        pixmap1 = QPixmap("res/mal_black.png")
                        painter.drawPixmap(cell_size*x+cell_size -15, cell_size*y+cell_size + 85, 50, 50,pixmap1)
                    elif updated_board[y][x] == '2':
                        pixmap2 = QPixmap("res/mal_white.png")
                        painter.drawPixmap(cell_size*x+cell_size -15, cell_size*y+cell_size + 85, 50, 50,pixmap2)
                    if (x, y) == lastest: #최근돌 표시
                        pixmap3 = QPixmap("res/lastest_red.png")
                        painter.drawPixmap(cell_size*x+cell_size -15, cell_size*y+cell_size + 85, 50, 50,pixmap3)
        self.lcd_score_b.display(str(Score(updated_board,'1'))) #스코어
        self.lcd_score_w.display(str(Score(updated_board,'2')))
        if game_status == "win": #이겼을때
            pixmap_win = QPixmap("res/end_win.png")
            painter.drawPixmap(cell_size*10+cell_size -55, cell_size*5+cell_size + 110, 240, 80,pixmap_win)
        elif game_status == "lose": #졌을때
            pixmap_lose = QPixmap("res/end_lose.png")
            painter.drawPixmap(cell_size*10+cell_size -55, cell_size*5+cell_size + 110, 240, 80,pixmap_lose)

