import pygame
import pygame_gui

class GUI( pygame_gui.UIManager ):
    def __init__( self, window_resolution ):
        super().__init__( window_resolution )

        self.lbl_fpsclock = pygame_gui.elements.UILabel( relative_rect = pygame.Rect( ( 0, 0 ), ( 50, 50 ) ), text="", manager=self )
        self.lbl_fpsclock

    def set_lbl_fpsclock_text( self, text ):
        self.lbl_fpsclock.set_text( text )
