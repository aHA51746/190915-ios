import os
import socket
import sqlite3
import re
#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def sms_db():

    files = ['sms.db','sms.db-shm','sms.db-wal']
    url = 'http://192.168.123.210:9000/private/var/mobile/Library/SMS/'
    for i in files:
        if os.path.exists(i):
            os.remove(i)
        os.system('wget '+url+i)

def get_keycode(data):

    sms_db()
    db = sqlite3.connect('sms.db')
    c = db.cursor()
    sql = 'select text from message'
    text = c.execute(sql)
    all_sms = [i for i in text]
    if data == 'last sms':
        last = all_sms[-1][0]
    elif data == 'key code':
        r = re.compile(r'[0-9]{6,}', re.S)
        last = r.search(all_sms[-1][0]).group()
    db.close()
    return last.encode('utf-8')

def main():

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',9000))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        while True:
            data = conn.recv(1024).decode()
            conn.send(get_keycode(data))
            break
        conn.close()


if __name__ == "__main__":
    main()
