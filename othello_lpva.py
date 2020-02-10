import sys, os, copy
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtGui, QtCore

from gameactive import * #필요한 변수 및 함수 불러오기

form_class_lpva = uic.loadUiType("ui/dlg_lpva.ui")[0] #UI 불러오기


class WindowClassLpva(QMainWindow, form_class_lpva) : #로컬 AI 대전 클래스 선언(화면 띄움)
    def __init__(self, parent=None) :
        super(WindowClassLpva,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Local Game : Player1 vs Player2(AI)")
        self.setWindowIcon(QIcon("res/icon.png"))
        self.btn_gameexit.clicked.connect(QApplication.instance().quit)
        self.points_xy = QtCore.QPoint()    

    def mousePressEvent(self, e): #마우스 클릭시 수행
        global p_x, p_y
        x = e.x()
        x = round((((x - 27) / 27) -1)/2) #좌표계산, 소수점 버리기
        y = e.y()
        y = round((((y - 70) / 27) -2)/2) #좌표계산, 소수점 버리기
        p_x = x
        p_y = y
        self.update()

    def paintEvent(self, ev): #그리기 이벤트
        painter = QPainter(self)
        self.drawGame(painter)      

    def drawGame(self, painter):
        global board, player, pass_check
        pixmap = QPixmap("res/board_green.png")
        cell_size = 50
        for x in range(0, 8):  #기본 판 그리기
            for y in range(0, 8):
                painter.drawPixmap(cell_size*x+cell_size - 10, cell_size*y+cell_size + 60, 50, 50,pixmap)
        if player == '0': #게임 시작 시 시작돌 및 선공 지정
            board[3][3] = '2'
            board[3][4] = '1'
            board[4][3] = '1'
            board[4][4] = '2'
            player = '1'

        if PassCheck(board, player): #패스여부
            print ('Player',player,' TURN PASS!!')
            if pass_check == 2: #둘다 패스하면 게임 끝
                print ('Game ended!!!!')
                if Score(board,'1') < Score(board,'2'): #승패여부 및 스코어 표시
                    pixmap_win = QPixmap("res/end_win.png")
                    painter.drawPixmap(cell_size*10+cell_size -55, cell_size*5+cell_size + 110, 240, 80,pixmap_win)
                elif Score(board,'1') > Score(board,'2'):
                    pixmap_lose = QPixmap("res/end_lose.png")
                    painter.drawPixmap(cell_size*10+cell_size -55, cell_size*5+cell_size + 110, 240, 80,pixmap_lose)
            else:
                if player == '1': #패스시 플레이어 넘기기
                    player = '2'
                    pass_check += 1
                    self.update()
                elif player == '2':
                    player = '1'
                    pass_check += 1
                    self.update()
        else:
            pass_check = 0
        if player == '1' and Available(board, p_x, p_y, player): #흑돌일때
            pixmap_turn1 = QPixmap("res/turn_red.png")
            painter.drawPixmap(cell_size*8+cell_size, cell_size*3+cell_size-35, 70, 60,pixmap_turn1)
            pixmap1 = QPixmap("res/mal_black.png")
            painter.drawPixmap(cell_size*p_x+cell_size - 10, cell_size*p_y+cell_size + 60, 50, 50,pixmap1)
            board[p_y][p_x] = '1' #돌두기
            (board, total) = Move(board, p_x, p_y, player) #뒤집기
            player = '2'
            for y in range(8): #저장되있는 돌 그려주기
                for x in range(8):
                    if board[y][x] == '1':
                        pixmap1 = QPixmap("res/mal_black.png")
                        painter.drawPixmap(cell_size*x+cell_size - 10, cell_size*y+cell_size + 60, 50, 50,pixmap1)
                    elif board[y][x] == '2':
                        pixmap2 = QPixmap("res/mal_white.png")
                        painter.drawPixmap(cell_size*x+cell_size - 10, cell_size*y+cell_size + 60, 50, 50,pixmap2)
            self.update()
        elif player == '2': #백돌일때
            pixmap_turn2 = QPixmap("res/turn_red.png")
            painter.drawPixmap(cell_size*8+cell_size, cell_size*1+cell_size+10, 70, 60,pixmap_turn2)
            (best_x, best_y) = Best(board, player) #MINIMAX알고리즘으로 수 계산
            board[best_y][best_x] = '2' #돌두기
            (board, total) = Move(board, best_x, best_y, player) #뒤집기
            player = '1'
            for y in range(8): #저장되있는 돌 그려주기
                for x in range(8):
                    if board[y][x] == '1':
                        pixmap1 = QPixmap("res/mal_black.png")
                        painter.drawPixmap(cell_size*x+cell_size -10, cell_size*y+cell_size + 60, 50, 50,pixmap1)
                    elif board[y][x] == '2':
                        pixmap2 = QPixmap("res/mal_white.png")
                        painter.drawPixmap(cell_size*x+cell_size -10, cell_size*y+cell_size + 60, 50, 50,pixmap2)
                    elif Available(board, x, y, player):
                        pixmap3 = QPixmap("res/avail.png")
                        painter.drawPixmap(cell_size*x+cell_size - 10, cell_size*y+cell_size + 60, 50, 50,pixmap3)
            self.update()
        else:
            if player == '1': #턴표시
                pixmap_turn1 = QPixmap("res/turn_red.png")
                painter.drawPixmap(cell_size*8+cell_size, cell_size*1+cell_size+10, 70, 60,pixmap_turn1)
            elif player == '2':
                pixmap_turn2 = QPixmap("res/turn_red.png")
                painter.drawPixmap(cell_size*8+cell_size, cell_size*3+cell_size-35, 70, 60,pixmap_turn2)
            for y in range(8): #저장되있는 돌 그려주기
                for x in range(8):
                    if board[y][x] == '1':
                        pixmap1 = QPixmap("res/mal_black.png")
                        painter.drawPixmap(cell_size*x+cell_size -10, cell_size*y+cell_size + 60, 50, 50,pixmap1)
                    elif board[y][x] == '2':
                        pixmap2 = QPixmap("res/mal_white.png")
                        painter.drawPixmap(cell_size*x+cell_size -10, cell_size*y+cell_size + 60, 50, 50,pixmap2)
                    elif Available(board, x, y, player):
                        pixmap3 = QPixmap("res/avail.png")
                        painter.drawPixmap(cell_size*x+cell_size - 10, cell_size*y+cell_size + 60, 50, 50,pixmap3)
        self.lcd_score_b.display(str(Score(board,'1'))) #스코어 업데이트
        self.lcd_score_w.display(str(Score(board,'2')))