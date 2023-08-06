import random
import yaml
import pickle

# varibles
# room1x = random.randint

# says you are not playing.
play = 0

# opens "save.yaml"
# with open("save.yaml") as f:
#     player = yaml.safe_load(f)

# asks you if you want to continue or start over
create_save = input(
    "Do you want to [c]ontinue saved game or create [n]ew game?")

if create_save.lower().startswith('n'):
    delsave = input("This will delete all data. Continue? Y/N ")
    if delsave.lower().startswith('y'):
        save_name = input("Please name your save (make sure you add .yaml to the end): ")
        player = {
            "health":10,
            "max health":10,
            "x":0,
            "y":0,
            "inventory":["Sword", "Healing Potion"],
            "held item":"Sword",
            "cheat":0
        }
        dumped = yaml.dump(player)
        with open(save_name, "w") as f:
            f.write(dumped)
        play = 1
    else:
        play = 1
# elif create_save.lower().startswith('c'):
else:
    play = 1

# checks to see if you are dead.
if player["health"] <= 0:
    if player["cheat"] < 3:
        cheatcode = input("What is the not-die code?")
        if not cheatcode == 43590:
            player["health"] = 10
            player["max health"] = 10
            player["x"] = 0
            player["y"] = 0
            player["inventory"] = ["Sword", "Healing Potion"]
            player["held item"] = "Sword"
            player["cheat"] = 0
            play = 0
        else:
            player["cheat"] += 1
            player["health"] = 10
    else:
        print("YOU DIED")
        player["health"] = 10
        player["max health"] = 10
        player["x"] = 0
        player["y"] = 0
        player["inventory"] = ["Sword", "Healing Potion"]
        player["held item"] = "Sword"
        player["cheat"] = 0
        play = 0

# gameplay here:
while play == 1:
    if player["x"] == 0 and player["y"] == 0:
        which_direction = input("You can go north, south, east or west.")
        if which_direction.lower().startswith('n'):
            player["y"] += 1
        elif which_direction.lower().startswith('s'):
            player["y"] -= 1
        elif which_direction.lower().startswith('e'):
            player["x"] += 1
        elif which_direction.lower().startswith('w'):
            player["x"] -= 1

    elif player["x"] == 0 and player["y"] == 1:
        which_direction = input("You can go north, or south.")
        if which_direction.lower().startswith('n'):
            player["y"] += 1
        elif which_direction.lower().startswith('s'):
            player["y"] -= 1
        # elif which_direction.lower().startswith('e'):
        #     player["x"] += 1
        # elif which_direction.lower().startswith('w'):
        #     player["x"] -= 1

    elif player["x"] == 0 and player["y"] == -1:
        which_direction = input("You can go north, east, or west.")
        if which_direction.lower().startswith('n'):
            player["y"] += 1
        # elif which_direction.lower().startswith('s'):
        #     player["y"] -= 1
        elif which_direction.lower().startswith('e'):
            player["x"] += 1
        elif which_direction.lower().startswith('w'):
            player["x"] -= 1

    elif player["x"] == 1 and player["y"] == 0:
        which_direction = input(
            "You can go west. There is a map on the ground. (type T to take the map, press M to view it when you have it.")
        # if which_direction.lower().startswith('n'):
        #     player["y"] += 1
        # elif which_direction.lower().startswith('s'):
        #     player["y"] -= 1
        # elif which_direction.lower().startswith('e'):
        #     player["x"] += 1
        if which_direction.lower().startswith('w'):
            player["x"] -= 1
        elif which_direction.lower().startswith('t'):
            if 'Map' not in player["inventory"]:
                player["inventory"].append('Map')
        elif which_direction.lower().startswith('m'):
            if 'Map' in player["inventory"]:
                print("**|**")
                print("*[+]*")
                print("**⊥**")

    elif player["x"] == -1 and player["y"] == 0:
        which_direction = input(
            "You can go east. There is an axe on the ground. (type T to take the axe.")
        # if which_direction.lower().startswith('n'):
        #     player["y"] += 1
        # elif which_direction.lower().startswith('s'):
        #     player["y"] -= 1
        if which_direction.lower().startswith('e'):
            player["x"] += 1
        # if which_direction.lower().startswith('w'):
        #     player["x"] -= 1
        elif which_direction.lower().startswith('t'):
            if 'Map' not in player["inventory"]:
                player["inventory"].append('Axe')
        elif which_direction.lower().startswith('m'):
            if 'Map' in player["inventory"]:
                print("**|**")
                print("*[+]*")
                print("**⊥**")

# put all the new data in the file
dumped = yaml.dump(player)

with open("save.yaml", "w") as f:
    f.write(dumped)