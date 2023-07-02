import random

# Define lists of monster attributes
monster_names = ["Goblin", "Dragon", "Vampire", "Werewolf", "Zombie"]
monster_sizes = ["Small", "Medium", "Large"]
monster_types = ["Beast", "Undead", "Magical", "Humanoid"]
monster_powers = ["Fire Breath", "Invisibility", "Teleportation", "Mind Control"]
monster_weaknesses = ["Silver", "Sunlight", "Water"]

# Function to generate a random monster
def generate_monster():
    name = random.choice(monster_names)
    size = random.choice(monster_sizes)
    monster_type = random.choice(monster_types)
    power = random.choice(monster_powers)
    weakness = random.choice(monster_weaknesses)

    # Print the generated monster
    print("Monster Name:", name)
    print("Size:", size)
    print("Type:", monster_type)
    print("Power:", power)
    print("Weakness:", weakness)

# Generate a random monster
generate_monster()
