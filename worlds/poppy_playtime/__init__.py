import logging

from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from typing import Dict

from .Locations import get_location_names, get_total_locations
from .Items import create_item, create_itempool, item_table
from .Options import PoppyPlaytimeOptions
from .Regions import create_regions
from .Types import ChapterType, chapter_type_to_name

class PoppyPlaytimeWeb(WebWorld):
    theme = "Party"
    
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Poppy Playtime for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Techsation"]
    )]

class PoppyPlaytimeWorld(World):
    """
    Poppy Playtime, released on Oct 12, 2021, is a horror/puzzle game.
    """

    game = "Poppy Playtime"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()
    options_dataclass = PoppyPlaytimeOptions
    options = PoppyPlaytimeOptions
    web = PoppyPlaytimeWeb()
    
    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def generate_early(self):
        starting_chapter = chapter_type_to_name[ChapterType(self.options.StartingChapter)]

        self.multiworld.push_precollected(self.create_item(starting_chapter))

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)
    
    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "options": {
                "StartingPlace":            self.options.StartingChapter.value,
                "TrapChance":               self.options.TrapChance.value,
                "DarknessTrapWeight":       self.options.DarknessTrapWeight.value
            },
            "Seed": self.multiworld.seed_name,
            "Slot": self.multiworld.player_name[self.player],
            "TotalLocations": get_total_locations(self)
        }

        return slot_data
    
    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)