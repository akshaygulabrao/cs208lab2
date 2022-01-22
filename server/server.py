import socket
import threading
import hashlib
import os
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()
    
    def accept_connections(self):
        ip = socket.gethostbyname('ipc_server_dns_name')
        port = 9898

        self.s.bind((ip,port))
        self.s.listen(100)

        print('Running on IP: '+ip)
        print('Running on port: '+str(port))

        c, addr = self.s.accept()
        print(c)
        threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def handle_client(self,c,addr):
        data = c.recv(1024).decode()
    
        if not os.path.exists(data):
            c.send("file-doesn't-exist".encode())

        else:
            c.send("file-exists".encode())
            print("Checksum: ",md5(data))
            print('Sending',data)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    c.send(data)
                    data = file.read(1024)

                c.shutdown(socket.SHUT_RDWR)
                c.close()
                

server = Server()
