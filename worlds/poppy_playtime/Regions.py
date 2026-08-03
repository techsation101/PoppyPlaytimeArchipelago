from BaseClasses import Region
from .Types import PoppyPlaytimeLocation
from .Locations import location_table, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import PoppyPlaytimeWorld

def create_regions(world: "PoppyPlaytimeWorld"):
    menu = create_region(world, "Menu")
    chaOne = create_region_and_connect(world, "Chapter 1", "Menu -> Chapter 1", menu)
    chaTwo = create_region_and_connect(world, "Chapter 2", "Menu -> Chapter 2", menu)
    chaThree = create_region_and_connect(world, "Chapter 3", "Menu -> Chapter 3", menu)
    chaFour = create_region_and_connect(world, "Chapter 4", "Menu -> Chapter 4", menu)
    chaFive = create_region_and_connect(world, "Chapter 5", "Menu -> Chapter 5", menu)

    # ---------------------------------- Chapter 1 ----------------------------------
    chaOneLobby = create_region_and_connect(world, "Ch 1 Lobby", "Chapter 1 -> Ch 1 Lobby", chaOne)
    chaOneHuggyRoom = create_region_and_connect(world, "Ch 1 Huggy Room", "Ch 1 Lobby -> Ch 1 Huggy Room", chaOneLobby)
    chaOnePowerRoom = create_region_and_connect(world, "Ch 1 Power Room", "Ch 1 Huggy Room -> Ch 1 Power Room", chaOneHuggyRoom)
    chaOneConveyorBeltRoom = create_region_and_connect(world, "Ch 1 Conveyor Belt Room", "Ch 1 Power Room -> Ch 1 Conveyor Belt Room", chaOnePowerRoom)
    create_region_and_connect(world, "Ch 1 Catwalks", "Ch 1 Conveyor Belt Room -> Ch 1 Catwalks", chaOneConveyorBeltRoom)

    # ---------------------------------- Chapter 2 ------------------------------------------
    #Nothing here yet

def create_region(world: "PoppyPlaytimeWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    for (key, data) in location_table.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = PoppyPlaytimeLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg

def create_region_and_connect(world: "PoppyPlaytimeWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg