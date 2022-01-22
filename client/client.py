import socket
import os

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = socket.gethostbyname('ips_server_dns_name') 
        self.target_port = 9898 
        print(self.target_ip,self.target_port)

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def main(self):
        file_name = 'mydata.txt' 
        self.s.send(file_name.encode())

        confirmation = self.s.recv(1024)
        if confirmation.decode() == "file-doesn't-exist":
            print("File doesn't exist on server.")

            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            self.reconnect()

        else:        
            write_name = 'from_server '+file_name
            if os.path.exists(write_name): os.remove(write_name)

            with open(write_name,'wb') as file:
                while 1:
                    data = self.s.recv(1024)

                    if not data:
                        break

                    file.write(data)

            print(file_name,'successfully downloaded.')

            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            
client = Client()
