from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
import sys
import os
from websocket import *
from ast import literal_eval
import json
import threading

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.title="Python Window"
        self.top=50
        self.left=100
        self.width=1000
        self.height=100
        self.scrollBarHeight=200
        self.getData()
        self.cc = []
        self.InitWindow()

    def components(self):

        self.main_layout=QVBoxLayout(self)
        self.main_frame=QFrame(self)
        self.frame_layout=QVBoxLayout()

        formLayout=QGridLayout()
        groupbox=QGroupBox()
        labelList=[]
        t=0
        y=10

        sections=self.data_dictionary

        x=0
        section_length=len(sections)

        while t<section_length:
         appliances=sections[t]["appliances"]
         print(appliances)

         appliancesLength=len(appliances)
         c=0
         cc=0
         rr=0
         if(appliancesLength>0):
             three_frame = QFrame()
             three_frame.setGeometry(10,10,200,400)
             three_frame.setFrameShape(QFrame.StyledPanel)
             three_frame.setLineWidth(5)
             three_frame_layout = QGridLayout()
             three_frame.setLayout(three_frame_layout)

             section_name_frame=QFrame()
             section_name_frame_layout = QFormLayout()
             section_name_frame.setLayout(section_name_frame_layout)
             section_name=QLabel(sections[t]["name"])

             section_name.setStyleSheet('color:#000000;padding-left:0px')
             font=QFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
             font.setFamily("Times")
             font.setWeight(10)
             font.setUnderline(True)
             font.setBold(True)

             section_name.setFont(font)
             section_name_frame_layout.addWidget(section_name)
             three_frame_layout.addWidget(section_name_frame)

         while c<appliancesLength:
             print("yha1",appliancesLength)
             cc=0
             if abs(c-appliancesLength)>1:

                    three_frame_layout.addWidget(self.getInnerUi(appliances[c],y), rr, cc)

                    cc+=1

                    three_frame_layout.addWidget(self.getInnerUi(appliances[c+1],y), rr, cc)

                    rr+=1

                    c+=2
             else:
                  three_frame_layout.addWidget(self.getInnerUi(appliances[c],y), rr, cc)


                  c+=1
             self.scrollBarHeight+=100

         if appliancesLength>0:
             labelList.append(three_frame)
             formLayout.addWidget(labelList[x])
             x+=1

         t+=1
         y+=105



        groupbox.setLayout(formLayout)
        scrollBar=QScrollArea()
        scrollBar.setWidget(groupbox)
        scrollBar.setWidgetResizable(True)
        scrollBar.setFixedHeight(self.scrollBarHeight)

        self.frame_layout.addWidget(scrollBar)
        self.main_frame.setLayout(self.frame_layout)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setGeometry(QRect(5,5,500,500))
        self.main_frame.setLineWidth(1)
        self.main_layout.addWidget(self.main_frame)
        self.show()


    def getInnerUi(self,appliance,frameY):

        t={"dataObject":appliance};
        frame = QFrame()
        frame_layout = QGridLayout()
        frame.setLayout(frame_layout)


        frame.setGeometry(10, frameY, 100, 100)
        appliance_name="Appliance :   "+appliance["name"]
        name = QLabel(appliance_name)
        image_label = QLabel()
        name.setFont(QtGui.QFont("Times", 8 ))
        name.setStyleSheet('color:#231D1C ;padding-left:3px;padding-top:3px')
        image_label.setStyleSheet('padding-top:3px')
        pixmap = QPixmap("FAN.png")
        pixmap4 = pixmap.scaled(80, 80, QtCore.Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap4)

        if(appliance["switch"]["state"]==1):
         status="status :   "+"On"
         status = QLabel(status)
        else:
            status = "status :   " + "Off"
            status = QLabel(status)

        frame_layout.addWidget(name, 0, 0)
        status.setFont(QtGui.QFont("Times", 8))
        frame_layout.addWidget(image_label, 0, 1)
        frame_layout.addWidget(status, 1, 0)
        status.setStyleSheet('color:#231D1C  ;padding-left:3px;padding-top:3px')


        if appliance["is_regulatable"]==1:
            speed = QLabel("Speed: "+str(appliance["speed"]))
            speed.setStyleSheet('color: blue')
            frame_layout.addWidget(speed,1,1)
        else:
            speed = QLabel("Speed: 0")
            speed.setStyleSheet('color: #231D1C  ')
            frame_layout.addWidget(speed, 1, 1)
        connected = QLabel("Connected")
        connected.setStyleSheet('color: green;padding-left:3px')
        frame_layout.addWidget(connected, 2, 0)
        t["status"] = status;
        t["speed"]=speed;
        self.cc.append(t)
        return frame



    def updateUI(self,message):
        for c in self.cc:

            dataObject=c["dataObject"]
            if(message["code"]==dataObject["code"]):
                board=dataObject["switch"]["board"]
                b1=message["switch"]["board"]
                if(board["code"]==b1["code"]):
                    s=board["section"]
                    s1=message["switch"]["board"]["section"]
                    if(s["code"]==s1["code"]):
                        status=c["status"]
                        speed=c["speed"]
                        if(message["switch"]["state"]==1):
                         status.setText("Status:  ON")
                         status.setStyleSheet('color:#231D1C  ;padding-left:3px;padding-top:3px')
                        if(message["is_regulatable"]==1):
                         s="Speed:  "+str(message["speed"])
                         speed.setText(s)
                         speed.setStyleSheet('color: blue')





    def getData(self):
        path=os.getcwd()
        path=path+"\\conf\\HOMEAUTOMATION.data"

        file=open(path,"r")
        fileLength=file.seek(0,os.SEEK_END)
        data=""
        file.seek(0)
        while file.tell()<fileLength:
            data+=file.read(1024)
        data=data.replace('"',"'")
        self.data_dictionary=literal_eval(data)
        self.data_dictionary=self.data_dictionary["sections"]


    def InitWindow(self):
        self.setWindowTitle(self.title)

        self.components()
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()


class InitSocket:
    def on_open(t):
        print("open")

    def on_message(self, message):
        message=literal_eval(message)
        print(message)
        self.window.updateUI(message)

    def on_error(t):
        print("error", t)

    def on_close():
        print("bye")

    def initializeApplication(self):
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.window.getData()
        sys.exit(self.app.exec())

    def __init__(self):
        enableTrace(True)
        self.ws = WebSocketApp("ws://localhost:3000?Ritesh", on_message=self.on_message, on_error=self.on_error,on_close=self.on_close)
        self.ws.on_open = self.on_open
        x = threading.Thread(target=self.initializeApplication, daemon=True)
        x.start()
        self.ws.run_forever()


server = InitSocket()
