import socket


def client(command):#获取验证码

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',9000))
    client.send(command.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())
    client.close()
    return data.decode()

client('last sms')
