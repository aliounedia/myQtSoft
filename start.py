# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mysoft/mysoft.ui'
#
# Created: Tue Jan 15 19:35:55 2013
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from mysoft import *
import sys
from PyQt4 import QtCore, QtGui

_debug=True

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # `QTCore` utilise les signaux pour activer , les evenements
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
