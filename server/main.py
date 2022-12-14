import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import MessageDialog

root = ttk.Window(themename="superhero")

startupmsg = "在使用此程序前，您必须配置您的设备连接到服务端所在的WiFi和一些相关配置。\n " \
             "如果您之前进行了一次有效的配置但仍旧弹出此界面，则表明设备无法连接至您指定的WiFi或产生了致命错误 \n" \
             "\n" \
             "使用以下方法配置你的设备！\n" \
             "①使此电脑连接至你的设备广播热点后重新打开服务端程序，如:ESP8266_RemoteHID_01  \n" \
             "②选择主机设备会在后续中使用的WiFi热点并连接 \n" \
             "③从设备返回的网络信息中检查设备IP网段是否与主机一致 \n" \
             "（可选）指定服务端主机的IP地址 \n"  \
             "④点击上传，设备会重启并连接目标WiFi后与服务端通信 \n" \



root.mainloop()