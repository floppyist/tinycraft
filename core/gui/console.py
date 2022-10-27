import pygame_gui

from core.gui.command import Command
from core.gui.command_description import CommandDescription

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
                    self.add_output_line_to_log( f'player teleported to tile ({tile_x}:{tile_y})' )
                if command == Command.WHERE:
                    ( x, y ) = world.get_current_tile( movement_scroll_x, movement_scroll_y )
                    self.add_output_line_to_log( f'you are now on tile ({x}:{y})' )
                if command == Command.HELP:
                    self.add_output_line_to_log( f'Tinycraft - devTerminal:')
                    for command in Command:
                        self.add_output_line_to_log( f'{command.value} - {CommandDescription[ command.name ].value}' )
        else:
            return
