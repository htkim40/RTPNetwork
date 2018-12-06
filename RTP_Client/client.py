import socket


class RTPSocket:

    def __init__(self, ipaddress, port):

        self._ip_addr = ipaddress
        self._port = port
        try:
            self._soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self._soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            self._soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
            self._soc.bind(('', self._port)) #'' will be changed to _ip_addr when we dynamically set ip address
        except socket.error as err:
            self._soc = None
            print "Error: " + str(err)

    def listen(self):
        pass

    def connect(self):
        pass

    def txframe(self):
        pass

    def rxframe(self):
        pass

    def close(self):
        self._soc.close()


print "Creating socket"
myclient = RTPSocket('192.168.7.1',5000)
print "Connecting"
myclient.connect()
print "Closing socket"
myclient.close()

