import socket

class RTPClient():
    def __init__(self, ip_addr_in, port_in):
        self.ip_addr = ip_addr_in
        self.port = port_in
        try:
            self.soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            self.soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
            self.soc.bind(('', self.port))
        except socket.error as err:
            self.soc = None
            print "Error: " + str(err)

    def connect(self):
        pass

    def close(self):
        self.soc.close()


print "Creating socket"
myclient = RTPClient('192.168.7.1',5000)
print "Listening"
myclient.connect()
print "Closing socket"
myclient.close()

