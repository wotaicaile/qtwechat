此项目为期末大作业，耗时3个月从0开始搭建，  
最终被无良教师打击嘲讽无用处、过于简单，  
究其原因，他说前台界面修改了数据，后台sql无改动（实际上有的，他不懂技术，我当场进入数据库打他脸，把事务切给他看，他只能尴尬地挽尊表示只是提醒我以后做项目要注意这点）  
经此插曲，虽然知道我的实力不在他嘴里，但还是对项目有了芥蒂，故废弃  
也因为此事件，我从python转了Java  
最后一次更改代码时，不小心把login.ui的文件覆盖掉了，幸运的是login.py没有更改，还能用  
# qtwechat
用pyqt5模仿微信界面（网络编程大作业）  
网络编程、多线程、数据库、ui
介绍：  
·该系统基于PYQT5、python3.9、mysql开发，界面参考微信，通过socket进行网络聊天通信。  
·	具有验证用户登陆、聊天消息发送、动态显示聊天气泡等功能。  
环境依赖：  
·客户端打包后不依赖环境，跨平台可用，如需运行源代码，需安装PYQT5、python3.9、mysql8.0  
·服务端为python脚本，需安装python3+，mysql8.0数据库管理系统使用。    
使用说明：  
根据chatInfo.txt创建数据库  
运行chatServer.py  
运行loginrun.py  
# 运行与测试结果
在装有Python3.9、mysql8.0（密码为123456）、搭载Windows10系统的计算机上运行chatServer.py
服务器正在运行中
![image](https://user-images.githubusercontent.com/50273609/135586096-ef13732f-766b-4403-91f9-128e2ec0791f.png)  
双击客户端的exe程序进行登陆。  
![image](https://user-images.githubusercontent.com/50273609/135586190-f3f20a1d-ed49-4357-a9ec-00df026c539d.png)  
进入登陆界面：
 ![image](https://user-images.githubusercontent.com/50273609/135586218-81b8ddd0-93d4-416f-a8f4-46d7f882e7d7.png)  

输入非法账号密码：  
![image](https://user-images.githubusercontent.com/50273609/135586239-51fb7723-6e91-4469-83f1-5bdf961af097.png)

 返回信息：  
 ![image](https://user-images.githubusercontent.com/50273609/135586257-76584fd3-2fad-45ed-9588-96dd2b14f18e.png)

 输入合法账号：  
 
 ![image](https://user-images.githubusercontent.com/50273609/135586280-55941d51-8aa5-4db8-9a38-e266e37ee7df.png)  



