# Ce fichier ne sert a rein d'autre qu'a rendre
# ce dossier un module .
from twisted.internet import reactor ,defer
from twisted.protocols import basic 
from twisted.internet.protocol import ClientCreator
from sys import stdout
import time
class Manager(basic.LineOnlyReceiver):

    def __init__(self):
        self.ids = {}
        
    def dataReceived(self, data):
        self.dispatch_incomming(data)
        
    def connectionMade(self):
        #self.test_send()
        #wait simulation
        time.sleep(5)
        self.call_with_key_test()
        
    def test_send(self,message):
        self.transport.write(message)
          
    def call_with_key_test(self , key =None, message =None):
        
         df = defer.Deferred()
         if not key or not message:
             message  ='test_key:test_val'
         else : message  ='%s:%s'%(key, message)
         

         if key in self.ids:
             del self.ids[key]
            
         self.ids['test_key'] =df.callback
         self.test_send(message)
         
               
         # test all methods
         df.addCallbacks(self.process_done)
         
         
    def process_done(self, *args):
        print  'process_done'
        print args
        try:
            del self.ids['test_key']
        except :
            pass
         
    def dispatch_incomming(self, data):
         key = data.split(':')[1]
         df_callback =self.ids.get(key, None)
         df_callback(data)
        

     
creator = ClientCreator(reactor, Manager)
d = creator.connectTCP("localhost", 1234)
reactor.run()
