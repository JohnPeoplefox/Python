
import sys

from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QGraphicsScene)
from PyQt5.QtCore import Qt, QRectF, QTimer
from PyQt5.QtGui import (
        QBrush, QColor, QPen, QPainter)

from mainwindow import Ui_MainWindow

from simulation import Simulation
from directory import Directory
from schedule import Time
from space import Space
from myagent import MyAgent

from random import randint


class Form(QMainWindow):
    
    
    def __init__(self, parent=None):
        
        super(Form, self).__init__(parent)
        
        self.scale = 6
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.button_start.clicked.connect(
                self.button_start_clicked)
        self.ui.button_stop.clicked.connect(
                self.button_stop_clicked)
        self.ui.button_pause.clicked.connect(
                self.button_pause_clicked)
        self.ui.button_resume.clicked.connect(
                self.button_resume_clicked)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.draw)
        
        self.scene = QGraphicsScene()
        self.ui.display.setScene(self.scene)        
        
        self.width = 100
        self.height = 100
        
        self.space = Space(self.width, self.height)
        self.time = Time()
        self.directory = Directory(self.width, self.height)
        self.directory.running = True
        
        for _ in range(100):
            agent = MyAgent(50, 50, self.space)
            self.directory.add(agent)
        
        self.simulation = Simulation(
                self.space,self.time, self.directory)

        
    
    def button_start_clicked(self):
        
        self.timer.start(100)
        
        
    def button_stop_clicked(self):
        
        self.timer.stop()
        
        
    def button_pause_clicked(self):
        
        self.timer.stop()
        
        
    def button_resume_clicked(self):
        
        self.timer.start(100)
    
        
    def draw(self):
        
        self.scene.clear()
        self.ui.display.viewport().update()

        color = QColor()
        pen = QPen()

        agents = list(self.directory.agents.values())
        for agent in agents:
            
            color.setRed(agent.red)
            color.setGreen(agent.green)
            color.setBlue(agent.blue)
            
            pen.setColor(color)
            
            self.scene.addRect(
            agent.x * self.scale,
            agent.y * self.scale,
            self.scale,
            self.scale,
            pen)
            
            agent.step()




def main():
    
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
