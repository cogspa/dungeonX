import random
import string

# Define lists of monster attributes
monster_names = ["Goblin", "Dragon", "Vampire", "Werewolf", "Zombie"]
monster_sizes = ["Small", "Medium", "Large"]
monster_types = ["Beast", "Undead", "Magical", "Humanoid"]
monster_powers = ["Fire Breath", "Invisibility", "Teleportation", "Mind Control"]
monster_weaknesses = ["Silver", "Sunlight", "Water"]
monster_features = ["Tentacles", "Eyestalks", "Spines", "Extra Arms"]

# Function to generate a random mutation
def generate_mutation():
    letters = string.ascii_lowercase
    mutation = ''.join(random.choice(letters) for _ in range(5))
    return mutation

# Function to generate a random nonsense monster name
def generate_nonsense_name():
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    name = ""
    for _ in range(random.randint(2, 5)):
        name += random.choice(consonants)
        name += random.choice(vowels)
    return name.capitalize()

# Function to generate random monster features
def generate_features():
    features = random.sample(monster_features, random.randint(1, len(monster_features)))
    return features

# Function to generate a random monster
def generate_monster():
    name = random.choice(monster_names)
    size = random.choice(monster_sizes)
    monster_type = random.choice(monster_types)
    power = random.choice(monster_powers)
    weakness = random.choice(monster_weaknesses)
    mutation = generate_mutation()
    nonsense_name = generate_nonsense_name()
    features = generate_features()

    # Print the generated monster
    print("Monster Name:", name)
    print("Nonsense Name:", nonsense_name)
    print("Size:", size)
    print("Type:", monster_type)
    print("Power:", power)
    print("Weakness:", weakness)
    print("Mutation:", mutation)
    print("Features:", ", ".join(features))

# Generate a random monster
generate_monster()
