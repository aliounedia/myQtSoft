from twisted.internet import protocol, reactor

class BasicServer(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write('server_response:'+ data)
        self.transport.loseConnection()

class BasicServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return BasicServer()
    
reactor.listenTCP(1234, BasicServerFactory())
reactor.run()
