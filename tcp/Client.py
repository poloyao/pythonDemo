import socket

def socket_send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.133',1000))
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