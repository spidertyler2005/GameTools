import GameTools.Timing as timing
import pygame
#pygame.init()

class Game:
    '''
    The game template for any renderer
    Methods:
      events(dt) -> programmer defined
      update(dt) -> programmer defined
      draw() -> programmer defined
      start() -> programmer defined
      start_GameLoop -> defined but changeable
    '''
    def __init__(self,width,height,title, AnnounceStart = True):
        self.width = width
        self.height = height
        self.title = title
        self.window = None
        self.running = True
        
        if AnnounceStart: print(f"\r\n\r\ngame, {title}, has started")
        self.start_GameLoop()
        
    
    def start(self):
        pass
    
    def draw(self):
        pass
    
    def update(self,dt):
        pass
    
    def events(self,dt):
        pass
    
    def start_GameLoop(self):
        '''
        a method that handles the startup sequence of the gameloop.
		This can be modified for other rendering tools
  		'''
        self.start()
        while self.running:
            timing.DeltaTime.calculate_DeltaTime()
            self.events(timing.deltaTime)
            self.update(timing.deltaTime)
            self.draw()
            
    def draw_Entity(self,entity):
        entity.draw(self)
    
            
class Pygame(Game):
    '''
    The game template for a pygame rendered game
    Methods:
      events(dt) -> programmer defined
      update(dt) -> programmer defined
      draw() -> programmer defined
      start() -> programmer defined
      start_GameLoop -> built-in
      
    '''
    def __init__(self,w,h,title, frameRate = 60, fillColor = (255,255,255), AnnounceStart = True):
        self.width = w
        self.height = h
        self.currentWidth = self.width
        self.currentHeight = self.height
        self.title = title
        self.window = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.frameRate = frameRate
        self.fillColor = fillColor
        self.running = True
        
        if AnnounceStart: print(f"\r\n\r\ngame, {title}, has started")
        self.start_GameLoop()
    
    def start_GameLoop(self):
        '''
        a method that handles the startup sequence of the gameloop.
        this specifically works with pygame rendering.
  		'''
        FF = True
        self.start()
        while self.running:
            self.clock.tick(self.frameRate)
            timing.DeltaTime.calculate_DeltaTime()
            if pygame.event.get(eventtype=pygame.QUIT):
                self.running=False
                continue
            if pygame.event.get(eventtype=pygame.WINDOWRESIZED):
                self.resize()
            self.events(timing.DeltaTime.deltaTime)
            if not FF: 
                self.update(timing.DeltaTime.deltaTime)
            else: FF = False
            self.window.fill(self.fillColor)
            self.draw()
            pygame.display.update()
        pygame.quit()
    
    def resize(self):
        #print(pygame.display.get_window_size())
        self.currentHeight = pygame.display.get_window_size()[1]
        self.currentWidth = pygame.display.get_window_size()[0]