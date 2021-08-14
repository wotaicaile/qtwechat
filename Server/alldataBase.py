import pymysql


def connectDasebase():
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password="123456", db="chat",
                               charset='utf8')
        print("连接成功")

        return conn
    except Exception as e:
        print(e)
        print("连接数据库失败")


def queryFriendRealtionship(user):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select * from friendsRealtionship where chat_id =%s " % user

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")

def queryAllFriend():
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select * from chatInfo"

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            data = cur.fetchall()
            return data
        else:
            return 0
        # 将id和name显示到界面表格上
        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data[0][0])))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(data[0][1]))
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")

def UpdateAccountList(user, state):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 更新的sql语句
        sql = "update Users set  User_autoState=%s where User_ID =%s" % (state, user)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        UpdataResult = cur.execute(sql)
        if UpdataResult > 0:
            cur.connection.commit()  # 执行commit操作，更新语句才能生效
            print("更新数据库成功")
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("更新数据库失败")



def queryPassword(password):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select chat_password from `chatInfo` where  chat_password =%s " % (password)

        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        if cur.execute(sql):
            # data = cur.fetchall()
            # if data[0][1] == password:
            #     # 打印测试
            #     print(data[0][0])
            #     print(data[0][1])
            #     print("密码正确")
            return 1
        # 将id和name显示到界面表格上
        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(data[0][0])))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(data[0][1]))
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("登陆失败")


def queryuser(user):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select * from chatInfo where chat_id =%s " % (user)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        # 输入框为空：
        if cur.execute(sql):
            data = cur.fetchall()
            return data
        else:
            return 0
    except Exception as e:
        print(e)
        print("查询数据库失败")


# 查看账号是否存在
def queryAccount(user):
    try:
        conn = connectDasebase()
        cur = conn.cursor()
        # 查询的sql语句

        sql = "select chat_id from chatInfo where chat_id =%s " % (user)
        result = cur.execute(sql)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        # 输入框为空：
        if result is None:
            return -1
        # 账号存在：
        elif result > 0:
            return 1
        # 账号不存在：
        else:
            return 0
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        print("查询数据库失败")


def queryNoteList(file_path):
    import os
    filesTxt = []
    list = os.listdir(file_path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        if list[i][-4:] == ".txt":
            filesTxt.append(list[i][:-4])
    return filesTxt


if __name__ == "__main__":
    #获取当前用户头像测试
    print(queryuser("1747105016"))