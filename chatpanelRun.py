# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtWidgets import QApplication

import chatReadandWrite
from chatRun import ChatRun
from chatpanel import Ui_Form

"""子界面的子界面，动态发送与接收消息的ui绘制"""


class ChatpanelRun(QtWidgets.QDialog, Ui_Form):
    #  通过类成员对象定义信号对象

    signal_2 = pyqtSignal(str)  # 子界面类创建信号用来绑定主界面类的函数方法

    def __init__(self, client):
        super(ChatpanelRun, self).__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        # self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 设定该窗口透明显示

        # self.child = children()生成子窗口实例self.child
        self.tempWidge = {}
        self.client = client
        self.setupUi(self)
        self.thread = None  # 初始化线程
        self.write = None  # 初始化线程
        self.sendMessage = None  # 更新界面
        # self.friendslistWidget.itemClicked.connect(self.chooseFriend)
        # self.sendPbn.clicked.connect(self.start_login)  # 绑定多线程触发事件
        self.start_login()



    def get_data(self, friend_id):
        # 接受Form1传过来的num，保存到自己的变量里面。
        try:
            self.to_qq = friend_id.split(",")[0]
            self.friendprofile = friend_id.split(",")[1]
            self.userprofile = friend_id.split(",")[2]
            self.childShow()
        except:
            print("接收好友信息失败")

        # # 子界面通过signal_2 向主界面传递数据
        # signal_2.emit(self.num2)

    def on_sendPbn_pressed(self):

        try:
            message = self.messageEdit.toPlainText().strip()
            if message != "":
                self.child.sendmessagebox(message)

                self.messageEdit.clear()

                # # 开启线程、写入数据
                # threading.Thread(target=chatReadandWrite.read_chat, args=(self.client,self)).start()
                # threading.Thread(target=chatReadandWrite.write_chat, args=(self.client, self.to_qq, message)).start()
                # 创建线程

                self.write = chatReadandWrite.RunthreadWrite(self.client, self.to_qq, message)
                # 开始线程
                self.write.start()
            else:
                pass

        except:
            print("发信息失败")

    def childShow(self):
        # 如果当前已经有好友面板了，删除
        for i in range(self.MaingridLayout1.count()):
            self.MaingridLayout1.itemAt(i).widget().deleteLater()
        try:
            self.MaingridLayout1.addWidget(self.tempWidge[self.to_qq])
            self.tempWidge[self.to_qq].show()
        except:
            print("3")
            # 生成新的面板
            self.child = ChatRun(self.userprofile, self.friendprofile)
            self.tempWidge[self.to_qq] = self.child
            self.MaingridLayout1.addWidget(self.tempWidge[self.to_qq])
            # self.tempWidge[self.to_qq].show()
            # self.child.show()


    def start_login(self):
        # 创建线程
        self.thread = chatReadandWrite.RunthreadRead(self.client)
        # 连接信号
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # 开始线程
        self.thread.start()

    def call_backlog(self, msg):
        print("此处应该有接收气泡")
        print(msg)
        fromWho, msg = msg.split(":", 1)
        try:
            # 如果消息发送人是系统，那么默认是to_friend没有连接，才会发送过来的
            if fromWho == "server":
                self.child.recvmessagebox(msg)  # 将线程的参数传入界面
            # 如果消息发送人是当前面板，那么打印在当前面板
            if fromWho == self.to_qq:
                self.child.recvmessagebox(msg)  # 将线程的参数传入界面
        except Exception:
            print(Exception)
            print("self.child.recvmessagebox(msg)失败")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChatpanelRun()
    win.show()
    sys.exit(app.exec_())
