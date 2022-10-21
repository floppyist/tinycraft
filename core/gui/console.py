import pygame_gui

class Console( pygame_gui.windows.UIConsoleWindow ):
    def __init__( self, rect, manager, window_title ):
        super().__init__( rect, manager, window_title )
