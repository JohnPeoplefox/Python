
from space import Space
from schedule import Time
from agent import Agent
from directory import Directory
from myagent import MyAgent


class Simulation:
    
    def __init__(self, space, time, directory):
        
        self.space = space
        self.time = time
        self.directory = directory
        
        self.running = False
        
        
    def start(self):
        while True:
            self.time.tick(self.directory) 
            
            
    def pause(self):
        self.running = False
        
        
    def resume(self):        
        self.running = True
        
        
    def stop(self):
        
        self.running = False
        self.space = None
        self.time = None
        self.directory = None
        



            
        
def main():
    
    width = 100
    height = 100
    
    space = Space(width, height)
    time = Time()
    directory = Directory(width, height)
    
    for _ in range(100):
        agent = MyAgent(10, 10, space)
        directory.add(agent)
    
    simulation = Simulation(space,time, directory)
    simulation.start()
    
    
if __name__ == '__main__':
    main()
    
    
