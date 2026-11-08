# =========================
# Modules
# =========================

import random

import math

import string

# =========================
# Game State Variables
# =========================

hidden_room_unlocked = False

monster_fought = None

game_over = False

# Initialises the current room
current_room = 1

# =========================
# Data Structures
# =========================

rooms = {
    "Room Names": {
        1: {
            "Map Coordinate": "a",
            "Room Name": "Entrance Hall",
        },

        2: {
            "Map Coordinate": "b",
            "Room Name": "Lounge Room",
        },

        3: {
            "Map Coordinate": "c",
            "Room Name": "Main Hall",
        },

        4: {
            "Map Coordinate": "d",
            "Room Name": "Study",
        },

        5: {
            "Map Coordinate": "e",
            "Room Name": "Music Room",
        },

        6: {
            "Map Coordinate": "f",
            "Room Name": "Garden of the Dark Thorns",
        },

        7: {
            "Map Coordinate": "g",
            "Room Name": "Abyss of Oblivion",
        },

        8: {
            "Map Coordinate": "h",
            "Room Name": "Bedroom",
        },

        9: {
            "Map Coordinate": "i",
            "Room Name": "Safe Room",
        },

        10: {
            "Map Coordinate": "j",
            "Room Name": "Boss Arena",
        },

        11: {
            "Map Coordinate": "k",
            "Room Name": "Escape Room",
        }
    },

    "Room Descriptions": {
        1: (
            "You find yourself in a small room, feeling consumed by the darkness surrounding you.\n"
            "You cannot lie to yourself:\n"
            "'There is nothing here but... despair,' you think.\n"
            "In the darkness, you notice old furniture and what seems to be a small door."
        ),

        2: (
            "You could swear you have seen bigger rooms before...\n"
            "At this moment, you no longer feel human. You feel like prey waiting to be consumed by the walls slowly closing around you.\n"
            "'I MUST LEAVE THIS PLACE,' you think."
        ),

        3: (
            "A bright and spacious room that once welcomed important figures now stands abandoned, like a bottle drifting across the ocean without a message inside.\n"
            "You look around and realise that, for the first time, you can move in four different directions.\n"
            "The thought alone forces you to consider your next move carefully."
        ),

        4: (
            "A giant dusty writing desk dominates most of the room, both in size and magnificence.\n"
            "Books about strategy, negotiation, and ancient languages fill the bookshelves that still seem to inhale knowledge through the centuries.\n"
            "'How old is this place?' you wonder."
        ),

        5: (
            "For a brief moment, you could swear you hear your favourite piece of music.\n"
            "But it is only the old piano and the other instruments staring silently back at you.\n"
            "Their silent gaze reminds you of better days."
        ),

        6: (
            "Before entering this room, you never imagined you could find life within death.\n"
            "Dark roses stare back at you, their thorns ready to inflict unimaginable pain.\n"
            "Without hesitation, you decide to leave immediately.\n"
            "'Who said flowers were always symbols of peace?' you think."
        ),

        7: (
            "The moment you step inside, your feet touch a dark fog beneath you.\n"
            "The ground suddenly disappears.\n"
            "You fall into the abyss of oblivion.\n"
            "YOU DIE."
        ),

        8: (
            "Dust and emptiness are now the only inhabitants of what once served as someone's bedroom.\n"
            "The bed remains untouched, as though its owner vanished long ago.\n"
            "A strange silence fills the room, making even your breathing feel unnatural."
        ),

        9: (
            "For the first time since arriving in this cursed place, the walls do not feel alive.\n"
            "A faint light illuminates the small room, revealing old emergency supplies scattered across the floor.\n"
            "The heavy metal door behind you shuts slowly, yet instead of fear, you feel something unfamiliar:\n"
            "safety.\n"
            "You sit in silence for a moment, almost forgetting the nightmare waiting outside.\n"
            "'Perhaps even despair grows tired eventually,' you think."
        ),

        10: (
            "The enormous chamber before you resembles less a room and more a forgotten cathedral built for something ancient.\n"
            "Towering pillars disappear into darkness above while the cold air itself feels heavy enough to suffocate you.\n"
            "At the centre of the arena, a lone figure waits motionless.\n"
            "Its presence alone is enough to make your heartbeat lose rhythm.\n"
            "You try to breathe, yet the room itself feels determined to deny you even that.\n"
            "'So this is the source of this nightmare,' you think."
        ),

        11: (
            "A golden light suddenly surrounds your exhausted body.\n"
            "The nightmare around you disappears, replaced by a silent chamber untouched by fear, death, or despair.\n"
            "Ancient walls shimmer faintly as though the room itself has waited centuries for your arrival.\n"
            "At the centre stands a stone pedestal.\n"
            "Upon it rests a single golden key.\n"
            "Not any golden key: the Mythical Golden Key.\n"
            "The moment you take it into your hands, warmth spreads through your body for the first time since entering this cursed place.\n"
            "The darkness no longer calls your name.\n"
            "The nightmare is over."
        )
    },

    "Room Directions": {
        1: {
            "N": {
                "Coordinate": "North",
                "New Room": 2
            }
        },

        2: {
            "N": {
                "Coordinate": "North",
                "New Room": 3
            },
            "S": {
                "Coordinate": "South",
                "New Room": 1
            }
        },

        3: {
            "N": {
                "Coordinate": "North",
                "New Room": 7
            },
            "S": {
                "Coordinate": "South",
                "New Room": 2
            },
            "W": {
                "Coordinate": "West",
                "New Room": 4
            },
            "E": {
                "Coordinate": "East",
                "New Room": 5
            }
        },

        4: {
            "N": {
                "Coordinate": "North",
                "New Room": 6
            },
            "E": {
                "Coordinate": "East",
                "New Room": 3
            }
        },

        5: {
            "N": {
                "Coordinate": "North",
                "New Room": 8
            },
            "W": {
                "Coordinate": "West",
                "New Room": 3
            }
        },

        6: {
            "N": {
                "Coordinate": "North",
                "New Room": 10
            },
            "S": {
                "Coordinate": "South",
                "New Room": 4
            },
            "E": {
                "Coordinate": "East",
                "New Room": 7
            }
        },

        8: {
            "S": {
                "Coordinate": "South",
                "New Room": 5
            },
            "W": {
                "Coordinate": "West",
                "New Room": 7
            }
        },

        "8 Secret Door": {
            "N": {
                "Coordinate": "North",
                "New Room": 9
            },
            "S": {
                "Coordinate": "South",
                "New Room": 5
            },
            "W": {
                "Coordinate": "West",
                "New Room": 7
            }
        },

        9: {
            "N": {
                "Coordinate": "North",
                "New Room": 10
            },
            "S": {
                "Coordinate": "South", "New Room": 8
            },
            "W": {
                "Coordinate": "West",
                "New Room": 7
            }
        },
    },

    "Room Visits": {
        # Room visits initialise at 0 considering the player has not reached those rooms yet
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0
    }
}

characters = {
    "Player Stats": {
        "Health Points": 100,
        "Maximum Health Points": 100,
        "Stamina Points": 100,  # Loses 5 stamina points when moving and 10 when attacking
        "Maximum Stamina Points": 100,
        "Attack Points vs Boss": 0.15,  # 15% multiplier
        "Attack Points vs Monsters": 0.45  # 45% multiplier
    },

    "Enemy Stats": {
        "Monsters": {
            "Monster Type": [
                # Three different monsters exist in the game.
                # One of them spawns randomly in Room 3.
                "Garden Slug",
                "Tokay Gecko",
                "Bull Frog"
            ],
            "Health Points": 75,
            "Maximum Health Points": 75,
            "Attack Points": 0.10  # 10% multiplier
        },

        "Boss": {
            "Health Points": 115,
            "Maximum Health Points": 115,
            "Attack Points": 0.20  # 20% multiplier
        }
    },

    "Modifiers": {
        "Attack Modifiers": {
            -1: 0,
            0: 1,
            1: 1.15,
            2: 1.25,
            3: 1.50,
            4: 2
        },

        "Defence Modifiers": {
            0: 0,
            1: 0.25,
            2: 0.50,
            3: 0.75
        }
    }
}

inventory = {
    # --- Consumables ---
    "Health Potions": {
        "Minor Health Potion": {
            "Quantity": 0,
            "Recovery Points": 0.25  # Weakest health potion: recovers 25% of the maximum HP
        },
        "Major Health Potion": {
            "Quantity": 0,
            "Recovery Points": 0.50  # Regular health potion: recovers 50% of the maximum HP
        },
        "Legendary Health Potion": {
            "Quantity": 0,
            "Recovery Points": 0.75  # Strongest health potion: recovers 75% of the maximum HP
        },
    },
    "Stamina Potions": {
        "Minor Stamina Potion": {
            "Quantity": 0,
            "Recovery Points": 0.25  # Weakest stamina potion: recovers 25% of the maximum stamina points
        },
        "Major Stamina Potion": {
            "Quantity": 0,
            "Recovery Points": 0.50  # Regular stamina potion: recovers 50% of the maximum stamina points
        },
        "Legendary Stamina Potion": {
            "Quantity": 0,
            "Recovery Points": 0.75  # Strongest stamina potion: recovers 75% of the maximum stamina points
        },
    },
    # --- Equipment ---
    "Equipment": {
        "Fire Sword": False,
        "Ice Shield": False
    },
    # --- Miscellaneous ---
    "Map": False,
    "Mini Statue Head": False,
    "Golden Key": False
}


# =========================
# Map
# =========================

def generate_map(current_room):
    """
    Generate the game map with the player's current room marked as 'X'.

    Rooms a–k are replaced with:
    - 'X' for the current room
    - '.' for all other rooms

    All walls and paths remain unchanged.

    Returns:
        str:
            The updated map with the player's position displayed.
    """

    # Takes the current room and returns a map showing the player's position
    current_room_map = ""  # Creates an empty string used to build the updated map

    game_map = """
    - > - > - > - > - > - > - > - > - > - > - >
    ^                                         '
    '         #########                N      v
    ^         #   k   #                ↑      '
    '         #########             W ← → E   v
    ^                                  ↓      '
    '   #####################          S      v
    ^   #         j         #                 '
    '   #####################                 v
    ^   #     #       #  i  #                 '
    '   #  f  #   g   #######                 v
    ^   #     #       #  h  #                 '
    '   #####################                 v
    ^   #  d  #   c   #  e  #                 '
    '   #####################                 v
    ^      #      b      #                    '
    '      ###############                    v
    ^         #   a   #                       '
    '         #########                       v
    ^                                         '
    - < - < - < - < - < - < - < - < - < - < - <
    """

    # Loops through each character in game_map
    for char in game_map:
        # If the character is a room label (a–k), replace it
        if char in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]:
            if char == current_room:
                # Marks the player's current position
                current_room_map += "X"
            else:
                # Marks all other rooms
                current_room_map += "."
        else:
            # Keep walls, paths, and symbols unchanged
            current_room_map += char

    # Return the updated map
    return current_room_map


def view_map(current_room):
    """
    Displays the game map with the player's current position.
    """

    current_room_map_translation = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h",
        "8 Secret Door": "h",
        9: "i",
        10: "j",
        11: "k"
    }

    print(generate_map(current_room_map_translation[current_room]))


# =========================
# Battle Helper Functions
# =========================

def starting_turn(current_enemy):
    """
    Determines who starts the battle.

    The enemy is assigned a random integer from 1 to 20, while the
    player is asked to choose a different integer within the same range.

    After both numbers are selected, one of them is randomly chosen.
    Whoever owns the chosen number takes the first turn in battle.
    """

    while True:
        # Generates a number from 1 to 20
        enemy_pick = random.randint(1, 20)
        player_pick = input("Pick a number from 1 to 20: ")

        # Validates input
        try:
            player_pick = int(player_pick)

            # If both pick the same number, asks the player to pick a different one
            if player_pick == enemy_pick:
                print(f"Same number as {current_enemy}. Pick a different number.")
            # Ensures the number is within range
            elif 1 <= player_pick <= 20:
                break
            else:
                print("Must be a number between 1 and 20.")
        # If the player types anything other than an integer
        except ValueError:
            print("Numbers only.")

    # Randomly selects one of the two numbers
    chosen_number = random.choice([player_pick, enemy_pick])

    print()
    print(
        f"You picked {player_pick}.\n"
        f"{current_enemy} picked {enemy_pick}.\n"
        f"The chosen number is {chosen_number}."
    )

    if chosen_number == player_pick:
        print("You start first.")
        return "Player"

    print(f"{current_enemy} starts first.")
    return current_enemy


def enemy_turn(current_enemy):
    """
    Defines the enemy's turn during battle.

    Enemies can only attack. The function randomly selects an attack
    modifier for the enemy and a defence modifier for the player to
    calculate the total damage dealt.

    If the player has the Ice Shield equipped, part of the damage may
    be absorbed based on the defence modifier.

    Returns:
        int: The total damage dealt to the player.
    """

    # Selects the enemy attack modifier
    enemy_attack_modifier = random.choice(list(characters["Modifiers"]["Attack Modifiers"].values()))

    # Selects the player defence modifier
    player_defence_modifier = random.choice(list(characters["Modifiers"]["Defence Modifiers"].values()))

    if current_enemy == "Boss":
        player_damage_taken = characters["Player Stats"]["Maximum Health Points"] * characters["Enemy Stats"]["Boss"][
            "Attack Points"]
    else:
        player_damage_taken = characters["Player Stats"]["Maximum Health Points"] * \
                              characters["Enemy Stats"]["Monsters"]["Attack Points"]

    # Applies the enemy attack modifier
    player_damage_taken *= enemy_attack_modifier

    # Applies the player defence modifier
    if inventory["Equipment"]["Ice Shield"]:
        player_damage_absorbed = player_damage_taken * player_defence_modifier
    else:
        player_damage_absorbed = 0

    # Calculates the total damage
    total_player_damage_taken = math.floor(player_damage_taken - player_damage_absorbed)

    return total_player_damage_taken


def player_turn(current_enemy):
    """
    Defines the player's turn during battle.

    The player can perform one of the following actions:

    (1) Attack:
        Calculates and returns the damage dealt to the enemy using
        random attack and defence modifiers.

    (2) View Stats:
        Displays the player's current HP and stamina without ending
        the turn.

    (3) Use Items:
        Allows the player to use a consumable item during battle.

    Returns:
        int | None:
            The total damage dealt to the enemy when attacking,
            or None if no attack is performed.
    """

    print(
        "What do you do?\n"
        "(1) Attack\n"
        "(2) View Stats\n"
        "(3) Use Items"
    )

    while True:
        player_turn_action = input("Choose an option: ")

        try:
            player_turn_action = int(player_turn_action)
            if player_turn_action in [1, 2, 3]:
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Numbers only.")

    print()

    # --- (1) Attack ---
    if player_turn_action == 1:
        # Selects the player attack modifier
        player_attack_modifier = random.choice(list(characters["Modifiers"]["Attack Modifiers"].values()))

        # Selects the enemy defence modifier
        enemy_defence_modifier = random.choice(list(characters["Modifiers"]["Defence Modifiers"].values()))

        if current_enemy == "Boss":
            enemy_damage_taken = characters["Enemy Stats"]["Boss"]["Maximum Health Points"] * \
                                 characters["Player Stats"]["Attack Points vs Boss"]
        else:
            enemy_damage_taken = characters["Enemy Stats"]["Monsters"]["Maximum Health Points"] * \
                                 characters["Player Stats"]["Attack Points vs Monsters"]

        # Applies player attack modifier
        enemy_damage_taken *= player_attack_modifier

        # Applies enemy defence modifier
        enemy_damage_absorbed = enemy_damage_taken * enemy_defence_modifier

        # Calculates total enemy damage
        total_enemy_damage_taken = math.floor(enemy_damage_taken - enemy_damage_absorbed)

        return total_enemy_damage_taken

    # --- (2) View Stats ---
    elif player_turn_action == 2:
        view_stats(characters)
        return player_turn(current_enemy)

    # --- (3) Use Items ---
    elif player_turn_action == 3:
        return use_consumable_item(current_enemy)


def battle_status(current_enemy):
    """
    Displays the current battle status, including the player's HP,
    stamina, and the enemy's HP.
    """

    print()
    print("==================================================")
    print("Battle Status:")
    print(
        f"Your HP: "
        f"{characters['Player Stats']['Health Points']}/"
        f"{characters['Player Stats']['Maximum Health Points']}"
    )
    print(
        f"Your stamina: "
        f"{characters['Player Stats']['Stamina Points']}/"
        f"{characters['Player Stats']['Maximum Stamina Points']}"
    )

    if current_enemy == "Boss":
        enemy_stats = characters["Enemy Stats"]["Boss"]
    else:
        enemy_stats = characters["Enemy Stats"]["Monsters"]

    print(
        f"{current_enemy}'s HP: "
        f"{enemy_stats['Health Points']}/"
        f"{enemy_stats['Maximum Health Points']}"
    )
    print("==================================================")
    print()


def total_health_potions():
    """
    Counts the total number of health potions in the player's inventory.

    Returns:
        int: The total number of health potions.
    """

    total_potions = 0

    for item_name, item_quantity in inventory["Health Potions"].items():
        total_potions += item_quantity["Quantity"]

    return total_potions


def total_stamina_potions():
    """
    Counts the total number of stamina potions in the player's inventory.

    Returns:
        int: The total number of stamina potions.
    """

    total_potions = 0

    for item_name, item_quantity in inventory["Stamina Potions"].items():
        total_potions += item_quantity["Quantity"]

    return total_potions


def use_consumable_item(current_enemy=None):
    """
    Allows the player to use consumable items.

    If the player has consumable items available, the function displays
    all usable health and stamina potions and allows one to be used.

    The parameter current_enemy defaults to None so the function can be
    used both inside and outside of battle. During battle, cancelling
    item usage or attempting to use an unavailable item returns the
    player to their turn.

    Returns:
        int | None:
            Returns the result of player_turn() when the
            player returns to the battle menu,
            or None otherwise.
    """

    # Checks the total number of consumable items the player has
    total_consumable_items = total_health_potions() + total_stamina_potions()

    # --- Scenario 1: No consumable items ---
    if total_consumable_items == 0:
        print("You have no consumable items.")
        print()
        # During battle, invalid or cancelled item usage returns the
        # player to their turn without consuming the action.
        if current_enemy is not None:
            return player_turn(current_enemy)

    # --- Scenario 2: Consumable items available ---
    else:
        # Asks the player which item to use
        while True:
            # Initialises a list to track available consumable items
            consumable_item_list = []

            print("Consumable Items:")

            # Displays the health potions currently in the inventory
            for item_name, item_quantity in inventory["Health Potions"].items():
                if item_quantity["Quantity"] > 0:
                    # Adds health potions to the list
                    consumable_item_list.append(item_name)
                    print(f"({consumable_item_list.index(item_name) + 1}) {item_name}: {item_quantity['Quantity']}")

            # Displays the stamina potions currently in the inventory
            for item_name, item_quantity in inventory["Stamina Potions"].items():
                if item_quantity["Quantity"] > 0:
                    # Adds stamina potions to the list
                    consumable_item_list.append(item_name)
                    print(f"({consumable_item_list.index(item_name) + 1}) {item_name}: {item_quantity['Quantity']}")

            # Displays an option to cancel item usage
            print("(0) Cancel")

            item_to_use = input("Choose an item: ")

            # Validates input
            try:
                item_to_use = int(item_to_use)

                if 0 <= item_to_use <= len(consumable_item_list):
                    break
                else:
                    print("Incorrect option.")
                    print()
            except ValueError:
                print("Numbers only.")
                print()

        # Cancels item usage
        if item_to_use == 0:
            print()

            # During battle, invalid or cancelled item usage returns the
            # player to their turn without consuming the action.
            if current_enemy is not None:
                return player_turn(current_enemy)
        # Uses one of the consumable items
        else:
            for consumable_item in consumable_item_list:
                if item_to_use == consumable_item_list.index(consumable_item) + 1:
                    # --- Health potions ---
                    if consumable_item in inventory["Health Potions"]:
                        # Prevent player healing at full HP
                        if characters["Player Stats"]["Health Points"] == characters["Player Stats"][
                            "Maximum Health Points"]:
                            print()
                            print("HP is full, cannot heal.")
                            print()
                            # During battle, invalid or cancelled item usage returns the
                            # player to their turn without consuming the action.
                            if current_enemy is not None:
                                return player_turn(current_enemy)
                        else:
                            # Heals HP
                            characters["Player Stats"]["Health Points"] += math.ceil(
                                characters["Player Stats"]["Maximum Health Points"] *
                                inventory["Health Potions"][consumable_item]["Recovery Points"])
                            inventory["Health Potions"][consumable_item]["Quantity"] -= 1

                            # Prevent HP going above maximum
                            if characters["Player Stats"]["Health Points"] > characters["Player Stats"][
                                "Maximum Health Points"]:
                                characters["Player Stats"]["Health Points"] = characters["Player Stats"][
                                    "Maximum Health Points"]

                            print()
                            print(f"You used a {consumable_item}.")
                            print(
                                f"Your HP is now {characters['Player Stats']['Health Points']}/{characters['Player Stats']['Maximum Health Points']}.")
                            print()

                    # --- Stamina potions ---
                    elif consumable_item in inventory["Stamina Potions"]:
                        # Prevent stamina recovery at full stamina
                        if characters["Player Stats"]["Stamina Points"] == characters["Player Stats"][
                            "Maximum Stamina Points"]:
                            print()
                            print("Stamina is full, cannot recover it.")
                            print()
                            # During battle, invalid or cancelled item usage returns the
                            # player to their turn without consuming the action.
                            if current_enemy is not None:
                                return player_turn(current_enemy)
                        else:
                            # Recovers Stamina
                            characters["Player Stats"]["Stamina Points"] += math.ceil(
                                characters["Player Stats"]["Maximum Stamina Points"] *
                                inventory["Stamina Potions"][consumable_item]["Recovery Points"])
                            inventory["Stamina Potions"][consumable_item]["Quantity"] -= 1

                            # Prevent stamina going above maximum
                            if characters["Player Stats"]["Stamina Points"] > characters["Player Stats"][
                                "Maximum Stamina Points"]:
                                characters["Player Stats"]["Stamina Points"] = characters["Player Stats"][
                                    "Maximum Stamina Points"]

                            print()
                            print(f"You used a {consumable_item}.")
                            print(
                                f"Your stamina is now {characters['Player Stats']['Stamina Points']}/{characters['Player Stats']['Maximum Stamina Points']}.")
                            print()

    return None


def voice_of_the_angels(current_enemy):
    """
    Activates a hidden divine blessing during the boss fight under
    the following conditions:
        - the player is fighting the boss
        - the player's HP is less than or equal to 33
        - the player does not have the Ice Shield
        - the player has no health potions

    Effects:
        - restores the player's HP to either 100 or 80
        - reduces the boss's HP to half of its current value

    The blessing activates automatically when all conditions are met.
    """

    total_health_potions_held = total_health_potions()

    # --- Boss fight condition ---
    if current_enemy == "Boss":
        # --- Low HP condition ---
        if 0 < characters["Player Stats"]["Health Points"] <= 33:
            # --- No Ice Shield condition ---
            if not inventory["Equipment"]["Ice Shield"]:
                # --- No health potions condition ---
                if total_health_potions_held == 0:
                    # --- Restore player HP ---
                    characters["Player Stats"]["Health Points"] = random.choice([100, 80])
                    # --- Reduce boss HP ---
                    characters["Enemy Stats"][current_enemy]["Health Points"] = math.floor(
                        characters["Enemy Stats"][current_enemy]["Health Points"] * 0.50
                    )

                    print()
                    print("Voice of angels activated!")

                    if characters["Enemy Stats"][current_enemy]["Health Points"] <= 0:
                        print(
                            # Description when the boss is defeated
                            f"The voice of the angels was strong enough to reduce the {current_enemy} to dust.\n"
                            f"{current_enemy} collapses before you."
                        )
                        print(
                            "A golden light suddenly surrounds your body.\n"
                            "Before you can react, the arena disappears beneath your feet...\n"
                            "You are suddenly teleported."
                        )
                        print()
                        return 11
                    else:
                        print()
                        print(
                            # Description when the boss survives
                            "A distant choir echoes through the arena.\n"
                            "Warmth suddenly flows through your body as divine light pierces the darkness.\n"
                        )
                        print(
                            f"Your HP: {characters['Player Stats']['Health Points']}/"
                            f"{characters['Player Stats']['Maximum Health Points']}"
                        )
                        print(
                            f"{current_enemy}'s HP: {characters['Enemy Stats'][current_enemy]['Health Points']}/"
                            f"{characters['Enemy Stats'][current_enemy]['Maximum Health Points']}"
                        )


# =========================
# Battle
# =========================

def battle(current_turn, current_enemy, player_name):
    """
    Defines the battle system.

    The function controls the flow of combat between the player
    and either a monster or the boss. It handles turn order,
    damage calculation, stamina consumption, death conditions,
    and battle outcomes.

    Returns:
        int | "Game Over" | "Out of Stamina" | True

            Returns 11 in two situations:
                - Voice of the Angels is activated and defeats the boss
                - The player defeats the boss and is teleported to room 11

            Returns:
                - "Game Over" if the player dies
                - "Out of Stamina" if the player's stamina reaches 0
                - True if a monster is defeated
    """

    print("Battle Begins.")
    print()

    while True:
        # --- Enemy turn ---
        if current_turn == current_enemy:
            if current_enemy == "Boss":
                print(f"{current_enemy}' Turn:")  # Grammar detail ("Boss' Turn" instead of "Boss's Turn")
            else:
                print(
                    f"{current_enemy}'s Turn:")  # Grammar detail ("Monster Name's Turn" instead of "Monster Name' Turn")

            # Calculates damage dealt to the player
            damage_to_player = enemy_turn(current_enemy)

            # Applies damage to the player
            characters["Player Stats"]["Health Points"] -= damage_to_player

            # Prevents the player's HP from dropping below 0
            if characters["Player Stats"]["Health Points"] < 0:
                characters["Player Stats"]["Health Points"] = 0

            print(f"{current_enemy} deals {damage_to_player} damage to you.")

            # Applies Voice of the Angels if activated successfully
            if voice_of_the_angels(current_enemy) == 11:
                return 11

            # If player's HP reaches 0, player dies
            if characters["Player Stats"]["Health Points"] <= 0:
                print(
                    "Your body grows cold.\n"
                    "The darkness consumes you.\n"
                    "YOU DIE."
                )
                print()
                return "Game Over"

            # Switches to the player's turn
            current_turn = player_name

        # If current_turn == player_turn:
        else:
            # --- Player turn ---
            print("Your Turn:")

            # Calculates damage dealt to the enemy
            damage_to_enemy = player_turn(current_enemy)

            # If the player attacked, apply damage to the enemy.
            # damage_to_enemy is None when the player uses an item instead.
            if damage_to_enemy is not None:
                # Maps the current enemy to the correct enemy category.
                # Monster names are stored under the "Monsters" key.
                current_enemy_category = None
                if current_enemy == "Boss":
                    current_enemy_category = "Boss"
                else:
                    current_enemy_category = "Monsters"

                # Applies damage to the enemy
                characters["Enemy Stats"][current_enemy_category]["Health Points"] -= damage_to_enemy

                # Prevents the enemy's HP from dropping below 0
                if characters["Enemy Stats"][current_enemy_category]["Health Points"] < 0:
                    characters["Enemy Stats"][current_enemy_category]["Health Points"] = 0

                # The player loses 10 stamina points per attack
                characters["Player Stats"]["Stamina Points"] -= 10

                # If the player's stamina reaches 0, the player passes out and dies
                if characters["Player Stats"]["Stamina Points"] <= 0:
                    return "Out of Stamina"

                print(f"You deal {damage_to_enemy} damage to {current_enemy}.")

                # If the boss' HP reaches 0, the boss is defeated
                if current_enemy == "Boss":
                    if characters["Enemy Stats"][current_enemy_category]["Health Points"] <= 0:
                        print(f"{current_enemy} collapses before you.")

                        print()
                        print(
                            "A golden light suddenly surrounds your body.\n"
                            "Before you can react, the arena disappears beneath your feet...\n"
                            "You are suddenly teleported."
                        )
                        print()
                        return 11
                else:
                    # If the monster's HP reaches 0, the monster is defeated
                    if characters["Enemy Stats"][current_enemy_category]["Health Points"] <= 0:
                        print(
                            f"{current_enemy} dies and drops a Mini Statue Head.\n"
                            f"You store the item in your bag."
                        )
                        # The monster drops a key item used later in a puzzle
                        inventory["Mini Statue Head"] = True
                        print()
                        return True

            # Switches to the enemy's turn
            current_turn = current_enemy

        # Displays the battle status
        battle_status(current_enemy)


# =========================
# Room Helper Functions
# =========================

def player_location(current_room):
    """
    Displays the player's current location and room description.
    """

    print(f">< - >< - >< You're in the {rooms['Room Names'][current_room]['Room Name']} >< - >< - ><")
    print()
    print(rooms["Room Descriptions"][current_room])
    print()


def room_visit(current_room):
    """
    Tracks and updates the number of visits to the current room.

    Returns:
        int: The current room's visit count.
    """

    rooms["Room Visits"][current_room] += 1
    return rooms["Room Visits"][current_room]


def view_inventory(inventory):
    """
    Displays the player's inventory and available items.
    """

    print("Inventory:")

    # Displays all health potions with a quantity greater than 0
    for item_name, item_quantity in inventory["Health Potions"].items():
        if item_quantity["Quantity"] > 0:
            print(f"- {item_name}: {item_quantity['Quantity']}")

    # Displays all stamina potions with a quantity greater than 0
    for item_name, item_quantity in inventory["Stamina Potions"].items():
        if item_quantity["Quantity"] > 0:
            print(f"- {item_name}: {item_quantity['Quantity']}")

    # Displays all equipped items
    for item_name, item_type in inventory["Equipment"].items():
        if item_type:
            print(f"- {item_name}: 1")

    # Displays the map if the player owns it
    if inventory["Map"]:
        print("- Map: 1")

    # Displays the Mini Statue Head dropped by the monster if obtained
    if inventory["Mini Statue Head"]:
        print("- Mini Statue Head: 1")

    print()


def view_stats(characters):
    """
    Displays the player's current stats in the following formats:
        - HP: Current HP/Maximum HP (e.g., HP: 78/100)
        - Stamina: Current Stamina/Maximum Stamina (e.g., Stamina: 50/100)
    """

    print("Stats:")
    print(f"HP: {characters['Player Stats']['Health Points']}/{characters['Player Stats']['Maximum Health Points']}.")
    print(
        f"Stamina: {characters['Player Stats']['Stamina Points']}/{characters['Player Stats']['Maximum Stamina Points']}.")
    print()


def player_movement(current_room):
    """
    Displays the available movement directions based on
    the player's current room.

    Returns:
        int | "Out of Stamina":
            Returns the next room number if movement succeeds,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    while True:
        print("You can move:")

        # Displays all available directions in the current room
        for direction in rooms["Room Directions"][current_room]:
            print(f"({direction}) {rooms['Room Directions'][current_room][direction]['Coordinate']}")

        # Asks the player which direction they want to move
        coordinate = input("Choose a direction: ").upper()

        # Checks whether the selected direction is valid
        if coordinate in rooms["Room Directions"][current_room]:
            # --- If the player has stamina remaining ---
            if characters["Player Stats"]["Stamina Points"] > 0:
                # Reduces stamina by 5 for each movement
                characters["Player Stats"]["Stamina Points"] -= 5
                # If stamina reaches 0 after moving
                if characters["Player Stats"]["Stamina Points"] <= 0:
                    return "Out of Stamina"
                # If stamina is still above 0 after moving,
                # returns the room number associated with the selected direction
                return rooms["Room Directions"][current_room][coordinate]["New Room"]
            # --- If the player has no stamina remaining ---
            else:
                return "Out of Stamina"
        # If the player enters an invalid direction,
        # display the valid directions again
        else:
            print("Invalid coordinate. Choose between:", end=" ")

            for direction, destination in rooms["Room Directions"][current_room].items():
                print(f"({direction}) {destination['Coordinate']}", end=" ")
            print()

        print()


def room_action(current_room, current_room_visit, characters, inventory):
    """
    Displays the actions the player can perform in the rooms.

    Returns:
        int | "Out of Stamina":
            Returns the next room number if movement succeeds,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    while True:
        # The player has no map during the first room visit,
        # so the map option is unavailable.
        if current_room == 1 and current_room_visit == 1:
            player_action = input(
                "What do you want to do?\n"
                "(1) Move\n"
                "(2) View Stats\n"
                "(3) Check Inventory\n"
                "(4) Use Items\n"
                "Choose an option: "
            )
            print()

        else:
            player_action = input(
                "What do you want to do?\n"
                "(1) Move\n"
                "(2) View Stats\n"
                "(3) Check Inventory\n"
                "(4) Use Items\n"
                "(5) View Map\n"
                "Choose an option: "
            )
            print()

        try:
            player_action = int(player_action)
            if current_room == 1 and current_room_visit == 1:
                if player_action not in [1, 2, 3, 4]:
                    print("Invalid option.")
                    continue
            else:
                if player_action not in [1, 2, 3, 4, 5]:
                    print("Invalid option.")
                    continue
        except ValueError:
            print("Numbers only.")
            continue

        if player_action == 1:
            next_room = player_movement(current_room)
            print()
            return next_room
        elif player_action == 2:
            view_stats(characters)
        elif player_action == 3:
            # The player starts with an empty inventory
            # during the first room visit
            if current_room == 1 and current_room_visit == 1:
                print("Your bag is empty.")
                print()
            else:
                view_inventory(inventory)
        elif player_action == 4:
            use_consumable_item()
        elif player_action == 5:
            view_map(current_room)


# =========================
# Rooms
# =========================

def room_1():
    """
    Starting room of the game.

    This room contains no special events or items.

    Returns:
        int | "Out of Stamina":
            Returns the next room number,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    # --- Tracking Current Room ---
    current_room = 1

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Actions ---
    return room_action(current_room, current_room_visit, characters, inventory)


def room_2():
    """
    Special room where the player obtains two important items:
        - Fire Sword
        - Map

    Returns:
        int | "Out of Stamina":
            Returns the next room number,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    # --- Tracking Current Room ---
    current_room = 2

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Event: Finds a Fire Sword and a Map ---
    if current_room_visit == 1:
        print(
            "You find a Fire Sword and a Map.\n"
            "You feel a momentary glimpse of protection and direction amidst the darkness that devours you..."
        )
        inventory["Equipment"]["Fire Sword"] = inventory["Map"] = True
        print()

    # --- Room Actions ---
    return room_action(current_room, current_room_visit, characters, inventory)


def room_3(player_name):
    """
    Special room containing two major events:

        - A battle against a random monster during the first visit
        - A portal event during the fourth visit, where the player
          chooses between three portals leading to rooms 1, 7, or 10

    Returns:
        "Game Over" | int | "Out of Stamina"

            Returns:
                - "Game Over" if the player dies
                - "Out of Stamina" if the player's stamina reaches 0
                - int representing the next room number
    """

    # --- Tracking Current Room ---
    current_room = 3

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Room Event 1: Random Monster Fight ---
    if current_room_visit == 1:
        global monster_fought

        # Selecting the random monster
        current_enemy = monster_fought = random.choice(characters["Enemy Stats"]["Monsters"]["Monster Type"])

        print(f"You enter the {rooms['Room Names'][current_room]['Room Name']} and {current_enemy} spawns.")
        print()

        # Deciding who starts
        current_turn = starting_turn(current_enemy)

        print()

        battle_outcome = battle(current_turn, current_enemy, player_name)
        if battle_outcome in ("Game Over", "Out of Stamina"):
            return battle_outcome

    # --- Room Event 2: Random Portal to Rooms 1, 7, or 10 ---
    if current_room_visit == 4:
        room_3_portals = {
            "Portal of the Rebirth": {
                "Message": f"You are teleported to the {rooms['Room Names'][1]['Room Name']}.",
                "Outcome": 1
            },
            "Portal of the Death": {
                "Message": f"You are teleported to the {rooms['Room Names'][7]['Room Name']}",
                "Outcome": 7
            },
            "Boss Portal": {
                "Message": f"You are teleported to the {rooms['Room Names'][10]['Room Name']}",
                "Outcome": 10
            },
        }

        print("3 portals spawn in front of you.")

        while True:
            portal_chosen = input("Choose wisely... (L) Left, (M) Middle, or (R) Right: ").lower()
            if portal_chosen not in ["l", "m", "r"]:
                print("Invalid option. Choose between (L), (M), or (R).")
            else:
                break

        print()

        portal_opened = random.choice(list(room_3_portals.keys()))

        portal_names = {
            "l": "left",
            "m": "middle",
            "r": "right"
        }

        print(f"You choose the {portal_names[portal_chosen]} portal and step towards the {portal_opened}.")
        print(room_3_portals[portal_opened]["Message"])
        print()
        return room_3_portals[portal_opened]["Outcome"]

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Actions ---
    return room_action(current_room, current_room_visit, characters, inventory)


def room_4():
    """
    Special room where the player finds a random health potion:
        - Minor Health Potion
        - Major Health Potion
        - Legendary Health Potion

    Returns:
        int | "Out of Stamina":
            Returns the next room number,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    # --- Tracking Current Room ---
    current_room = 4

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Event: Finds a Random Health Potion (Minor, Major, or Legendary) ---
    if current_room_visit == 1:
        print(
            "You see an empty space in one of the bookshelves.\n"
            "Your curiosity calls and you inspect it..."
        )

        health_potion_found = random.choice(list(inventory['Health Potions'].keys()))

        print(f"You found a {health_potion_found}")

        inventory["Health Potions"][health_potion_found]["Quantity"] += 1

        print()

    # --- Room Actions ---
    return room_action(current_room, current_room_visit, characters, inventory)


def room_5():
    """
    Special room where the player finds a random stamina potion:
        - Minor Stamina Potion
        - Major Stamina Potion
        - Legendary Stamina Potion

    Returns:
        int | "Out of Stamina":
            Returns the next room number,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    # --- Tracking Current Room ---
    current_room = 5

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Event: Finds a Random Stamina Potion (Minor, Major, or Legendary) ---
    if current_room_visit == 1:
        print(
            "You notice that one of the piano keys is missing. You look around and fit the missing key.\n"
            "You insert it in the key slot and hear a subtle note... "
        )

        stamina_potion_found = random.choice(list(inventory["Stamina Potions"].keys()))

        print(f"You found a {stamina_potion_found}")

        inventory["Stamina Potions"][stamina_potion_found]["Quantity"] += 1

        print()

    # --- Room Actions ---
    return room_action(current_room, current_room_visit, characters, inventory)


def room_6():
    """
    Regular room with no special events or items.

    Returns:
        int | "Out of Stamina":
            Returns the next room number,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    # --- Tracking Current Room ---
    current_room = 6

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Actions ---
    return room_action(current_room, current_room_visit, characters, inventory)


def room_7():
    """
    Special room containing a fatal pitfall trap.

    Entering this room results in the player's immediate death.
    """

    # --- Tracking Current Room ---
    current_room = 7

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)


def room_8():
    """
    Special room containing the Mini Statue puzzle.

    Solving the puzzle unlocks a hidden path leading to room 9.

    Returns:
        int | "Out of Stamina":
            Returns the next room number,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    # --- Tracking Current Room ---
    current_room = 8
    global hidden_room_unlocked

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Event: Secret Door ---
    if not hidden_room_unlocked:
        while True:
            reveal_room = input(
                "On the nightstand table, you see a mini statue missing the head.\n"
                f"It seems to fit the Mini Statue Head that {monster_fought} dropped.\n"
                "Do you place the head on the statue? (Y/N): "
            ).lower()

            if reveal_room == "y":
                hidden_room_unlocked = True
                inventory["Mini Statue Head"] = False

                print()
                print(
                    "You place the head on the statue and hear a click.\n"
                    "A secret door suddenly appears facing North."
                )
                print()
                break
            elif reveal_room == "n":
                print()
                print("You ignore the statue.")
                print()
                break
            else:
                print("Invalid option. Choose (Y) or (N).")

    # --- Room Actions ---
    if hidden_room_unlocked:
        return room_action("8 Secret Door", current_room_visit, characters, inventory)
    else:
        return room_action(current_room, current_room_visit, characters, inventory)


def room_9():
    """
    Special room where the player obtains the Ice Shield.

    Returns:
        int | "Out of Stamina":
            Returns the next room number,
            or "Out of Stamina" if the player's stamina reaches 0.
    """

    # --- Tracking Current Room ---
    current_room = 9

    # --- Tracking Current Room Visit ---
    current_room_visit = room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Event: Finds an Ice Shield ---
    if current_room_visit == 1:
        print(
            "Your hands are freezing.\n"
            "You find an Ice Shield."
        )
        inventory["Equipment"]["Ice Shield"] = True
        print()

    # --- Room Actions ---
    return room_action(current_room, current_room_visit, characters, inventory)


def room_10(player_name):
    """
    Special room containing four major events:

        - The player's HP and stamina are fully restored
        - The player finds a random health potion:
            - Minor Health Potion
            - Major Health Potion
            - Legendary Health Potion
        - The player finds a random stamina potion:
            - Minor Stamina Potion
            - Major Stamina Potion
            - Legendary Stamina Potion
        - A boss battle

    Returns:
        "Game Over" | int | "Out of Stamina"

            Returns:
                - "Game Over" if the player dies
                - "Out of Stamina" if the player's stamina reaches 0
                - int representing the next room number
    """

    # --- Tracking Current Room ---
    current_room = 10

    # --- Tracking Current Room Visit ---
    room_visit(current_room)

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Event 1: Fully Recovers HP and Stamina ---
    characters["Player Stats"]["Health Points"] = characters["Player Stats"]["Maximum Health Points"]
    characters["Player Stats"]["Stamina Points"] = characters["Player Stats"]["Maximum Stamina Points"]

    print(
        "A faint light surrounds your body.\n"
        "Your wounds disappear.\n"
        "Your HP and stamina are fully recovered."
    )

    print()

    # --- Room Event 2: Finds a Random Health Potion (Minor, Major, or Legendary) ---
    health_potion_found = random.choice(list(inventory['Health Potions'].keys()))
    print(f"You found a {health_potion_found}")
    inventory["Health Potions"][health_potion_found]["Quantity"] += 1

    # --- Room Event 3: Finds a Random Stamina Potion (Minor, Major, or Legendary) ---
    stamina_potion_found = random.choice(list(inventory["Stamina Potions"].keys()))
    print(f"You found a {stamina_potion_found}")
    inventory["Stamina Potions"][stamina_potion_found]["Quantity"] += 1

    print()

    # --- Room Event 4: Boss Fight ---
    current_enemy = "Boss"
    who_starts_the_fight = starting_turn(current_enemy)
    current_turn = who_starts_the_fight

    print()
    battle_outcome = battle(current_turn, current_enemy, player_name)
    return battle_outcome


def room_11():
    """
    Victory room where the player obtains the Mythical Golden Key
    and completes the quest.
    """

    # --- Tracking Current Room ---
    current_room = 11

    # --- Displaying Player Location and Room Description ---
    player_location(current_room)

    # --- Room Event: Finds the Mythical Golden Key ---
    inventory["Golden Key"] = True


# =========================
# Game Starts
# =========================

print()

while True:
    player_name = input("What's your name? ").strip()

    if player_name.replace(" ", "").isalpha():
        break
    else:
        print("Name must contain letters only.")

player_name = string.capwords(player_name)

# =========================
# Welcome Message
# =========================

input(f"""
==================================================

Welcome to the Mythical Golden Key Quest, {player_name}.

Your objective is simple, yet deadly:
find the Mythical Golden Key and escape your nightmare.

To survive, you must explore a series of mysterious rooms,
battle dangerous enemies, and manage your HP and Stamina carefully.

==================================================

Instructions:

- When prompted, type the corresponding key for your chosen action.
- Moving costs 5 Stamina points.
- Attacking costs 10 Stamina points.
- If your HP or Stamina reaches 0, you die.
- You can view your stats during the game by selecting option (2) when available.
- There are 3 potion tiers for restoring HP and Stamina:
    - Minor restores 25%
    - Major restores 50%
    - Legendary restores 75%
- Some rooms contain hidden events, items, or secrets.
- Explore carefully — not every room is safe.

==================================================

Are you ready for this challenge?

Press ENTER to embrace your destiny...
""")  # Once the player presses Enter, the game starts

print(
    f"Good luck, {player_name}.\n"
    f"May the blessings of the Mythical Golden Key smile upon you."
)
print()

# =========================
# Main Game Loop
# =========================

while not game_over:
    if current_room == 1:
        current_room = room_1()
    elif current_room == 2:
        current_room = room_2()
    elif current_room == 3:
        current_room = room_3(player_name)
    elif current_room == 4:
        current_room = room_4()
    elif current_room == 5:
        current_room = room_5()
    elif current_room == 6:
        current_room = room_6()
    elif current_room == 7:
        current_room = room_7()
        # Game Over
        print("Game Over")
        input("\nPress ENTER to close the game.")
        game_over = True
    elif current_room == 8:
        current_room = room_8()
    elif current_room == 9:
        current_room = room_9()
    elif current_room == 10:
        current_room = room_10(player_name)
    elif current_room == 11:
        current_room = room_11()
        # Victory!
        print(
            f"{player_name}, you successfully found the Mythical Golden Key!\n"
            "Victory is yours!"
        )
        print()
        print("Thank you for playing the game.")
        input("\nPress ENTER to close the game.")
        break
    elif current_room == "Game Over":
        # Game Over if player dies
        print("Game Over")
        input("\nPress ENTER to close the game.")
        game_over = True
    elif current_room == "Out of Stamina":
        print(
            "Your legs collapse beneath you.\n"
            "You have completely run out of stamina.\n"
            "Your exhausted body can no longer move.\n"
            "You slowly lose consciousness as the darkness approaches.\n"
            "YOU DIE."
        )
        print()
        print("Game Over")
        input("\nPress ENTER to close the game.")
        game_over = True
    else:
        print("Invalid room.")
        break
