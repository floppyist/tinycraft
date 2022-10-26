import pygame_gui

from core.gui.command import Command

class Console( pygame_gui.windows.UIConsoleWindow ):
    def __init__( self, rect, manager, window_title ):
        super().__init__( rect, manager, window_title )

        self.blocking = True

    def execute_command( self, cmd, world ):
        cmd = cmd.split()
        
        for command in Command:
            if cmd[0] == command.value:
                world.load_at( int(cmd[1]), int(cmd[2]) )
                self.add_output_line_to_log( 'executed' )
        else:
            return
