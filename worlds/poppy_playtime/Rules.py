from worlds.generic.Rules import add_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import PoppyPlaytimeWorld

def set_rules(world: "PoppyPlaytimeWorld"):
    player = world.player
    options = world.options

    # Chapter Access
    add_rule(world.multiworld.get_entrance("Menu -> Chapter 1", player),
             lambda state: state.has("Chapter 1", player))
    add_rule(world.multiworld.get_entrance("Menu -> Chapter 2", player),
             lambda state: state.has("Chapter 2", player))
    add_rule(world.multiworld.get_entrance("Menu -> Chapter 3", player),
             lambda state: state.has("Chapter 3", player))
    add_rule(world.multiworld.get_entrance("Menu -> Chapter 4", player),
             lambda state: state.has("Chapter 4", player))
    add_rule(world.multiworld.get_entrance("Menu -> Chapter 5", player),
             lambda state: state.has("Chapter 5", player))
    
    add_rule(world.multiworld.get_entrance("Ch 1 Lobby -> Ch 1 Huggy Room", player),
             lambda state: state.has("Grabpack Ch 1"))
    add_rule(world.multiworld.get_entrance("Ch 1 Huggy Room -> Ch 1 Power Room", player),
             lambda state: state.has("Key Ch 1") and state.has("Grabpack Ch 1"))
    add_rule(world.multiworld.get_entrance("Ch 1 Conveyor Belt Room", "Ch 1 Power Room -> Ch 1 Conveyor Belt Room", player),
             lambda state: state.has("Red Hand Ch 1") and state.has("Key Ch 1") and state.has("Grabpack Ch 1"))
    add_rule(world.multiworld.get_entrance("Ch 1 Conveyor Belt Room -> Ch 1 Catwalks", player),
             lambda state: state.has("Cat Bee Ch 1") and state.has("Red Hand Ch 1") and state.has("Key Ch 1") and state.has("Grabpack Ch 1"))
    
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)