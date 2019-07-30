from game_states import GameStates
from game_messages import Message
from render_functions import RenderOrder

def kill_player(player, dead_color):
    player.char = '@'
    player.color = dead_color

    return Message('You died!', dead_color), GameStates.PLAYER_DEAD

def kill_monster(monster, dead_color, slay_color):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), slay_color)

    monster.char = '%'
    monster.color = dead_color
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message