from twisted.internet import protocol, reactor
class BasicServer(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write('server_response:test_key:test_val\r\n')
        n=0
        while n<10:
            n =n + 1
            self.transport.write("%d server_response:test_key:test_val\r\n" % n)
        self.transport.write("%d stop server_response:test_key:test_val\r\n" % n)
        self.transport.loseConnection()
     
class BasicServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return BasicServer()
    
reactor.listenTCP(1234, BasicServerFactory())
reactor.run()
