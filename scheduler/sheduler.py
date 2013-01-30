from datetime import datetime, timedelta
from apscheduler.scheduler import Scheduler
from apscheduler.jobstores.mongodb_store import MongoDBJobStore
from BaseHTTPServer  import BaseHTTPRequestHandler , HTTPServer
from datetime  import datetime
import os , sys
import thread
__author__ = "Alioune Dia"
___date__  = "2013-01-30"

def a_job_for_test(*args ):
    
    # Cette fonction ne fait que
    if os.path.exists('run_verification.txt'):
        os.remove('run_verification.txt')
    with open('run_verification.txt', 'wb') as f:
        f.write('The  a_job_for_test  is running' )
        f.write('The  a_job_for_test args ' % args)

    # Ici , libre au developpeur d' y mettre des taches
    # qui seront pris en compte par le sheduler, lorsque des
    # problemes de ressources /db, acces fichiers / empeche
    # le traitement , la demande du client n'est pas bloquee
    # cela permet au client de continue d'autres traiements

class ShedulerServer(HTTPServer):
      def set_sheduler(self, sheduler):
          self.sheduler = sheduler

      
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    """Simple HTTP request handler with GET and HEAD commands.

    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method.

    The GET and HEAD requests are identical except that the HEAD
    request omits the actual contents of the file.

    """

    server_version = "SimpleHTTP/0.1" 

    def do_GET(self):
        """Serve a GET request."""
        # f = self.send_head()
        # if f:
        # self.copyfile(f, self.wfile)
        # f.close()
        print self.path 
        
        if not self.server.sheduler:
            f.write("Sheduler not running")
            return
        args  =self.path
        print "args", args
        print  'sheduler', self.server.sheduler
        # Ceci est juste un test que ajoute un job sur le sheduler(
        # un job en duren -a_job_for_test, mais on aurait pu imaginer*
        # un truc plus generic , ou la method en question a executee
        # est passe par la requete Http.
        now = datetime.now() + timedelta(seconds=10)

        # comme un 'cron' , voici une facon de scecifier au sheduler
        # un job a effctue tous le trois secondes:) .Note que dans
        # l'exemple la fonction 'a_job_for_test' est juste
        # un exemple , mais nous aurions pu aussi bien imaginer que
        # le nom de la fonction est passe au serveur via Http
        # un truc du genre self.path.split('')
        self.server.sheduler.scheduler.add_interval_job(
                                   a_job_for_test,
                                   seconds=3,
                                   name='a_job_for_test',
                                   jobstore='MongoDB',
                                   args=[now])

        # comme un 'cron' , voici une facon de scecifier au sheduler
        # un job a effctued dans 10 secondes un seule fois.Note que dans
        # l'exemple  la fonction 'a_job_for_test' est juste
        # un exemple , mais nous aurions pu aussi bien imaginer que
        # le nom de la fonction est passe au serveur via Http
        # un truc du genre self.path.split('')
        
        # self.server.sheduler.scheduler.add_date_job(a_job_for_test,
        #                           now,
        #                           name='a_job_for_test',
        #                           jobstore='MongoDB',
        #                           args=[now])
        thread.start_new_thread(
            self.server.sheduler.scheduler.start, ())
        
      
class Sheduler:
    def __init__(self):
        self.scheduler = Scheduler(standalone=True)
        self.scheduler.add_jobstore(MongoDBJobStore('mesjobs'),
                                    'MongoDB')

    def start(self):
        print('Starting the sheduler')
        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass

# Vous pouver demarrer le sheduler depuis sur la console
# ,le sheduler va demarrer en meme temps que le server
# Http qui va  se mettre en attente d'une requete pour
# passation au sheduler
# test:
# On peut tester en utlisant curl ou bien un navigateur
# 10.11.4.56:32/plop?foo=bar

if __name__ == "__main__":
    server_address = ('', 32)
    sh_server= ShedulerServer(server_address, SimpleHTTPRequestHandler)
    sh_server.set_sheduler(Sheduler())
    print sh_server.__dict__
    sh_server.sheduler.start()
    sh_server.sheduler.is_running = True 
    print("Starting Http Server on %s %s", server_address)
    try:
        sh_server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sh_server.server_close()
        sys.exit(0)
