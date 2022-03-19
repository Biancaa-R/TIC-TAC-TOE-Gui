import random
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import csv
import sys, os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

matrice=[[0,0,0],[0,0,0],[0,0,0]]
seq=[]

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("tictactoe1.ui",self)
        self.value.setText("Hello  "+name+" !")
        self.Button1.clicked.connect(self.gotoset1)
        self.Button2.clicked.connect(self.gotoset2)
        self.Button3.clicked.connect(self.gotoset3)
        self.Button4.clicked.connect(self.gotoset4)
        self.Button5.clicked.connect(self.gotoset5)
        self.Button6.clicked.connect(self.gotoset6)
        self.Button7.clicked.connect(self.gotoset7)
        self.Button8.clicked.connect(self.gotoset8)
        self.Button9.clicked.connect(self.gotoset9)
        self.playagain.clicked.connect(self.gotoclear)
        self.logout.clicked.connect(self.gotowelcome)

    def gotowelcome(self):
        welcome= WelcomeScreen() 
        widget.addWidget(welcome)
        widget.setCurrentWidget(welcome) 
    def checkwinner(self):
        
        line=0
        for i in matrice:
            for j in i:
                if j==0:
                    line+=1
        
        global points         
        points=line
        y=self.confirm_2.text()
        if y in ["Player wins","player wins"]:
            F=open("high.csv","a",newline="")
            w=csv.writer(F)
            w.writerow([name,username,str(points)])
            F.close()
            print("Successful")
        
        #global matrice
        if matrice[0][0]!=0 and matrice[0][1]!=0 and matrice[0][2]!=0:
            if matrice[0][0]==1 and matrice[0][1]==1 and matrice[0][2]==1:
               self.confirm_2.setText("Player wins")
            elif matrice[0][0]==2 and matrice[0][1]==2 and matrice[0][2]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        if matrice[1][0]!=0 and matrice[1][1]!=0 and matrice[1][2]!=0:
            if matrice[1][0]==1 and matrice[1][1]==1 and matrice[1][2]==1:
                self.confirm_2.setText("Player wins")
                #self.pointcalc()
            elif matrice[1][0]==2 and matrice[1][1]==2 and matrice[1][2]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        if matrice[2][0]!=0 and matrice[2][1]!=0 and matrice[2][2]!=0:
            if matrice[2][0]==1 and matrice[2][1]==1 and matrice[2][2]==1:
                self.confirm_2.setText("Player wins")
                '''if True:
                    pointcalc()'''
            elif matrice[2][0]==2 and matrice[2][1]==2 and matrice[2][2]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        if matrice[0][0]!=0 and matrice[1][0]!=0 and matrice[2][0]!=0:
            if matrice[0][0]==1 and matrice[1][0]==1 and matrice[2][0]==1:
                self.confirm_2.setText("Player wins")
                '''if True:
                    pointcalc()'''
            elif matrice[0][0]==2 and matrice[1][0]==2 and matrice[2][0]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        if matrice[0][1]!=0 and matrice[1][1]!=0 and matrice[2][1]!=0:
            if matrice[0][1]==1 and matrice[1][1]==1 and matrice[2][1]==1:
                self.confirm_2.setText("Player wins")
                '''if True:
                    pointcalc()'''
            elif matrice[0][1]==2 and matrice[1][1]==2 and matrice[2][1]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        if matrice[0][2]!=0 and matrice[1][2]!=0 and matrice[2][2]!=0:
            if matrice[0][2]==1 and matrice[1][2]==1 and matrice[2][2]==1:
                self.confirm_2.setText("Player wins")
                '''if True:
                    pointcalc()'''
            elif matrice[0][2]==2 and matrice[1][2]==2 and matrice[2][2]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        if matrice[0][0]!=0 and matrice[1][1]!=0 and matrice[2][2]!=0:
            if matrice[0][0]==1 and matrice[1][1]==1 and matrice[2][2]==1:
                self.confirm_2.setText("Player wins")
                '''if True:
                    pointcalc()'''
            elif matrice[0][0]==2 and matrice[1][1]==2 and matrice[2][2]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        if matrice[0][2]!=0 and matrice[1][1]!=0 and matrice[2][0]!=0:
            if matrice[0][2]==1 and matrice[1][1]==1 and matrice[2][0]==1:
                self.confirm_2.setText("Player wins")
                '''if True:
                    pointcalc()'''
            elif matrice[0][2]==2 and matrice[1][1]==2 and matrice[2][0]==2:
                self.confirm_2.setText("Opponent wins")
            else:
                pass
        else:
            pass
        
        
    def response(self):
        #global matrice
        global seq
        for row_number, row_data in enumerate(matrice):
            for col_number,col_data in enumerate(row_data):
                if col_data==0:
                    seq.append([row_number,col_number])
                 
        if matrice[1][1]==0:
            seq=[]
            y=self.confirm_2.text()
            if y in ["Player wins","Opponent wins","ALL done"]:
                pass
            else:
                self.Button5.setText("O")
                matrice[1][1]=2
            if True:
                self.checkwinner()
                
        elif len(seq)!=0:
            choice1=random.choice(seq)
            row_number,col_number=choice1
            if row_number==0 and col_number==0:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button1.setText("O")
                    matrice[0][0]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==0 and col_number==1:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button2.setText("O")
                    matrice[0][1]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==0 and col_number==2:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button3.setText("O")
                    matrice[0][2]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==1 and col_number==0:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button4.setText("O")
                    matrice[1][0]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==1 and col_number==1:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:                
                    self.Button5.setText("O")
                    matrice[1][1]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==1 and col_number==2:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button6.setText("O")
                    matrice[1][2]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==2 and col_number==0:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button7.setText("O")
                    matrice[2][0]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==2 and col_number==1:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button8.setText("O")
                    matrice[2][1]=2
                    seq=[]
                if True:
                    self.checkwinner()
            elif row_number==2 and col_number==2:
                y=self.confirm_2.text()
                if y in ["Player wins","Opponent wins","ALL done"]:
                    pass
                else:
                    self.Button9.setText("O")
                    matrice[2][2]=2
                    seq=[]
                if True:
                    self.checkwinner()
        
        else:
            self.confirm_2.setText("ALL done")
    def gotoclear(self):
        global matrice
        self.Button1.setText("")
        self.Button2.setText("")
        self.Button3.setText("")
        self.Button4.setText("")
        self.Button5.setText("")
        self.Button6.setText("")
        self.Button7.setText("")
        self.Button8.setText("")
        self.Button9.setText("")
        self.confirm_2.setText("")
        matrice=[[0,0,0],[0,0,0],[0,0,0]]
        seq=[]
        
    def gotoset1(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button1.setText("X")
            matrice[0][0]=1
            if True:
                self.response()
        if True:
            self.checkwinner()

        
    def gotoset2(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button2.setText("X")
            matrice[0][1]=1
            if True:
                self.response()
        if True:
            self.checkwinner()

        
    def gotoset3(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button3.setText("X")
            matrice[0][2]=1
            if True:
                self.response()
        if True:
            self.checkwinner()

    def gotoset4(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button4.setText("X")
            matrice[1][0]=1
            if True:
                self.response()
        if True:
            self.checkwinner()

    def gotoset5(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button5.setText("X")
            matrice[1][1]=1
            if True:
                self.response()
        if True:
            self.checkwinner()
    def gotoset6(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button6.setText("X")
            matrice[1][2]=1
            if True:
                self.response()
        if True:
            self.checkwinner()

    def gotoset7(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button7.setText("X")
            matrice[2][0]=1
            if True:
                self.response()
        if True:
            self.checkwinner()
    def gotoset8(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button8.setText("X")
            matrice[2][1]=1
            if True:
                self.response()
        if True:
            self.checkwinner()
    def gotoset9(self):
        global matrice
        y=self.confirm_2.text()
        if y in ["Player wins","Opponent wins","ALL done"]:
            pass
        else:
            self.Button9.setText("X")
            matrice[2][2]=1
            if True:
                self.response()
        if True:
            self.checkwinner()
        
        
class WelcomeScreen(QMainWindow):
    #initializing and loading welcome screen
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcome.ui", self)
        self.usernamefield.setPlaceholderText("Enter your Username")
        self.passwordfield.setPlaceholderText("Enter your name")
        
        self.GAME.clicked.connect(self.gotogame)
        self.passwordfield.returnPressed.connect(self.gotogame)
        self.HIGHSCORES.clicked.connect(self.gotohigh)

    def gotogame(self):
        global username
        global name
        username = self.usernamefield.text()
        name = self.passwordfield.text()
        if len(username)==0 or len(name)==0:
            self.error_2.setText("Please fill in all fields")
        else:
            F=open("Record.csv","a",newline="")
            w=csv.writer(F)
            w.writerow([username,name])
            F.close()
            game = MainPage() 
            widget.addWidget(game)
            widget.setCurrentWidget(game)     

    #checking user credentials
    def gotohigh(self):
        F=open("high.csv","r",newline="")
        r=csv.reader(F)
        for i in r :
            print(i)
        

app = QApplication(sys.argv)
welcome=WelcomeScreen()
#mainpage = MainPage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(720)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting..")    

