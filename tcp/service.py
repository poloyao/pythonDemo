import sys
import socket
import threading
import time

def rec(sock,addr):
    while True:
        try:
            ret = sock.recv(2048).decode()
            print(addr[0] + ":" + str(addr[1]) + "---" + ret)
            sock.send(ret.encode())
            if ret== 'exit':
                sock.close()
                break
        except:
            print("close")
            break

 
def work():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('0.0.0.0',1000))
    sock.listen(5)
    while True:
        time.sleep(1)
        try:
            conn,addr = sock.accept()
            trd = threading.Thread(target=rec,args=(conn,addr))
            trd.start()                
        except:
            #print(sys.exc_info()[0])
            #print(addr[0] + ":" + str(addr[1]))
            #sys.exit(0)
            print("work---Close")
    sock.close()
 
if __name__ == '__main__':
    work()