import pygame

from core.config import config
from core.player import Player
from core.direction import Direction

class Core:
    def __init__( self ):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.display = pygame.display

        self.width = config[ 'screen' ][ 'width' ]
        self.height = config[ 'screen' ][ 'height' ]
        self.fullscreen = config[ 'screen' ][ 'fullscreen']

        # FIXME: need better config processing
        if self.fullscreen:
            arg = pygame.FULLSCREEN
        else:
            # seems a bit hacky to me
            arg = 0

        self.screen = self.display.set_mode( ( self.width, self.height ), arg )

        # describes the movement of the player
        # will increased based on [W][A][S][D]-buttons
        self.movement_scroll_x = 0
        self.movement_scroll_y = 0

        # create sprite array to draw them together
        self.mov_sprites = pygame.sprite.Group()

        # create player at { 0, 0 }
        # { 0, 0 } means the center
        self.player = Player( 0, 0 )
        self.mov_sprites.add( self.player )

        # initialize variable for direction object
        self.direction = Direction

        # different flags for direction-handling
        self.isLeft = False
        self.isRight = False
        self.isUp = False
        self.isDown = False

    # the game loop
    def run( self ):
        while True:
            # some basic event handling
            for event in pygame.event.get():
                # check is [CMD] + [Q] was pressed
                if event.type == pygame.QUIT:
                    # if true, leave loop
                    return

            # handle hold down key events
            # else will be fired every time the key isn't pressed
            # makes the controls feel soft
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

            # if no direction-button is pressed, change direction to idle
            if not any( [ self.isLeft, self.isRight, self.isUp, self.isDown ] ):
                self.direction = Direction.IDLE
                self.player.animate( False )
            else:
                self.player.animate( True )

            # FIXME: not very elegant
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

            # draw all sprites which are part of the array
            self.mov_sprites.draw( self.screen )

            # update player animation
            self.mov_sprites.update( self.direction, self.movement_scroll_x, self.movement_scroll_y )

            # update the whole display
            self.display.flip()

            # set targeted framerate to 60
            # be careful changing this because all animations are bound to this (!)
            self.clock.tick( 60 )