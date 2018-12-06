import socket


class RTPSocket:

    def __init__(self, ipAddress, port):

        self._address = ipAddress
        self._port = port
        self._connection = None
        self._clientAddress = None
        try:
            self._soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self._soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            self._soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
            self._soc.bind(('', self._port)) #'' will be changed to _ip_addr when we dynamically set ip address
        except socket.error as err:
            self._soc = None
            print("Error: ", str(err))

    def Listen(self,maxConnections = 1):

        self._soc.listen(maxConnections)
        self._connection, self._clientAddress = self._soc.accept()
        print("Connected to ", self._clientAddress)

    def Connect(self, serverIPAddress, serverPort):

        try:
            if self._soc.connect((serverIPAddress,serverPort)) is None:
                print "Connection to %s::%d failed"%(serverIPAddress,serverPort)

            else:
                print "Connection to %s::%d established"%(serverIPAddress,serverPort)

        except socket.error as err:
            print("Socket error: ", str(err))

    #@Hong Kim or Aaron Allar. to do: Define SendFrame Method
    def SendFrame(self):

        pass

    #@Hong Kim or Aaron Allar. to do: Define SendFrame Method
    def RecvFrame(self):

        pass

    def Close(self):
        self._soc.close()
