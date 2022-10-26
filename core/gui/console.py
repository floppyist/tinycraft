import pygame_gui

from core.gui.command import Command

class Console( pygame_gui.windows.UIConsoleWindow ):
    def __init__( self, rect, manager, window_title ):
        super().__init__( rect, manager, window_title )

        self.blocking = True

    def execute_command( self, cmd, world, movement_scroll_x, movement_scroll_y ):
        cmd = cmd.split()
        
        for command in Command:
            if cmd[0] == command.value:
                if command == Command.TELE:
                    tile_x = int( cmd[1] )
                    tile_y = int( cmd[2] )
                    world.load_at( tile_x, tile_y, movement_scroll_x, movement_scroll_y )
                    self.add_output_line_to_log( f'teleported to tile ({tile_x}:{tile_y})' )
        else:
            return
