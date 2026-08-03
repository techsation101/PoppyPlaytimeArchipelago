from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import PoppyPlaytimeWorld

def get_total_locations(world: "PoppyPlaytimeWorld") -> int:
    total = 0
    for name in location_table:
        if is_valid_location(world, name):
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

def is_valid_location(world: "PoppyPlaytimeWorld", name) -> bool:
    
    return True

poppy_playtime_locations = {
    "Pickup Green Tape First Room Ch 1": LocData(10001, "Ch 1 Lobby"),
    "Listen to Green Tape First Room Ch 1": LocData(10002, "Ch 1 Lobby"),
    "Enter Train Room Ch 1": LocData(10003, "Ch 1 Lobby"),
    "Enter Grabpack Room Ch 1": LocData(10004, "Ch 1 Lobby"),
    "Pickup Blue Tape Grabpack Room Ch 1": LocData(10005, "Ch 1 Lobby"),
    "Listen to Blue Tape Grabpack Room Ch 1": LocData(10006, "Ch 1 Lobby"),
    "Pickup Grab Pack Ch 1": LocData(10007, "Ch 1 Lobby"),

    "Enter Huggy Room Ch 1": LocData(10008, "Ch 1 Huggy Room"),
    "Pickup Key Huggy Room Ch 1": LocData(10009, "Ch 1 Huggy Room"),

    "Enter Power Room Ch 1": LocData(10010, "Ch 1 Power Room"),
    "Solve Power Room Puzzle Ch 1": LocData(10011, "Ch 1 Power Room"),
    "Enter Factory Room Ch 1": LocData(10012, "Ch 1 Power Room"),
    "Pickup Blue Power Cube Factory Room Ch 1": LocData(10013, "Ch 1 Power Room"),
    "Pickup Yellow Power Cube Factory Room Ch 1": LocData(10014, "Ch 1 Power Room"),
    "Pickup Green Power Cube Factory Room Ch 1": LocData(10015, "Ch 1 Power Room"),
    "Pickup Red Power Cube Factory Room Ch 1": LocData(10016, "Ch 1 Power Room"),
    "Solve Factory Room Puzzle Ch 1": LocData(10017, "Ch 1 Power Room"),
    "Pickup Grab Pack Red Hand Ch 1": LocData(10018, "Ch 1 Power Room"),
    "Pickup Orange Tape Factory Room Ch 1": LocData(10019, "Ch 1 Power Room"),
    "Listen to Orange Tape Factory Room Ch 1": LocData(10020, "Ch 1 Power Room"),
    
    "Enter Conveyor Belt Room Ch 1": LocData(10021, "Ch 1 Conveyor Belt Room"),
    "Solve Conveyor Belt Room Puzzle Ch 1": LocData(10022, "Ch 1 Conveyor Belt Room"),
    "Enter Make a Friend Room Ch 1": LocData(10023, "Ch 1 Conveyor Belt Room"),
    "Pickup Pink Tape Make a Friend Room Ch 1": LocData(10024, "Ch 1 Conveyor Belt Room"),
    "Listen to Pink Tape Make a Friend Room Ch 1": LocData(10025, "Ch 1 Conveyor Belt Room"),
    "Solve Make a Friend Room Puzzle Ch 1": LocData(10026, "Ch 1 Conveyor Belt Room"),
    "Pickup Cat Bee Ch 1": LocData(10027, "Ch 1 Conveyor Belt Room"),

    "Deposit Cat Bee Ch 1": LocData(10028, "Ch 1 Catwalks"),
    "Kill Huggy Ch 1": LocData(10029, "Ch 1 Catwalks"),
    "Enter Catwalks Ch 1": LocData(10030, "Ch 1 Catwalks"),
    "Pickup Gray Tape Catwalks Ch 1": LocData(10031, "Ch 1 Catwalks"),
    "Listen to Gray Tape Catwalks Ch 1": LocData(10032, "Ch 1 Catwalks"),
    "Enter Poppy Room Ch 1": LocData(10033, "Ch 1 Catwalks"),
}

event_locations = {
    "Finish Ch 1": LocData(10034, "Ch 1 Catwalks")
}

location_table = {
    **poppy_playtime_locations,
    **event_locations
}