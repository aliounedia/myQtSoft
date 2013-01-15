--------------
Meme si tu es sous Windows, tu peux utiliser des outils 
open source , jusqu'a ce que tu decide de changer ton 
systeme.


C:\>cd C:\Python26\Lib\site-packages\PyQt4\mysoft
C:\Python26\Lib\site-packages\PyQt4>pyuic4 mysoft/mysoft.ui
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 
# 'mysoft/mysoft.ui'
#
# Created: Tue Jan 15 19:34:26 2013
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn = QtGui.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.btn.setObjectName(_fromUtf8("btn"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 110, 256, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
	"MainWindow", "Ma
inWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn.setText(QtGui.QApplication.translate(
		"MainWindow", "Go", None,
QtGui.QApplication.UnicodeUTF8))


----
Le code ci dessus doit etre redirige sous un fichier nomé 
`mysoft.py` , car 'mysoft.ui' est uniquiment du layout , non
exploitable sous python.


---
cree un fichier nome start.py dans ton dossier d'application
mysoft, et mettez le code suivant:


from mysoft import *
import sys
from PyQt4 import QtCore, QtGui

_debug=True

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # `QTCore` utilise les signaux pour activer , 
	# les evenements
        # sur le Widget, I l'image des listeneur sous Java,
        # Add un signal avec ui_object.connect(<ui>,
        #  Signa, whatToDo if signal
        QtCore.QObject.connect(self.ui.btn,
                               QtCore.SIGNAL("clicked()"),
                               self._add)

    

    def _add(self):
        if _debug:
             print>>sys.stdout, "{0}".format( 
             self.ui.lineEdit.text())
            
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())



---
Ensuite vous pouvez lancer votre application avec `python 
start.py` .pour test car l'ojectif est de creer un execu
table dans un envioronnement Window.


---
Telecharger  `py2exe` http://sourceforge.net/projects/py2exe/files/


---
Installer le logiciel 

from distutils.core import setup  
import py2exe

setup(windows=['start.py'],
      options={

# And now, configure py2exe by passing more options;

          'py2exe': {

# This is magic: if you don't add these, your .exe may
# or may not work on older/newer versions of windows.

              "dll_excludes": [
                  "MSVCP90.dll",
                  "MSWSOCK.dll",
                  "mswsock.dll",
                  "powrprof.dll",
                  ],

# Py2exe will not figure out that you need these on its own.
# You may need one, the other, or both.

              'includes': [
                  'sip',
                  'PyQt4.QtNetwork',
                  ],

# Optional: make one big exe with everything in it, or
# a folder with many things in it. Your choice
#             'bundle_files': 1,
          }
      }
      )

python setup.py install

*** binary dependencies ***
Your executable(s) also depend on these dlls which are not included,
you may or may not need to distribute them.

Make sure you have the license if you distribute any of them, and
make sure you don't distribute files belonging to the operating 
system.

   WSOCK32.dll - C:\WINDOWS\system32\WSOCK32.dll
   USER32.dll - C:\WINDOWS\system32\USER32.dll
   ADVAPI32.dll - C:\WINDOWS\system32\ADVAPI32.dll
   SHELL32.dll - C:\WINDOWS\system32\SHELL32.dll
   KERNEL32.dll - C:\WINDOWS\system32\KERNEL32.dll

-Ad











