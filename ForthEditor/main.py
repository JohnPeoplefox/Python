
import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog)
from PyQt5.QtCore import (
    QProcess, QTextCodec)

from forthedit import Ui_MainWindow
from highlighter import Highlighter



class Editor(QMainWindow):

    def __init__(self, parent=None):

        super(Editor, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        

        self.file_path = None
        self.proc = QProcess()

        Highlighter(self.ui.text_editor)
        
        self.ui.actionRun.triggered.connect(
            self.run_triggered)

        self.ui.actionOpen.triggered.connect(
            self.open_triggered)

        self.ui.actionSave.triggered.connect(
            self.save_triggered)

        self.ui.actionClose.triggered.connect(
            self.close_triggered)

        self.proc.started.connect(
            self.process_started)

        self.proc.errorOccurred.connect(
            self.process_error_occurred)

        self.proc.readyReadStandardOutput.connect(
            self.process_ready_read_standard_output)

        self.proc.finished.connect(
            self.process_finished)

        self.proc.readyReadStandardError.connect(
            self.process_ready_read_standard_error)


    def process_ready_read_standard_error(self):
        self.ui.output.appendPlainText(
            str(QTextCodec.codecForMib(106).toUnicode(
            self.proc.readAllStandardError())))

    def process_finished(self):
        self.ui.output.appendPlainText(
            '\n Process finished ...')

    def process_ready_read_standard_output(self):
        self.ui.output.appendPlainText(
            str(QTextCodec.codecForMib(106).toUnicode(
            self.proc.readAllStandardOutput())))

    def process_error_occurred(self, process_error):
        self.ui.output.appendPlainText(
            str(process_error))
       
    
    def process_started(self):
        self.ui.output.appendPlainText(
            'Process started ...\n')


    def run_forth(self, path=None):
        self.ui.output.setPlainText('')
        self.proc.start('gforth', [path])
        
    def run_triggered(self):
        self.run_forth(self.file_path)


    def save_triggered(self):
        self.save_file()

    def save_file(self):

        text = self.ui.text_editor.toPlainText()
        
        if not self.file_path:
            self.file_path, _ = QFileDialog.getSaveFileName()

        with open(self.file_path, 'w') as f:
            f.write(text)
        
            
    def close_triggered(self):
        self.save_file()
        self.ui.text_editor.setPlainText('')
        


    def open_triggered(self):
        
        self.file_path, _ = QFileDialog.getOpenFileName()

        if self.file_path:
            with open(self.file_path, 'r') as content_file:
                content = content_file.read()

            self.ui.text_editor.setPlainText(content)
            


def main(args):
    
    app = QApplication(args)
    editor = Editor()
    editor.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    
    sys.exit(main(sys.argv))
