# -*- coding: utf-8 -*-
import json

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QSize
from PyQt5.QtGui import QIcon

from chatpanelRun import ChatpanelRun
from main import Ui_Form

"""主界面，不作主要处理，主要事件在子界面"""


class MainRun(QtWidgets.QDialog, Ui_Form):
    _startPos = None
    _endPos = None
    _isTracking = False
    user = ""
    # 声明无参数的信号
    _signal = pyqtSignal(str)

    def __init__(self, user, client):
        super(MainRun, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 设定该窗口透明显示
        self.setupUi(self)
        self.friendslistWidget.itemDoubleClicked.connect(self.chooseFriend)
        self.user = user
        print(self.user + "已登陆")

        #
        #  拿到登录后的socket
        self.chat = client
        self.friend_avatar = {}
        self.friendDatas = self.chat.client.recv(1024).decode()
        print(self.friendDatas)
        self.path = self.chat.client.recv(1024).decode()
        print(self.path)
       

        self.loadFriendlistWidgetdata()
        self.init()
        self.thread = None  # 初始化线程
        if self.gridLayout_2.count() == 0:
            # # # 面板不存在，生成
            print("面板不存在，生成")
            self.temp = ChatpanelRun(self.chat.client)
            try:
                self._signal.connect(self.temp.get_data)  # 进程连接回传到GUI的事件
                print("信号绑定成功")
            except:
                print("信号绑定失败")
            self.childChat = self.temp
            # # 添加子窗口
            self.gridLayout_2.addWidget(self.childChat.Chatframe)
            self.temp.show()

    def init(self):

        self.label_mask.setVisible(False)
        self.label_2.setVisible(False)
        self.currentChatFriendName.setText("")

        self.avatarlabel.setIcon(QIcon(self.path))
        self.avatarlabel.setIconSize(QSize(self.avatarlabel.width(), self.avatarlabel.height()))  # 设置icon大小

    def loadFriendlistWidgetdata(self):

        list_or_dict = json.loads(self.friendDatas)

        for i in range(len(list_or_dict)):
            friend_id = list_or_dict[i][1]
            friend_name = list_or_dict[i][2]
            tempstr = friend_name + "(" + friend_id + ")"
            self.friend_avatar[friend_id] = list_or_dict[i][3]
            self.friendslistWidget.addItem(tempstr)

    # 在这里获取要通信的好友
    def chooseFriend(self):

        self.currentChatFriendName.clear()
        # 获取好友id和头像
        Currentchatfriends = self.friendslistWidget.currentItem().text()
        self.friend_id = Currentchatfriends.split("(")[1].split(")")[0]
        self.friendpath = self.friend_avatar[self.friend_id]

        # 在面板上添加
        self.currentChatFriendName.setText(Currentchatfriends)
        # 发送信号
        try:
            str = self.friend_id + "," + self.friendpath + "," + self.path
            print(str)
            self._signal.emit(str)  # 注意这里与_signal = pyqtSignal(str)中的类型相同
        except:
            print("信号发送失败")

    def mouseMoveEvent(self, event):  # 重写移动事件

        self._endPos = event.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label_2.setVisible(False)
            self._isTracking = True
            self._startPos = QPoint(event.x(), event.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

##    # 主界面上的头像点击事件，已完成
##    def on_avatarlabel_clicked(self):
##        try:
##            self.label_2.setVisible(True)
##            self.label_2.setText("%s\n用户名：%s" % (self.username, self.user))  # 服务器数据库返回不同昵称和用户名
##        except:
##            print("头像点击事件失败")
# 以下为测试代码
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     client = ChatClient("1747105016", "123456")
#     win1 = MainRun("1747105016", client)
#     win1.show()
#     sys.exit(app.exec_())
# # 以下为测试代码
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     client = ChatClient("1747105016", "123456")
#     win2 = MainRun("1234567890", client)
#     win2.show()
#     sys.exit(app.exec_())
#     # 以下为测试代码
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     client = ChatClient("1747105016", "123456")
#     win3 = MainRun("2638634836", client)
#     win3.show()
#     sys.exit(app.exec_())
