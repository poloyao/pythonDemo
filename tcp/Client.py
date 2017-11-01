import socket

def socket_send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = input('输入ip：')
    port = input('输入串口:')
    #print(port)
    #sock.connect(('192.168.1.13',2111))
    sock.connect((ip,int(port)))
    while True:
        date  = input('input:')
        if date == "exit()":
            break
        sock.send(date.encode())
        result = sock.recv(1024).decode()
        print(result)
    sock.close()

socket_send()


#{HKEY_CURRENT_USER\Software\MyTest_ChildPlat\ChildPlat}