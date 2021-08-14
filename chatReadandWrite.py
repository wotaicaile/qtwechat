
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

"""网络传输收发"""


# 继承QThread
class RunthreadRead(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self, socket):
        super(RunthreadRead, self).__init__()
        self.socket = socket

    def run(self):
        while (True):
            try:
                msg = self.socket.recv(1024).decode()

                # 将接收到的信息、传给界面
                print("接收到：" + msg)
                self._signal.emit(msg)  # 注意这里与_signal = pyqtSignal(str)中的类型相同
            except ConnectionResetError:
                print("服务器连接失败、请重新连接~")


# 继承QThread
class RunthreadWrite(QtCore.QThread):

    def __init__(self, socket, to_qq, msg):
        super(RunthreadWrite, self).__init__()
        self.socket = socket
        self.to_qq = to_qq
        self.msg = msg

    def run(self):
        """
           发送信息给to_qq
           :param socket:
           :param to_qq:
           :return:
           """
        # 准备发送给服务器的内容
        msg = f"{self.to_qq}:{self.msg}"
        print("发出：" + msg)
        # 将信息发送给服务器
        try:
            self.socket.send(msg.encode())

        except ConnectionResetError:
            print("服务器连接失败、请重新连接~")
            # break


# 继承QThread
class RunthreadServer(QtCore.QThread):
    # #  通过类成员对象定义信号对象
    # _signal = pyqtSignal(str)

    def __init__(self, socket, socket_mapping):
        super(RunthreadServer, self).__init__()
        self.socket = socket
        self.socket_mapping = socket_mapping

    def run(self):
        """
            服务器处理数据、并实现两个客户端的交互
            :param socket:
            :param socket_mapping:
            :return:
            """
        # 接收客户端的身份、并进行存储
        qq = self.socket.recv(1024).decode()
        # 存储身份(这里也可以实现不允许同一账户多次登录)
        self.socket_mapping[qq] = self.socket
        # # 给所有socket 显示 该用户上线了
        # for k, v in self.socket_mapping.items():
        #     v.send(f"【{qq}】上线了\n".encode())

        # 开启循环、用来不断的进行转发数据
        while True:
            try:
                # 接收客户端发送的信息
                data = self.socket.recv(1024).decode()
                to_qq, msg = data.split(":", 1)
                # 将信息转发给 to_qq 对应的客户端
                to_socket = self.socket_mapping[to_qq]
                # 将信息发送给 to_socket
                # to_socket.send(f"{qq}:{msg}".encode())
                to_socket.send(msg.encode())

            except ConnectionResetError:
                # 该客户端离线了
                self.socket_mapping.pop(qq)
                # 提示所有的客户端、该用户下线了
                for k, v in self.socket_mapping.items():
                    v.send(f"【{qq}】下线了\n".encode())
                # 退出循环
                break
            except KeyError:
                # 该用户不在线、提示fqq,您的好友不在线
                self.socket.send(f"您的好友【{to_qq}】不在线\n".encode())
        # self._signal.emit(msg)  # 注意这里与_signal = pyqtSignal(str)中的类型相同
