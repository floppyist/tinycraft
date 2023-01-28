import pygame

class SpritesheetManager():
    def __init__( self, spritesheet, columns, rows, scale=1 ):
        self.spritesheet = pygame.image.load( spritesheet )

        # if there is a specific scale given, scale the whole spritesheet
        if scale != 1:
            self.spritesheet = pygame.transform.scale( self.spritesheet, ( self.spritesheet.get_width() * scale, self.spritesheet.get_height() * scale ) )
        
        self.width = self.spritesheet.get_width()
        self.height = self.spritesheet.get_height()
        self.rows = rows
        self.columns = columns

    # simple function which sets a grid based on given rows and
    # columns on the spritesheet and return this specific cell as image
    def get_tile( self, select_x, select_y ):
        # required rect size based on  given rows and columns
        rect_width = self.width / self.columns
        rect_height = self.height / self.rows

        # multiply rect-size with given coordinates to make them selectable
        rect = pygame.Rect( ( select_x * rect_width, select_y * rect_height, rect_width, rect_height ) )

        # create surface for drawing the image
        # flag SRCALPHA have to been set because if using SCALE on display, flag doesn't accept .convert_alpha()
        image = pygame.Surface( rect.size, pygame.SRCALPHA )

        # print the image on the rectangle
        image.blit( self.spritesheet, ( 0, 0 ), rect )

        return image

    # returns the tilewidth in pixels WITH scaling
    def get_tile_width( self ):
        return self.width / self.columns

    # returns the tileheight in pixels WITH scaling
    def get_tile_height( self ):
        return self.height / self.rows