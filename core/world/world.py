import pygame
import random
import numpy as np

from core.manager.spritesheetmanager import SpritesheetManager

class World( pygame.sprite.Sprite ):
    def __init__( self, world_x, world_y, scale=1 ):
        super().__init__()

        MAP_WIDTH  = 11
        MAP_HEIGHT = 11

        # TODO: next step is to convert this into tilesets
        self.world_map = np.random.randint( 3, size=( MAP_WIDTH, MAP_HEIGHT ) )

        self.spritesheet = SpritesheetManager( 'sprites/world_grass.png', 16, 16, scale=scale )
        
        # coordinates world_x and world_y are now centers of tiles
        # this allows us to spawn on a given tile (coordinates)

        self.world_x = world_x * self.spritesheet.get_tile_width()
        self.world_y = world_y * self.spritesheet.get_tile_height()

        self.ground_grass  = self.spritesheet.get_tile( 8, 3 )
        self.ground_stone0 = self.spritesheet.get_tile( 5, 8 )
        self.ground_stone1 = self.spritesheet.get_tile( 1, 4 )

        self.tile_width  = self.spritesheet.get_tile_width() * scale
        self.tile_height = self.spritesheet.get_tile_height() * scale
    
        self.image = pygame.Surface( ( self.spritesheet.get_tile_width() * len( self.world_map ), self.spritesheet.get_tile_height() * len( self.world_map ) ) ).convert_alpha()

        for x in range( len( self.world_map ) ):
            for y in range( len( self.world_map ) ):
                if self.world_map[y][x] == 1:
                    self.image.blit( self.ground_stone0, ( self.spritesheet.get_tile_width() * x, self.spritesheet.get_tile_height() * y ) )
                elif self.world_map[y][x] == 2:
                    self.image.blit( self.ground_stone1, ( self.spritesheet.get_tile_width() * x, self.spritesheet.get_tile_height() * y ) )
                else:
                    self.image.blit( self.ground_grass, ( self.spritesheet.get_tile_width() * x, self.spritesheet.get_tile_height() * y ) )

                # draw grid
                pygame.draw.rect( self.image, ( 0, 0, 0 ), ( 0, 0, self.spritesheet.get_tile_width() * ( x + 1 ), self.spritesheet.get_tile_height() * ( y + 1 ) ), 1 )

        # needed for parent class (like image)
        self.rect  = self.image.get_rect()

        # coords for the absolute center
        # TODO: this chaos needs to be fixed
        self.x = ( pygame.display.get_surface().get_width()  - self.image.get_width() )  / 2
        self.y = ( pygame.display.get_surface().get_height() - self.image.get_height() ) / 2 + self.spritesheet.get_tile_height() / 2

    def update( self, movement_scroll_x, movement_scroll_y ):
        self.rect.topleft = [ self.x - self.world_x + movement_scroll_x, self.y + self.world_y + movement_scroll_y ]
