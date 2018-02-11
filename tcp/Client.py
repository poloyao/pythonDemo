import socket
import threading

def socket_send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = input('输入ip：')#'192.168.1.198'#input('输入ip：')
    port = input('输入串口:')#'1000'#input('输入串口:')
    #print(port)
    #sock.connect(('192.168.1.13',9090))
    sock.connect((ip,int(port)))
    trd = threading.Thread(target=socketRecvThread,args=(sock,))
    trd.start()
    while True:
        date  = input('input:')
        if date == "exit()":
            break
        sock.send(date.encode())
        # result = sock.recv(1024).decode()
        # print(result)
    sock.close()
# 
#
#
def socketRecvThread(sock):
    while True:
        result = sock.recv(1024).decode()
        print(result)


socket_send()


#{HKEY_CURRENT_USER\Software\MyTest_ChildPlat\ChildPlat}