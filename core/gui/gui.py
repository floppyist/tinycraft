import pygame
import pygame_gui

from core.gui.fpsclock import FPSClock
from core.gui.console import Console

class GUI( pygame_gui.UIManager ):
    def __init__( self, window_resolution ):
        super().__init__( window_resolution )

        # list of all ui_elements
        self.ui_elements = []

        # TODO: needs too be much more complex in case of managing and answering requests
        self.fpsclock = FPSClock( relative_rect = pygame.Rect( ( 0, 0 ), ( 50, 50 ) ), text='', manager=self )
        self.console = Console( rect = pygame.Rect( ( 0, 30 ), ( 500, 300 ) ), manager=self, window_title='Tinycraft - devTerminal' )
        
        # add all elements to list
        self.ui_elements.append( self.fpsclock )
        self.ui_elements.append( self.console )

        # TODO: maybe better opportunities could arise if object will be more complex
        for element in self.ui_elements:
            element.hide()

    # shows or hides the mouse pointer depending on at least one opened ui element
    def isActive( self ):
        for element in self.ui_elements:
            # if selected element is active show mouse pointer
            if element.visible == 1 and element.blocking:
                pygame.mouse.set_visible( True )
                return True

        pygame.mouse.set_visible( False )
        return False

