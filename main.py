__author__ = 'jiang'


from twisted.internet import protocol,reactor


class MockFactory(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return MockProtocol()


class MockProtocol(protocol.Protocol):
    def dataReceived(self, data):
        if data == 'quit':
            
            pass
    def connectionLost(self,reson):
        print 'connect lost'

    def connectionMade(self):
        print 'connected'


if __name__ == '__main__':
    reactor.listenTCP(1992,MockFactory())
    reactor.run()