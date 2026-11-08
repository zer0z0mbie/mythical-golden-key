# The Mythical Golden Key

A text-based adventure game for the console, written in Python. Explore 11 rooms, fight enemies, manage your health and stamina, and find the Mythical Golden Key.

Built as coursework for a first-year programming module on my BSc (Hons) Computer Science (University of Essex Online), where it was awarded a Distinction.

## Features

- 11 connected rooms with movement in four directions and an ASCII map showing your position
- Turn-based combat against a random monster and a final boss, with random attack and defence modifiers
- Health and stamina system: moving and attacking cost stamina, and running out of either ends the game
- Inventory with three tiers of health and stamina potions, plus equipment that affects combat
- A puzzle that unlocks a hidden room, a random portal event, and a few other secrets

## What it demonstrates

- **Data structures:** nested dictionaries for rooms, directions, characters, inventory and combat modifiers
- **Functions:** 28 functions with docstrings, including reusable helpers for movement, combat and inventory
- **Control flow:** game loop, room state tracking and multiple win and lose conditions
- **Input validation:** `try`/`except` and conditional checks on every player input
- **Randomness:** the `random` module for enemy selection, loot, combat rolls and portal outcomes
- **Debugging and testing:** edge cases such as an empty inventory, full HP or stamina, and values dropping below zero

## How to run

Requires Python 3. It uses only the standard library, so there's nothing to install.

```bash
git clone https://github.com/matheusmajer/mythical-golden-key.git
cd mythical-golden-key
python mythical_golden_key.py
```

## Example output

```
>< - >< - >< You're in the Main Hall >< - >< - ><

What do you want to do?
(1) Move
(2) View Stats
(3) Check Inventory
(4) Use Items
(5) View Map
Choose an option: 5

    - > - > - > - > - > - > - > - > - > - > - >
    ^                                         '
    '         #########                N      v
    ^         #   .   #                ↑      '
    '         #########             W ← → E   v
    ^                                  ↓      '
    '   #####################          S      v
    ^   #         .         #                 '
    '   #####################                 v
    ^   #     #       #  .  #                 '
    '   #  .  #   .   #######                 v
    ^   #     #       #  .  #                 '
    '   #####################                 v
    ^   #  .  #   X   #  .  #                 '
    '   #####################                 v
    ^      #      .      #                    '
    '      ###############                    v
    ^         #   .   #                       '
    '         #########                       v
    ^                                         '
    - < - < - < - < - < - < - < - < - < - < - <
```

```
Your Turn:
What do you do?
(1) Attack
(2) View Stats
(3) Use Items
Choose an option: 1

You deal 31 damage to Bull Frog.

==================================================
Battle Status:
Your HP: 89/100
Your stamina: 60/100
Bull Frog's HP: 23/75
==================================================
```

## Testing and debugging

I tested the game manually throughout development. I ran individual functions in isolation in IDLE, added temporary `print()` statements to trace values, and stepped through tricky logic with Python Tutor.

Issues I found and fixed during development included:
- the map marking room 11 as "XX" (fixed by switching room labels from numbers to letters)
- HP and stamina showing negative values after big hits
- the secret door's directions not updating after the puzzle was solved
- the console window closing before players could read the ending

## Changes since submission

The first commit is the code exactly as submitted. Later commits are fixes I made afterwards:
- Fixed a bug where cancelling item use in battle caused your next attack to be lost
- Running out of stamina in the Room 3 battle now ends the game immediately
- Minor tidy-ups (unnecessary f-strings, a corrected comment)

## What I learnt

- Planning data structures first made the rest of the game much easier to build
- The hardest bugs were semantic: the code ran, but did the wrong thing
- Testing functions on their own is much faster than replaying the whole game to reach one scenario

## What I'd improve next

- Add automated tests with `pytest` (this needs the game start wrapped in a `main()` function first)
- Replace the 11 similar room functions with one data-driven room handler
- Reduce reliance on global variables, possibly by using classes
- Add a save and load feature