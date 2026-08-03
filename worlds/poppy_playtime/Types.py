from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Location, Item, ItemClassification

class PoppyPlaytimeLocation(Location):
    game = "Poppy Playtime"

class PoppyPlaytimeItem(Item):
    game = "Poppy Playtime"

# I use these next 2 to convert the number you get from the options into a name
# Mainly used in Items.py for starting chapter
# Not important for a lot of games
class ChapterType(IntEnum):
    ChapterOne = 1
    ChapterTwo = 2
    ChapterThree = 3
    ChapterFour = 4
    ChapterFive = 5

chapter_type_to_name = {
    ChapterType.ChapterOne:  "Chapter 1",
    ChapterType.ChapterTwo:  "Chapter 2",
    ChapterType.ChapterThree:  "Chapter 3",
    ChapterType.ChapterFour:  "Chapter 4",
    ChapterType.ChapterFive:  "Chapter 5",
}

class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: Optional[int] = 1

class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]
