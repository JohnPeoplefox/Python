import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel
from PyQt5.QtCore import QDir
from browser import Ui_MainWindow


class MainWindow(QMainWindow):
    
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        path = QDir.currentPath()
        
        self.browser_model = QFileSystemModel()
        self.browser_model.setRootPath(path)
        self.browser_model.setFilter(
            QDir.NoDotAndDotDot | 
            QDir.AllDirs)
            
        self.ui.browser.setModel(self.browser_model)
        
        self.details_model = QFileSystemModel()
        self.details_model.setRootPath(path)
        self.details_model.setFilter(
            QDir.NoDotAndDotDot | 
            QDir.AllEntries)
               
        self.ui.details.setModel(self.details_model)
        
        column_count = self.browser_model.columnCount()
        for i in range(1, column_count):
            self.ui.browser.hideColumn(i)
            
        self.setupUi()
    
            
    def setupUi(self):
        self.ui.browser.clicked.connect(
            self.browser_clicked)
        
    
    def browser_clicked(self, index):

        file_info = self.browser_model.fileInfo(index)
        path = file_info.absoluteFilePath()
        self.ui.details.setRootIndex(
            self.details_model.setRootPath(path))
        

def main(args):
    
    app = QApplication(args)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    sys.exit(main(sys.argv))
