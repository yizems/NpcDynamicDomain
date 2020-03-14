# NPC 动态ip解决方案

使用前提,需要有一个域名,和知道域名 生效最快的DNS服务器,一般买域名会给2个DNS服务器地址

**只编译了windows 客户端**

## 思路

调用`nslookup`查询域名地址, 查不到继续等待

查到了 执行npc连接,如果连接出错,则 kill npc进程

等待5秒,再查询域名地址,如此循环

## 打包

`pip install PyInstaller`

`PyInstaller -F main.py`


## 使用

### 1 源码编译

### 2 通过命令

`main domain port vkey type dns`

## npc

脚本只是负责调用命令,所以,和`npc` 放在同一目录即可


## NPS 官方网址

[github](https://github.com/ehang-io/nps)


## 备注

本人python贼烂,能用就好=.=,请不要吐糟代码=.=

我没有上传 虚拟环境 ,请自己创建