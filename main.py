# import pygame module
import pygame
from pygame.locals import *

# define a class object named 'App'
class App:
    # initialize base class 'App'
    def __init__(self):
        # define a variable within the class 'App' named '_running'
        self._running = True
        # define a variable within the class 'App' named '_display_surf'
        self._display_surf = None
        # define a variable within class 'App' named 'size' and assign variables 'weight' and 'height'
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        # initialize all PyGame modules
        pygame.init()
        # create main display window 600x400
        # also attempt to use hardward acceleration
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        # set _running to True to keep game going
        self._running = True

    def on_event(self, event):
        # check event queue for QUIT event
        # if present, set _running == false to break game loop
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        # quit all pygame modules
        # python cleans remaining modules
        pygame.quit()

    def on_execute(self):
        # initialize pygame, then enter main loop
        # in which check events and compute and render
        if self.on_init() == False:
            self._running == False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()