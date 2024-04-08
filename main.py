# These are our imports
import random
import tkinter as tk
from tkinter import messagebox

# Generates stats for the user
def generate_random_stats():
    min_stat = 8 # Minimum value for a stat
    max_stat = 18 # Maximum value for a stat
    # List of abilities
    abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    
    # Generates a random value for each ability and maps it to the ability
    abilities_values = {ability: random.randint(min_stat, max_stat) for ability in abilities}
    
    # Returns the abilities and their values
    return abilities_values

# Generate a background for the user and gives description
def generate_random_background():
    backgrounds = {
        'Acolyte': 'You have spent your life in service to a temple, learning sacred rites and providing spiritual guidance.',
        'Criminal': 'You have a history of breaking the law and have honed your skills to survive in the underworld.',
        'Folk Hero': 'You come from a humble social rank but became a local hero for your deeds and courage.',
        'Noble': 'You were born into a family of high social standing, and you are accustomed to a life of privilege.',
        'Sage': 'You spent years in study, collecting knowledge and becoming an expert in various fields.',
        'Soldier': 'You served in an army, and your training and discipline have shaped your skills.'
    }

    # Returns a random background from the list
    return random.choice(list(backgrounds.keys()))

# ************** SUBCLASSES FUNCTIONS ****************

def generate_wizard_subclass():
    wizard_subclasses = ['School of Evocation', 'School of Abjuration', 'School of Conjuration', 'School of Necromancy', 'School of Transmutation', 'School of Enchantment', 'School of Illusion', 'School of Divination', 'Bladesinging', 'War Magic']
    return random.choice(wizard_subclasses)

def generate_rogue_subclass():
    rogue_subclasses = ['Thief', 'Assassin', 'Arcane Trickster', 'Mastermind', 'Swashbuckler', 'Inquisitive', 'Scout', 'Phantom']
    return random.choice(rogue_subclasses)

def generate_fighter_subclass():
    fighter_subclasses = ['Champion', 'Battle Master', 'Eldritch Knight', 'Arcane Archer', 'Cavalier', 'Samurai', 'Purple Dragon Knight', 'Echo Knight']
    return random.choice(fighter_subclasses)

def generate_cleric_subclass():
    cleric_subclasses = ['Life Domain', 'Light Domain', 'Nature Domain', 'Tempest Domain', 'Trickery Domain', 'War Domain', 'Death Domain', 'Knowledge Domain', 'Forge Domain', 'Grave Domain', 'Order Domain', 'Peace Domain', 'Twilight Domain']
    return random.choice(cleric_subclasses)

def generate_barbarian_subclass():
    barbarian_subclasses = ['Path of the Berserker', 'Path of the Totem Warrior', 'Path of the Ancestral Guardian', 'Path of the Storm Herald', 'Path of the Zealot', 'Path of the Battlerager']
    return random.choice(barbarian_subclasses)

def generate_ranger_subclass():
    ranger_subclasses = ['Hunter', 'Beast Master', 'Gloom Stalker', 'Horizon Walker', 'Fey Wanderer']
    return random.choice(ranger_subclasses)

def generate_paladin_subclass():
    paladin_subclasses = ['Oath of Devotion', 'Oath of the Ancients', 'Oath of Vengeance', 'Oath of Conquest', 'Oath of Redemption', 'Oath of the Crown', 'Oathbreaker', 'Oath of the Watchers']
    return random.choice(paladin_subclasses)

def generate_monk_subclass():
    monk_subclasses = ['Way of the Open Hand', 'Way of Shadow', 'Way of the Four Elements', 'Way of the Drunken Master', 'Way of the Kensei', 'Way of the Sun Soul']
    return random.choice(monk_subclasses)

def generate_sorcerer_subclass():
    sorcerer_subclasses = ['Draconic Bloodline', 'Wild Magic', 'Divine Soul', 'Shadow Magic', 'Storm Sorcery', 'Aberrant Mind', 'Clockwork Soul']
    return random.choice(sorcerer_subclasses)

def generate_druid_subclass():
    druid_subclasses = ['Circle of the Land', 'Circle of the Moon', 'Circle of Dreams', 'Circle of the Shepherd', 'Circle of Twilight', 'Circle of Spores']
    return random.choice(druid_subclasses)

def generate_warlock_subclass():
    warlock_subclasses = ['The Archfey', 'The Fiend', 'The Great Old One', 'The Celestial', 'The Hexblade', 'The Undying', 'The Raven Queen', 'The Genie', 'The Fathomless']
    return random.choice(warlock_subclasses)

def generate_bard_subclass():
    bard_subclasses = ['College of Lore', 'College of Valor', 'College of Glamour', 'College of Swords', 'College of Whispers', 'College of Eloquence']
    return random.choice(bard_subclasses)

# ************** END SUBCLASSES FUNCTIONS ****************

# Generates a random character for the user
def generate_random_character(name, char_class=None):
    # List of races and classes to be randomized
    races = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Tiefling', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc']
    classes = ['Wizard', 'Rogue', 'Fighter', 'Cleric', 'Barbarian', 'Ranger', 'Paladin', 'Monk', 'Sorcerer', 'Druid', 'Warlock', 'Bard']

    # Randomizes a race and sets it
    race = random.choice(races)
    
    # If the user did not enter a class, randomize it
    if char_class is None:
        char_class = random.choice(classes)
    
    # Randomizes abilities and their values
    abilities_values = generate_random_stats()
    ability_modifiers = {ability: (value - 10) // 2 for ability, value in abilities_values.items()}

    # Generate a random background
    background = generate_random_background()
    
    #************** SUBCLASSES ****************
    # Allows subclasses to be randomized based on class received or picked
    if char_class == 'Wizard':
        subclass = generate_wizard_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Rogue':
        subclass = generate_rogue_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Fighter':
        subclass = generate_fighter_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Cleric':
        subclass = generate_cleric_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Barbarian':
        subclass = generate_barbarian_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Ranger':
        subclass = generate_ranger_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Paladin':
        subclass = generate_paladin_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Monk':
        subclass = generate_monk_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Sorcerer':
        subclass = generate_sorcerer_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Druid':
        subclass = generate_druid_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Warlock':
        subclass = generate_warlock_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    elif char_class == 'Bard':
        subclass = generate_bard_subclass()
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Subclass': subclass,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }
    #************** END SUBCLASSES ****************
    #If the user enters class and it doesn't match any of the above, it will generate a character without a subclass
    else:
        character = {
            'Name': name,
            'Race': race,
            'Class': char_class,
            'Background': background,
            'Abilities': abilities_values,
            'Ability Modifiers': ability_modifiers
        }

    return character

# Prints the character's information
def print_character(character):
    # Prints the character's information
    character_info = f"Generated Character for {character['Name']}:\n"
    # Prints the race 
    character_info += f"Race: {character['Race']}\n"
    # Prints the class
    character_info += f"Class: {character['Class']}\n"
        
    # If the character has a subclass, print it
    if 'Subclass' in character:
        character_info += f"Subclass: {character['Subclass']}\n"

    # Print the background information
    character_info += f"Background: {character['Background']}\n"
    
    # Prints the abilities and their values  
    character_info += "Ability Scores\n"
    for ability, value in character['Abilities'].items():
        modifier = character['Ability Modifiers'][ability]
        character_info += f"{ability}: {value} (Modifier: {modifier})\n"
    
    # Returns the character's information
    return character_info


# Welcome screen function
def welcome_screen():
    # Create a new window for the welcome screen
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome to D&D Character Generator")
    welcome_window.geometry("400x200")

    # Welcome message
    welcome_label = tk.Label(welcome_window, text="Welcome to the D&D Character Generator!\n All you need to do is enter your name. \nWe'll handle the rest.")
    welcome_label.pack(pady=20)

    # Start button to close the welcome screen and open the main window
    start_button = tk.Button(welcome_window, text="Start", command=welcome_window.destroy)
    start_button.pack()

# Generates and displays the character
def generate_and_display_character():
    user_name = name_entry.get()
    user_class = class_entry.get()

    if user_name.strip() == "":
        messagebox.showinfo("Error", "Please enter your name.")
        return

    # Generate a random character
    if user_class:  # If the user manually entered a class
        random_character = generate_random_character(user_name, user_class)
    else:  # If the user wants to randomize the class
        random_character = generate_random_character(user_name)

    # Display the character information
    character_info = print_character(random_character)
    result_label.config(text=character_info)

# Clears character information
def clear_character():
    name_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("D&D Random Character Generator")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add options to the "File" menu
file_menu.add_command(label="Clear Character", command=clear_character)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Set the window size to 400x450
root.geometry("400x450")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

class_label = tk.Label(root, text="Enter your class (leave blank for random):")
class_label.pack()

class_entry = tk.Entry(root)
class_entry.pack()

generate_button = tk.Button(root, text="Generate Character", command=generate_and_display_character)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Show the welcome screen
welcome_screen()

root.mainloop()
