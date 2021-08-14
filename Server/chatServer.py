# /usr/bin/python3
import json
import socket
import threading

from PyQt5 import QtCore

import chatReadandWrite
from alldataBase import queryAccount, queryPassword, queryFriendRealtionship, queryuser


class ChatServer():
    def __init__(self):
        # 初始化socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定IP地址和端口
        server.bind(("localhost", 8999))
        # 设置最大监听数
        server.listen(5)
        # 设置一个字典，用来保存每一个客户端的连接 和 身份信息
        socket_mapping = {}
        # 开启准备等待获取客户端的链接
        while True:
            # 为每一个客户端开启一个线程、保证程序的高效运行
            sc, addr = server.accept()
            print("分配线程")
            msg = sc.recv(1024).decode()
            user_id, user_password = msg.split(",")
            print(user_id)
            print(user_password)
            if self.isUserLegel(user_id, user_password):
                write = RunthreadServer(sc, socket_mapping, user_id)
                # 开始线程
                write.start()
            else:
                sc.close()  # 关闭当前线程

    # 查询数据库，判断是否合法
    def isUserLegel(self, user_id, user_password):
        if queryAccount(user_id):
            if queryPassword(user_password):
                return True

        else:
            return False


# 继承QThread
class RunthreadServer(QtCore.QThread):
    # #  通过类成员对象定义信号对象
    # _signal = pyqtSignal(str)

    def __init__(self, socket, socket_mapping, user_id):
        super(RunthreadServer, self).__init__()
        self.socket = socket
        self.socket_mapping = socket_mapping
        self.user_id = user_id

    def run(self):
        """
            服务器处理数据、并实现两个客户端的交互
            :param socket:
            :param socket_mapping:
            :return:
            """

        # 存储身份(这里实现不允许同一账户多次登录)
        self.socket_mapping[self.user_id] = self.socket

        # 发送好友信息，收到此状态，更新列表
        datas = queryFriendRealtionship(self.user_id)
        data = json.dumps(datas)
        self.socket.send(bytes(data.encode('utf-8')))

        #发送自己头像信息
        userproflie = queryuser(self.user_id)[0][3]
        self.socket.send(userproflie.encode())
        usrname = queryuser(self.user_id)[0][2]

        self.socket.send(usrname.encode())
        print(usrname)
        
        # self.socket.send(f"{j+','}".encode())
        # for j in datas[i]:
        #     print(datas[i][j])

        # # 给所有socket 显示 该用户上线了
        # for k, v in self.socket_mapping.items():
        #     v.send(f"【{self.user_id}】上线了\n".encode())
        # 在这里服务器可以返回每个用户的信息（好友列表）

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
                # to_socket.send(msg.encode())
                turemsg = self.user_id + ":" + msg
                to_socket.send(turemsg.encode())

            except ConnectionResetError:
                # 该客户端离线了
                self.socket_mapping.pop(self.user_id)
                # 提示所有的客户端、该用户下线了
                # for k, v in self.socket_mapping.items():
                #     v.send(f"【{self.user_id}】下线了\n".encode())
                # # 退出循环
                # break
            except KeyError:
                # 该用户不在线、提示fqq,您的好友不在线
                turemsg = "server:您的好友不在线"
                self.socket.send(turemsg.encode())
        # self._signal.emit(msg)  # 注意这里与_signal = pyqtSignal(str)中的类型相同


if __name__ == '__main__':
    c = ChatServer()
