import pygame

class NPC( pygame.sprite.Sprite ):
    def __init__( self, pos_x, pos_y ):
        super().__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprites_walk_W = []
        self.sprites_walk_W.append( pygame.image.load( 'sprites/norah/norah_walk_E_01.png' ) )

        self.image = self.sprites_walk_W[ 0 ]
        self.rect = self.image.get_rect()
        self.rect.topleft = [ pos_x, pos_y ]

    def update( self, direction, movement_scroll_x, movement_scroll_y ):
        self.rect.topleft = [ self.pos_x + movement_scroll_x, self.pos_y + movement_scroll_y ]

    def get_rect( self ):
        return self.rect