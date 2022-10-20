#!/usr/bin/env python3.10

import pygame

from core.config import config
from core.player import Player
from core.direction import Direction

# FIXME: testing only
font = str()

def update_fps( clock ):
    fps = str( int( clock.get_fps() ) )
    fps_text = font.render( fps, 1, pygame.Color( 'black' ) )
    return fps_text

def main():
    # TODO: gather informations on how it works exactly
    clock  = pygame.time.Clock()

    # whole display object
    display = pygame.display

    # add main surface object
    #screen = display.set_mode( ( 1280, 720 ), pygame.FULLSCREEN )

    if config[ 'screen' ][ 'fullscreen' ]:
        arg = pygame.FULLSCREEN
    else:
        arg = 0

    screen = display.set_mode( ( config[ 'screen' ][ 'width' ], config[ 'screen' ][ 'height' ] ), arg )

    # relative movement for all but player
    movement_scroll_x = 0
    movement_scroll_y = 0

    # FIXME: placed only for testing reasons
    mov_sprites = pygame.sprite.Group()

    player = Player( 0, 0 )
    mov_sprites.add( player )

    direction = Direction

    isLeft  = False
    isRight = False
    isUp    = False
    isDown  = False

    # game loop
    while True:
        # some basic event handling
        for event in pygame.event.get():
            # check is [CMD] + [Q] was pressed
            if event.type == pygame.QUIT:
                # if true, leave loop
                return

        # handle hold down key events
        # else will handle button released events
        keys = pygame.key.get_pressed()

        if keys[ pygame.K_a ]:
            isLeft = True
            movement_scroll_x += 5
        else:
            isLeft = False

        if keys[ pygame.K_d ]:
            isRight = True
            movement_scroll_x -= 5
        else:
            isRight = False

        if keys[ pygame.K_w ]:
            isUp = True
            movement_scroll_y += 5
        else:
            isUp = False

        if keys[ pygame.K_s ]:
            isDown = True
            movement_scroll_y -= 5
        else:
            isDown = False

        if not any( [ isLeft, isRight, isUp, isDown ] ):
            direction = Direction.IDLE
            player.animate( False )
        else:
            player.animate( True )

        if isLeft and not isUp and not isDown and not isRight:
            direction = Direction.WEST
        if isRight and not isUp and not isDown and not isLeft:
            direction = Direction.EAST
        if isUp and not isRight and not isDown and not isLeft:
            direction = Direction.NORTH
        if isDown and not isRight and not isLeft and not isUp:
            direction = Direction.SOUTH
        if isRight and isUp and not isDown and not isLeft:
            direction = Direction.NORTHEAST
        if isRight and not isUp and isDown and not isLeft:
            direction = Direction.SOUTHEAST
        if isLeft and isUp and not isDown and not isRight:
            direction = Direction.NORTHWEST
        if isLeft and not isUp and isDown and not isRight:
            direction = Direction.SOUTHWEST

        # set screen background color
        screen.fill( ( 34, 139, 34 ) )

        # draw player sprite
        mov_sprites.draw( screen )

        # update player animation
        mov_sprites.update( direction, movement_scroll_x, movement_scroll_y )

        # draw fps-clock
        screen.blit( update_fps( clock ), ( 10, 0 ) )

        # update the whole display
        display.flip()

        # set targeted framerate to 60
        # be careful changing this because all animations are bound to this (!)
        clock.tick( 60 )

    return

if __name__ == '__main__':
    pygame.init()
    font = pygame.font.SysFont( 'Courier', 24, bold=True )
    main()
