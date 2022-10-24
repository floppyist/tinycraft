import pygame

from core.manager.spritesheetmanager import SpritesheetManager

class World( pygame.sprite.Sprite ):
    def __init__( self, world_x, world_y, scale ):
        super().__init__()

        self.scale = scale

        self.spritesheet = SpritesheetManager( 'sprites/world_grass.png', 16, 16 )
        
        self.world_x = world_x
        self.world_y = world_y

        self.image = self.spritesheet.get_tile( 0, 8 )
        self.image = pygame.transform.scale( self.image, ( self.spritesheet.get_tile_width() * scale, self.spritesheet.get_tile_height() * scale ) )
        self.rect  = self.image.get_rect()

        # coords for the absolute center
        self.x = ( ( pygame.display.get_surface().get_width() - self.image.get_width() ) / 2 )
        self.y = ( ( pygame.display.get_surface().get_height() ) / 2 )

    def update( self, movement_scroll_x, movement_scroll_y ):
        self.world_x = self.world_x + self.spritesheet.get_tile_width()
        self.world_y = self.world_y + self.spritesheet.get_tile_height()
        self.rect.topleft = [ self.x - self.world_x + movement_scroll_x, self.y + self.world_y + movement_scroll_y ]
