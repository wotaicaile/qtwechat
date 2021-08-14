from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer, QPoint, QRect, QSize
from PyQt5.QtGui import QPixmap, QFont, QFontMetrics
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QLabel, QListWidgetItem

from userchat import Ui_Form as userChat
from friendChat import Ui_Form as friendChat
from chat import Ui_Form as Chat



"""嵌入到主界面的子界面，聊天窗口"""


class ChatRun(QtWidgets.QDialog, Chat):
    def __init__(self, userprofile, friendprofile):
        super(ChatRun, self).__init__()

        self.setupUi(self)
        self.userprofile = userprofile
        self.friendprofile = friendprofile

    def sendmessagebox(self, str):
        item = QListWidgetItem()
        userChat = UserChat(str)
        userChat.label.setPixmap(QPixmap(self.userprofile).scaled(userChat.label.width(), userChat.label.height()))
        item.setSizeHint(QSize((userChat.label_2.width()), (userChat.label_2.height())))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, userChat)
        self.listWidget.verticalScrollBar().setValue(50)  # 设置滚动条到底部

        print("添加了发送气泡")

    def recvmessagebox(self, str):
        item = QListWidgetItem()
        friendChat = FriendChatRun(str)
        friendChat.label.setPixmap(
            QPixmap(self.friendprofile).scaled(friendChat.label.width(), friendChat.label.height()))
        item.setSizeHint(QSize((friendChat.label_2.width()), (friendChat.label_2.height())))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, friendChat)
        self.listWidget.verticalScrollBar().setValue(50)  # 设置滚动条到底部

        print("添加了接收气泡")

        # # for rown in range(10):
        # item1 = QListWidgetItem()
        # item2 = QListWidgetItem()
        # item3 = QListWidgetItem()
        # item4= QListWidgetItem()
        # item5= QListWidgetItem()
        # item6= QListWidgetItem()
        # friendChat = FriendChatRun()
        # userChat1 = UserChat()
        # userChat2 = UserChat()
        # userChat1.label.setPixmap(QPixmap("resource/罗小黑.jpg").scaled(userChat1.label.width(), userChat1.label.height()))
        # userChat2.label.setPixmap(QPixmap("resource/罗小黑.jpg").scaled(userChat2.label.width(), userChat2.label.height()))
        # friendChat.label.setPixmap(QPixmap("resource/罗小黑.jpg").scaled(friendChat.label.width(), friendChat.label.height()))
        #
        # item1.setSizeHint(QSize((friendChat.label_2.width()),(friendChat.label_2.height())))
        # item2.setSizeHint(QSize((userChat2.label_2.width()),(userChat2.label_2.height())))
        # item3.setSizeHint(QSize((userChat2.label_2.width()),(userChat2.label_2.height())))
        #
        #
        #
        # # fc.setxy(rown, 0)
        # # fc.lable.setText(wg.lable.text() + " " + str(rown))
        #
        # self.listWidget.addItem(item1)
        # self.listWidget.addItem(item2)
        # self.listWidget.addItem(item3)
        # # self.listWidget.addItem(item4)
        # # self.listWidget.addItem(item5)
        # # self.listWidget.addItem(item6)
        # self.listWidget.setItemWidget(item1, friendChat)
        # self.listWidget.setItemWidget(item2, userChat1)
        # self.listWidget.setItemWidget(item3, userChat2)
        # # self.listWidget.setItemWidget(item4, userChat)
        # # self.listWidget.setItemWidget(item5, friendChat)
        # # self.listWidget.setItemWidget(item6, userChat)
        # # self.listWidget.show()
        #
        # # friendChat = FriendChatRun()
        # # userChat = UserChat()
        # # hlay = QHBoxLayout(self)
        # # hlay.setContentsMargins(0, 0, 0, 0)
        # # hlay.setSpacing(0)
        # #
        # # # line = QLineEdit()
        # #
        # # hlay.addWidget(self.label_2)
        # # # hlay.addWidget(friendChat.label_2)
        # #
        # # # hlay.addWidget(line)
        # # self.label.setPixmap(QPixmap("resource/罗小黑.jpg").scaled(self.label.width(), self.label.height()))
        # # # friendChat.label.setPixmap(QPixmap("resource/罗小黑.jpg").scaled(self.label.width(), self.label.height()))
        # #
        # # hlay.addWidget(self.label)
        # # # hlay.addWidget(friendChat.label)
        # #
        # # # btn.pressed.connect(self.btnclick)
        # #
        # # self.label_2.adjustSize()  # 适应文本大小
        # # str = "服务端的实现,那么服务端要实现的就有这么几点：监听客户端的连接,同时操作多个用户,广播消息通知"
        # # print(len(str))
        # # self.label_2.setGeometry(QRect(20, 20, 50, 50 * 4))
        # # self.label_2.setText(str)


class FriendChatRun(QtWidgets.QDialog, friendChat):
    def __init__(self, str):
        super(FriendChatRun, self).__init__()

        self.setupUi(self)

        # str = "找一名晚托兼职老师。西街小学教一年级学生,工资找一名晚托兼职老师。西街小学教一年级学生,工资找一名晚托兼职老师。西街小学教一年级学生,工资"
        print(len(str))
        # 字数不满一段的
        if len(str) < 23 or len(str) == 23:
            self.label_2.adjustSize()  # 适应文本大小
            self.label_2.resize(len(str) * 16, 16)

            self.label_2.setText(str)
        # 字数满一段的
        else:
            hightx = len(str) / 23  # 几行
            # self.label_2.setGeometry(QRect(20, 20, 50, 50 * 4))
            font1 = QFont("微软雅黑", 16);
            fm = QFontMetrics(font1)
            pixelsWide = fm.horizontalAdvance("What's the width of this text?")
            pixelsHigh = fm.height()
            x = int(self.label.x() + 50 + 10)
            y = int(self.label.y())
            self.label_2.setGeometry(QRect(x, y, pixelsWide, pixelsHigh * hightx))
            self.label_2.setText(str)


class UserChat(QtWidgets.QDialog, userChat):
    def __init__(self, str):
        super(UserChat, self).__init__()

        self.setupUi(self)
        self.label_2.adjustSize()  # 适应文本大小
        # str = "找一名晚托兼职老师。西街小学教一年级学生,工资找一名晚托兼职老师。西街小学教一年级学生,工资找一名晚托兼职老师。西街小学教一年级学生,工资"

        # 字数不满一段的
        if len(str) < 23:

            self.label_2.adjustSize()  # 适应文本大小
            self.label_2.resize(len(str) * 16, 16)

            self.label_2.setText(str)
            self.label_2.move(self.label.x() - self.label_2.width() - 10, self.label.y())
        else:
            # 字数满一段的
            hightx = len(str) / 23  # 几行
            font2 = QFont("微软雅黑", 16);
            fm = QFontMetrics(font2)
            pixelsWide = fm.horizontalAdvance("What's the width of this text?")
            pixelsHigh = fm.height()

            self.label_2.setAlignment(QtCore.Qt.AlignTop)

            self.label_2.setGeometry(
                QRect(-(pixelsWide - self.label.x()) - 10, self.label.y(), pixelsWide, pixelsHigh * hightx))
            self.label_2.setText(str)


if __name__ == "__main__":
    import sys

    myapp = QApplication(sys.argv)  # 创建应用程序
    test = ChatRun("", "")
    test.show()  # 显示窗口
    sys.exit(myapp.exec_())
