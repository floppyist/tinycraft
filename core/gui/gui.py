import pygame
import pygame_gui

class GUI( pygame_gui.UIManager ):
    def __init__( self, window_resolution ):
        super().__init__( window_resolution )

        # TODO: needs too be much more complex in case of managing and answering requests
        self.lbl_fpsclock = pygame_gui.elements.UILabel( relative_rect = pygame.Rect( ( 0, 0 ), ( 50, 50 ) ), text='', manager=self )
        self.con_development = pygame_gui.windows.UIConsoleWindow( rect = pygame.Rect( ( 0, 30 ), ( 500, 300 ) ), manager=self, window_title='Tinycraft - devTerminal' )

    def set_lbl_fpsclock_text( self, text ):
        self.lbl_fpsclock.set_text( text )
