import logging

from BaseClasses import Item, ItemClassification

from .Types import ItemData, ChapterType, PoppyPlaytimeItem, chapter_type_to_name
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import PoppyPlaytimeWorld

def create_itempool(world: "PoppyPlaytimeWorld") -> List[Item]:
    itempool: List[Item] = []

    starting_chapter = chapter_type_to_name[ChapterType(world.options.StartingChapter)]

    for chapter in poppy_playtime_chapters.keys():
        print("-------------------------")
        print(starting_chapter)
        print("-------------------------")
        if starting_chapter == chapter:
            continue
        else:
            itempool.append(create_item(world, chapter))

    
    for item in poppy_playtime_item.keys():
        if item == "Victory":
            continue
        else:
            itempool.append(create_item(world, item))
    
    # CHANGE VICTORY LOCATION
    victory = create_item(world, "Victory")
    world.multiworld.get_location("Finish Ch 1", world.player).place_locked_item(victory)

    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)

    return itempool

def create_item(world: "PoppyPlaytimeWorld", name: str) -> Item:
    data = item_table[name]
    return PoppyPlaytimeItem(name, data.classification, data.ap_code, world.player)

def create_multiple_items(world: "PoppyPlaytimeWorld", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [PoppyPlaytimeItem(name, item_type, data.ap_code, world.player)]

    return itemlist

def create_junk_items(world: "PoppyPlaytimeWorld", count: int) -> List[Item]:
    trap_chance = world.options.TrapChance.value
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    trap_list: Dict[str, int] = {}

    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

        elif trap_chance > 0 and ic == ItemClassification.trap:
            if name == "Darkness Trap":
                trap_list[name] = world.options.DarknessTrapWeight.value

    for i in range(count):
        if trap_chance > 0 and world.random.randint(1, 100) <= trap_chance:
            junk_pool.append(world.create_item(
                world.random.choices(list(trap_list.keys()), weights=list(trap_list.values()), k=1)[0]))
        else:
            junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

poppy_playtime_items = {
    # Progression items
    "Grabpack Ch 1": ItemData(50001, ItemClassification.progression),
    "Key Ch 1": ItemData(50002, ItemClassification.progression),
    "Red Hand Ch 1": ItemData(50003, ItemClassification.progression),
    "Cat Bee Ch 1": ItemData(50004, ItemClassification.progression),

    "Victory": ItemData(50007, ItemClassification.progression)
}

poppy_playtime_chapters = {
    "Chapter 1": ItemData(50008, ItemClassification.progression),
    "Chapter 2": ItemData(50009, ItemClassification.progression),
    "Chapter 3": ItemData(50010, ItemClassification.progression),
    "Chapter 4": ItemData(50011, ItemClassification.progression),
    "Chapter 5": ItemData(50012, ItemClassification.progression)
}

junk_items = {
    # Junk
    "Limon Piece": ItemData(50005, ItemClassification.filler, 0),
    "Poppy": ItemData(50006, ItemClassification.filler, 0),

    # Traps
    "Darkness Trap": ItemData(50013, ItemClassification.trap, 0)
}

junk_weights = {
    "Limon Piece": 75,
    "Poppy": 25
}

item_table = {
    **poppy_playtime_items,
    **poppy_playtime_chapters,
    **junk_items
}