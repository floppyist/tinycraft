import pygame
import pygame_gui

from core.gui.fpsclock import FPSClock
from core.gui.tilecoords import TileCoords
from core.gui.console import Console

class GUI( pygame_gui.UIManager ):
    def __init__( self, window_resolution ):
        super().__init__( window_resolution )

        # load configuration for ui elements
        self.get_theme().load_theme( 'core/gui/gui_config.json' )

        # list of all ui_elements
        self.ui_elements = []

        # TODO: needs too be much more complex in case of managing and answering requests
        self.fpsclock = FPSClock( relative_rect = pygame.Rect( ( 15, 10 ), ( 300, 20 ) ), text='', manager=self )
        self.tilecoords = TileCoords( relative_rect = pygame.Rect( ( 15, 30 ), ( 300, 20 ) ), text='', manager=self )
        self.console = Console( rect = pygame.Rect( ( 0, 50 ), ( 600, 400 ) ), manager=self, window_title='Tinycraft - devTerminal' )

        # add all elements to list
        self.ui_elements.append( self.fpsclock )
        self.ui_elements.append( self.tilecoords )
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

