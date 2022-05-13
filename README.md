此项目为期末大作业，耗时3天完成
# qtwechat（最终版本，不再更新）
用pyqt5模仿微信界面（网络编程大作业）  
技术涉及到网络编程、多线程、数据库、ui设计  
介绍：  
·该系统基于PYQT5、python3.9、mysql开发，界面参考微信，通过socket实现网络聊天通信。  
·	具有验证用户登陆、聊天消息发送、动态显示聊天气泡等功能。  
环境依赖：  
·客户端打包后不依赖环境，跨平台可用。  
本项目的ide环境为PyCharm，如需运行源代码，建议导入PyCharm，之后还需安装python3.9、mysql8.0，其中python需要用pip3命令安装PYQT5库。  
·服务端为python脚本，需安装python3+，mysql8.0数据库管理系统进行使用，并且建议用python自带的idle运行，而不推荐双击运行脚本，因为双击之后脚本运行之后看不到后台信息    
使用说明：  
1.根目录中有一个chatInfo.txt文件，根据chatInfo.txt创建数据库  
2.运行chatServer.py  
3.运行loginrun.py  
# 运行与测试结果
## （运行打包后的exe）
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
 成功进入登陆界面  
 ![image](https://user-images.githubusercontent.com/50273609/135586401-6bc7d837-3c6a-4f66-9a2b-08e2d0e0d6bf.png)  
 选择好友进行聊天：  
 ![image](https://user-images.githubusercontent.com/50273609/135586447-35af0017-608f-430f-915b-d3ffeaf519f1.png)  
 再登陆一个用户：
 ![image](https://user-images.githubusercontent.com/50273609/135586516-f8d54b87-31cb-4b35-baa3-58e292ece30c.png)  

进行聊天：
 ![image](https://user-images.githubusercontent.com/50273609/135586533-7c3510da-9e5d-42ec-9a69-f2098e096c0d.png)  

与其他人聊天：  
![image](https://user-images.githubusercontent.com/50273609/135586548-0ea43816-5788-4410-867a-63638f1dda3d.png)

 


  




