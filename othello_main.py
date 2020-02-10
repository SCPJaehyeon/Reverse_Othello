import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from othello_lpvp import *
from othello_lpva import *
from othello_npvp import *

form_class_main = uic.loadUiType("ui/dlg_main.ui")[0] #UI 불러오기


class WindowClassMain(QMainWindow, form_class_main) : #메인화면 클래스 선언(화면 띄움)
    def __init__(self, parent=None) :
        super(WindowClassMain, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Reverse Othello :)")
        self.setWindowIcon(QIcon("res/icon.png"))
        
        self.btn_lpvp.clicked.connect(self.buttonLpvpFunction) #버튼 클릭 시 함수 호출
        self.btn_lpva.clicked.connect(self.buttonLpvaFunction)
        self.btn_npvp.clicked.connect(self.buttonNpvpFunction)
        self.btn_madeby.clicked.connect(self.buttonMadebyFunction)
        self.btn_exit.clicked.connect(QApplication.instance().quit)
        self.dialogs = list() #다이얼로그 여러개위한 리스트함수

    def buttonLpvpFunction(self) : #local pvp 버튼 클릭시 함수
        LpvpWindow = WindowClassLpvp()
        self.dialogs.append(LpvpWindow)
        LpvpWindow.show()

    def buttonLpvaFunction(self) : #local pva 버튼 클릭시 함수
        LpvaWindow = WindowClassLpva()
        self.dialogs.append(LpvaWindow)
        LpvaWindow.show()

    def buttonNpvpFunction(self) : #network pvp 버튼 클릭시 함수
        NpvpWindow = WindowClassNpvp()
        self.dialogs.append(NpvpWindow)
        NpvpWindow.show()
        
    def buttonMadebyFunction(self) : #made by 버튼 클릭시 함수
        QMessageBox.information(self, "Made by", "Reverse Othello v0.1\nMade by. JaeHyeon")


def main():
    app = QApplication(sys.argv) #프로그램 실행 클래스
    MainWindow = WindowClassMain() #인스턴스 생성 
    MainWindow.show() #프로그램 화면 show
    app.exec_() #이벤트루프로 진입


if __name__ == "__main__" :
    main()