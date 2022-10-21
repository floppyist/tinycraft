import pygame
import pygame_gui

from core.gui.fpsclock import FPSClock
from core.gui.console import Console

class GUI( pygame_gui.UIManager ):
    def __init__( self, window_resolution ):
        super().__init__( window_resolution )

        # flag if some UI element is shown, needed to centralize ui controls
        self.isUIShown = False

        # TODO: needs too be much more complex in case of managing and answering requests
        # FIXME: currently the draw_ui function draws all elements
        # TODO: maybe create everything just with hide flag?
        # TODO: create seperate classes, especially for console which will gain a lot of complexity
        #self.lbl_fpsclock = pygame_gui.elements.UILabel( relative_rect = pygame.Rect( ( 0, 0 ), ( 50, 50 ) ), text='', manager=self )
        self.fpsclock = FPSClock( relative_rect = pygame.Rect( ( 0, 0 ), ( 50, 50 ) ), text='', manager=self )
        self.console = Console( rect = pygame.Rect( ( 0, 30 ), ( 500, 300 ) ), manager=self, window_title='Tinycraft - devTerminal' )

        # TODO: maybe better opportunities could arise if object will be more complex
        self.fpsclock.hide()
        self.console.hide()
