import pygame

from core.direction import Direction
from core.manager.spritesheetmanager import SpritesheetManager

class Player( pygame.sprite.Sprite ):
    def __init__( self, world_x, world_y, scale=1 ):
        super().__init__()

        self.world_x = world_x
        self.world_y = world_y

        # initialize current spriteset for switching animations
        self.sprites_current = []

        # load spritesheet
        self.spritesheet = SpritesheetManager( 'sprites/player.png', 4, 8, scale=scale )

        self.sprites_idle = []
        self.sprites_idle.append( self.spritesheet.get_tile( 0, 0 ) )

        self.sprites_walk_south = []
        self.sprites_walk_south.append( self.spritesheet.get_tile( 0, 0 ) )
        self.sprites_walk_south.append( self.spritesheet.get_tile( 1, 0 ) )
        self.sprites_walk_south.append( self.spritesheet.get_tile( 2, 0 ) )
        self.sprites_walk_south.append( self.spritesheet.get_tile( 3, 0 ) )

        self.sprites_walk_west = []
        self.sprites_walk_west.append( self.spritesheet.get_tile( 0, 1 ) )
        self.sprites_walk_west.append( self.spritesheet.get_tile( 1, 1 ) )
        self.sprites_walk_west.append( self.spritesheet.get_tile( 2, 1 ) )
        self.sprites_walk_west.append( self.spritesheet.get_tile( 3, 1 ) )

        self.sprites_walk_east = []
        self.sprites_walk_east.append( self.spritesheet.get_tile( 0, 2 ) )
        self.sprites_walk_east.append( self.spritesheet.get_tile( 1, 2 ) )
        self.sprites_walk_east.append( self.spritesheet.get_tile( 2, 2 ) )
        self.sprites_walk_east.append( self.spritesheet.get_tile( 3, 2 ) )

        self.sprites_walk_north = []
        self.sprites_walk_north.append( self.spritesheet.get_tile( 0, 3 ) )
        self.sprites_walk_north.append( self.spritesheet.get_tile( 1, 3 ) )
        self.sprites_walk_north.append( self.spritesheet.get_tile( 2, 3 ) )
        self.sprites_walk_north.append( self.spritesheet.get_tile( 3, 3 ) )

        self.sprites_walk_southeast = []
        self.sprites_walk_southeast.append( self.spritesheet.get_tile( 0, 4 ) )
        self.sprites_walk_southeast.append( self.spritesheet.get_tile( 1, 4 ) )
        self.sprites_walk_southeast.append( self.spritesheet.get_tile( 2, 4 ) )
        self.sprites_walk_southeast.append( self.spritesheet.get_tile( 3, 4 ) )

        self.sprites_walk_southwest = []
        self.sprites_walk_southwest.append( self.spritesheet.get_tile( 0, 5 ) )
        self.sprites_walk_southwest.append( self.spritesheet.get_tile( 1, 5 ) )
        self.sprites_walk_southwest.append( self.spritesheet.get_tile( 2, 5 ) )
        self.sprites_walk_southwest.append( self.spritesheet.get_tile( 3, 5 ) )

        self.sprites_walk_northwest = []
        self.sprites_walk_northwest.append( self.spritesheet.get_tile( 0, 6 ) )
        self.sprites_walk_northwest.append( self.spritesheet.get_tile( 1, 6 ) )
        self.sprites_walk_northwest.append( self.spritesheet.get_tile( 2, 6 ) )
        self.sprites_walk_northwest.append( self.spritesheet.get_tile( 3, 6 ) )

        self.sprites_walk_northeast = []
        self.sprites_walk_northeast.append( self.spritesheet.get_tile( 0, 7 ) )
        self.sprites_walk_northeast.append( self.spritesheet.get_tile( 1, 7 ) )
        self.sprites_walk_northeast.append( self.spritesheet.get_tile( 2, 7 ) )
        self.sprites_walk_northeast.append( self.spritesheet.get_tile( 3, 7 ) )

        # currently there is no idle animation, just one picture, so there is no need
        # to play an animation
        # TODO: create idle animations
        self.is_animating = False
        self.animation_step = 0
        
        # set idle sprite as standard value
        self.sprites_current = self.sprites_idle

        self.image = self.sprites_current[ self.animation_step ]
        self.rect = self.image.get_rect()

        # calculate absolute center
        x = ( ( pygame.display.get_surface().get_width() - self.image.get_width() ) / 2 )
        y = ( ( pygame.display.get_surface().get_height() - self.image.get_height() ) / 2 )

        # positioning rect
        self.rect.topleft = [ x, y ]

    def update( self, direction ):
        if self.is_animating == True:
            # use a low number which will converted to int later which produces the
            # following logic: { 0.x -> 0 | 1.x -> 1 }
            self.animation_step += 0.15
                
            if self.animation_step >= len( self.sprites_current ):
                self.animation_step = 0
            
        if direction == Direction.WEST:
            self.sprites_current = self.sprites_walk_west
        if direction == Direction.EAST:
            self.sprites_current = self.sprites_walk_east
        if direction == Direction.NORTH:
            self.sprites_current = self.sprites_walk_north
        if direction == Direction.SOUTH:
            self.sprites_current = self.sprites_walk_south
        if direction == Direction.NORTHWEST:
            self.sprites_current = self.sprites_walk_northwest
        if direction == Direction.NORTHEAST:
            self.sprites_current = self.sprites_walk_northeast
        if direction == Direction.SOUTHWEST:
            self.sprites_current = self.sprites_walk_southwest
        if direction == Direction.SOUTHEAST:
            self.sprites_current = self.sprites_walk_southeast

        self.image = self.sprites_current[ int( self.animation_step ) ]

    def animate( self, is_animating ):
        self.is_animating = is_animating

        if self.is_animating == False:
            self.animation_step = 0
            self.image = self.sprites_current[ self.animation_step ]

    def get_world_x( self ):
        return self.world_x
    
    def get_world_y( self ):
        return self.world_y