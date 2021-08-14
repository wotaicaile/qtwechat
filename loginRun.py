from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication

from login import Ui_widget
from mainRun import MainRun as window_ok

"""继承登陆界面，做与登陆有关事件，发送登陆信息到远程服务器，验证成功进入主界面，验证失败断开socket连接"""
import socket


class ChatClient:
    """
    创建 socket 客户端，发送自己的身份，给服务器，验证密码，密码不正确，断开socket，密码正确，回到登陆
    """

    def __init__(self, user_id, user_pawword):
        """
        登陆验证
        """
        try:

            print("发起登陆验证请求")
            # 账号密码
            self.user_id = user_id
            self.user_pawword = user_pawword
            # 创建 socket 客户端
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 连接服务器
            self.client.connect(("localhost", 8999))
        
            print("连接服务器成功")

            # 发送自己的身份，给服务器
            msg = self.user_id + "," + self.user_pawword
            print(msg)
            self.client.send(msg.encode())
            print("验证身份成功")
        except:
            print("验证失败！服务器故障或账号密码错误！")


class loginRun(QtWidgets.QDialog, Ui_widget):
    def __init__(self):
        super(loginRun, self).__init__()
        self.setupUi(self)

        self.login_button.clicked.connect(self.confirmLogin)

    # 读取登陆信息，发送给服务器
    def confirmLogin(self):
        user = self.user.text().strip()
        password = self.password.text().strip()
        print("获取到登陆信息")
        try:
            self.client = ChatClient(user, password)
            self.w1 = window_ok(user, self.client)
            self.w1.show()
            self.hide()

        except:
            self.user.clear()
            self.user.setText("账号或密码错误！")
            print("连接服务器验证密码失败")


if __name__ == "__main__":
    import sys

    myapp = QApplication(sys.argv)  # 创建应用程序
    test = loginRun()
    test.show()  # 显示窗口
    sys.exit(myapp.exec_())
