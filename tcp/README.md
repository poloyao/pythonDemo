# TCP通讯
有阻塞和非阻塞两种模式  
为了避免客户端独占service我没个客户端的连接都建立了一个线程来负责调度。未考虑大量连接出现的并发情况。 

# 引用
与websocket通讯我引用了websocket-client  
```
pip install websocket-client
```