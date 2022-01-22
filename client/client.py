import sys
import socket
import hashlib
import os
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = socket.gethostbyname('ipc_server_dns_name') 
        self.target_port = sys.argv[1] 
        print(self.target_ip,self.target_port)

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def main(self):
        file_name = 'mydata.txt' 
        self.s.send(file_name.encode())
        print(f'Requesting {file_name}')

        confirmation = self.s.recv(1024)
        if confirmation.decode() == "file-doesn't-exist":
            print("File doesn't exist on server.")

            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()

        else:        
            write_name = file_name
            if os.path.exists(write_name): os.remove(write_name)

            with open(write_name,'wb') as file:
                while 1:
                    data = self.s.recv(1024)

                    if not data:
                        break

                    file.write(data)

            print(file_name,'successfully downloaded. Checksum: ', md5("mydata.txt"))

            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            
client = Client()
