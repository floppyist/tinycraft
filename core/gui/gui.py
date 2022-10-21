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
        # FIXME: currently the draw_ui function draws all elements
        # TODO: maybe create everything just with hide flag?
        # TODO: create seperate classes, especially for console which will gain a lot of complexity
        self.fpsclock = FPSClock( relative_rect = pygame.Rect( ( 0, 0 ), ( 50, 50 ) ), text='', manager=self )
        self.console = Console( rect = pygame.Rect( ( 0, 30 ), ( 500, 300 ) ), manager=self, window_title='Tinycraft - devTerminal' )
        
        # add all elements to list
        self.ui_elements.append( self.fpsclock )
        self.ui_elements.append( self.console )

        # TODO: maybe better opportunities could arise if object will be more complex
        for element in self.ui_elements:
            element.hide()

    # TODO: why is this function only working correctly if return False is outside of foor loop?
    def isActive( self ):
        for element in self.ui_elements:
            if element.visible == 1:
                pygame.mouse.set_visible( True )
                return True

        pygame.mouse.set_visible( False )
        return False

