import pygame

from core.manager.spritesheetmanager import SpritesheetManager

class World( pygame.sprite.Sprite ):
    def __init__( self, world_x, world_y, scale ):
        super().__init__()

        # simple map for testing
        # TODO: next step is to convert this into tilesets
        self.world_map = [
            [ 1, 1, 1 ],
            [ 0, 0, 0 ],
            [ 1, 1, 1 ]
        ]

        self.spritesheet = SpritesheetManager( 'sprites/world_grass.png', 16, 16, scale=scale )
        
        # coordinates world_x and world_y are now centers of tiles
        # this allows us to spawn on a given tile (coordinates)
        self.world_x = world_x * self.spritesheet.get_tile_width()  / len( self.world_map ) * scale
        self.world_y = world_y * self.spritesheet.get_tile_height() / len( self.world_map ) * scale

        self.ground_grass = self.spritesheet.get_tile( 8, 3 )
        self.ground_stone = self.spritesheet.get_tile( 2, 8 )

        self.tile_width  = self.spritesheet.get_tile_width()  * scale
        self.tile_height = self.spritesheet.get_tile_height() * scale
    
        self.image = pygame.Surface( ( self.tile_width, self.tile_height ) ).convert_alpha()

        print( self.spritesheet.get_tile_width() )
        print( self.spritesheet.get_tile_height() )

        for x in range( len( self.world_map ) ):
            for y in range( len( self.world_map[x] ) ):
                if self.world_map[y][x] == 1:
                    self.image.blit( self.ground_stone, ( self.spritesheet.get_tile_width() * x, self.spritesheet.get_tile_height() * y ) )
                else:
                    self.image.blit( self.ground_grass, ( self.spritesheet.get_tile_width() * x, self.spritesheet.get_tile_height() * y ) )

        self.rect  = self.image.get_rect()

        # coords for the absolute center
        # TODO: this chaos needs to be fixed
        self.x = ( pygame.display.get_surface().get_width() - self.image.get_width() ) / 2
        self.y = pygame.display.get_surface().get_height() / 2 - self.image.get_height() / len( self.world_map )

    def update( self, movement_scroll_x, movement_scroll_y ):
        self.rect.topleft = [ self.x - self.world_x + movement_scroll_x, self.y + self.world_y + movement_scroll_y ]
