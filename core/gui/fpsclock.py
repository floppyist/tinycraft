import pygame_gui

class FPSClock( pygame_gui.elements.UILabel ):
    def __init__( self, relative_rect, text, manager ):
        super().__init__( relative_rect, text, manager )
