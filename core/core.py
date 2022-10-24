import pygame
import pygame_gui

from core.config import config
from core.gui.gui import GUI
from core.player import Player
from core.npc import NPC
from core.direction import Direction
from core.gui.command import Command
from core.world.world import World

class Core:
    def __init__( self ):
        pygame.init()

        # setup pygame objects
        self.clock   = pygame.time.Clock()
        self.display = pygame.display

        # read configuration file
        self.width      = config[ 'screen' ][ 'width' ]
        self.height     = config[ 'screen' ][ 'height' ]
        self.fullscreen = config[ 'screen' ][ 'fullscreen' ]

        # FIXME: need better config processing
        if self.fullscreen:
            arg = pygame.FULLSCREEN
        else:
            # seems a bit hacky to me
            arg = 0

        # initialize configuration to display
        self.screen = self.display.set_mode( ( self.width, self.height ), arg, vsync=1 )

        # add GUI manager
        self.gui_manager = GUI( ( self.width, self.height ) )

        # describes the movement of the player
        # will increased based on [W][A][S][D]-buttons
        self.movement_scroll_x = 0
        self.movement_scroll_y = 0

        # these groups are layered by there initialization
        # TODO: for world building put the drawings before items, characters and so on
        # create sprite array to draw them together
        self.world_sprites  = pygame.sprite.Group()
        self.npc_sprites    = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
 
        # ( 0, 0 ) means the center of the map
        # this value represents the center of the drawed tiles
        self.player = Player( -1, -1 )
        self.player_sprites.add( self.player )

        #self.npc = NPC( 2, 2 )
        #self.npc_sprites.add( self.npc )
        
        self.world = World( self.player.get_world_x(), self.player.get_world_y(), scale=3 )
        self.world_sprites.add( self.world )

        # initialize variable for direction object
        self.direction = Direction

        # different flags for direction-handling
        self.isLeft  = False
        self.isRight = False
        self.isUp    = False
        self.isDown  = False

    # the game loop
    def run( self ):
        while True:
            fps = str( round( self.clock.get_fps() ) )

            # event handling needs a seperate object
            # some basic event handling
            for event in pygame.event.get():
                # check is [CMD] + [Q] was pressed
                if event.type == pygame.QUIT:
                    # if true, leave loop
                    return
                # handler for keydown-events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_HASH:
                        # switch for fps clock
                        if self.gui_manager.fpsclock.visible:
                            self.gui_manager.fpsclock.hide()
                        else:            
                            self.gui_manager.fpsclock.show()
                            
                    if event.key == pygame.K_PLUS:
                        # switch for console
                        # TODO: not finished, console will open with showFPS-flag
                        # FIXME: if console is closed by [x] it will still handled like shown
                        if self.gui_manager.console.visible:
                            self.gui_manager.console.hide()
                        else:
                            self.gui_manager.console.show()
                
                if event.type == pygame_gui.UI_CONSOLE_COMMAND_ENTERED:
                    # TODO: define command handling here
                    print( event.command )

                # after checking necessary events process all gui events
                # must be processed after key events to make console work properly
                self.gui_manager.process_events( event )

            # lock movement if a menu is opened
            if self.gui_manager.isActive():
                # disable animation if menu is shown otherwise opening a menu while an animation
                # is running will still playing these
                self.player.animate( False )
            else:
                # handle hold down key events
                # else will be fired if no menu is opened
                keys = pygame.key.get_pressed()

                if keys[ pygame.K_a ]:
                    self.isLeft = True
                    self.movement_scroll_x += 5
                else:
                    self.isLeft = False

                if keys[ pygame.K_d ]:
                    self.isRight = True
                    self.movement_scroll_x -= 5
                else:
                    self.isRight = False

                if keys[ pygame.K_w ]:
                    self.isUp = True
                    self.movement_scroll_y += 5
                else:
                    self.isUp = False

                if keys[ pygame.K_s ]:
                    self.isDown = True
                    self.movement_scroll_y -= 5
                else:
                    self.isDown = False

                # if no direction-button were pressed, change direction to idle
                if not any( [ self.isLeft, self.isRight, self.isUp, self.isDown ] ):
                    self.direction = Direction.IDLE
                    self.player.animate( False )
                else:
                    self.player.animate( True )

            # FIXME: not very elegant
            # check pressed buttons and select the correct direction
            # needed because northwest, southeast ... should be detected
            if self.isLeft and not self.isUp and not self.isDown and not self.isRight:
                self.direction = Direction.WEST
            if self.isRight and not self.isUp and not self.isDown and not self.isLeft:
                self.direction = Direction.EAST
            if self.isUp and not self.isRight and not self.isDown and not self.isLeft:
                self.direction = Direction.NORTH
            if self.isDown and not self.isRight and not self.isLeft and not self.isUp:
                self.direction = Direction.SOUTH
            if self.isRight and self.isUp and not self.isDown and not self.isLeft:
                self.direction = Direction.NORTHEAST
            if self.isRight and not self.isUp and self.isDown and not self.isLeft:
                self.direction = Direction.SOUTHEAST
            if self.isLeft and self.isUp and not self.isDown and not self.isRight:
                self.direction = Direction.NORTHWEST
            if self.isLeft and not self.isUp and self.isDown and not self.isRight:
                self.direction = Direction.SOUTHWEST

            # set screen background color
            # TODO: need world design
            self.screen.fill( ( 34, 139, 34 ) )

            # draw world first
            self.world_sprites.update( self.movement_scroll_x, self.movement_scroll_y )
            self.world_sprites.draw( self.screen )

            self.npc_sprites.update( self.direction, self.movement_scroll_x, self.movement_scroll_y )
            self.npc_sprites.draw( self.screen )

            # update and draw all sprites in list
            self.player_sprites.update( self.direction )
            self.player_sprites.draw( self.screen )

            # set targeted framerate to 60
            # be careful changing this because all animations are bound to this (!)
            # only use clock.tick once, because clock will not work correctly otherwise
            self.time_delta = self.clock.tick( 60 )

            # update text
            # TODO: this should be done is manager class
            self.gui_manager.fpsclock.set_text( fps )

            # update and draw all ui elements
            self.gui_manager.update( self.time_delta / 1000 )
            self.gui_manager.draw_ui( self.screen )

            # update the whole display
            # the update function also enables us to refresh single rectangles by
            # passing them through arguements
            self.display.update()
