from enum import Enum

class CommandDescription( Enum ):
    TELE  = 'Teleports the player to given coordinates.'
    WHERE = 'Shows current tile player is standing.'
    HELP  = 'Shows this help page.'