from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in poppy_playtime_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class StartingChapter(Choice):
    """
    Determines which chapter you'll start with.
    Only Chapter 1 works right now
    """
    display_name = "Starting Chapter"
    option_chapter_one = 1
    option_chapter_two = 2
    option_chapter_three = 3
    option_chapter_four = 4
    option_chapter_five = 5
    default = 1

class TrapChance(Range):
    """
    Determines the chance for any junk item to become a trap.
    Set it to 0 for no traps.
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 50

class DarknessTrapWeight(Range):
    """
    The weight of Darkness traps in the item pool
    """
    display_name = "Darkness Trap Weight"
    range_start = 0
    range_end = 100
    default = 100

@dataclass
class PoppyPlaytimeOptions(PerGameCommonOptions):
    StartingChapter:            StartingChapter
    TrapChance:                 TrapChance
    DarknessTrapWeight:         DarknessTrapWeight

poppy_playtime_option_groups: Dict[str, List[Any]] = {
    "General Options": [StartingChapter],
    "Trap Options": [TrapChance, DarknessTrapWeight]
}