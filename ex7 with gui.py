import csv
from pokedex_gui import show_Pokedex_GUI

#           "Coding Style Will Not Have an Effect On Your Grade In This Assignment"
#                                ~E.Houry (goat), 2025
#           
#           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣶⣦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣶⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⠀⠀⢀⡀⣄⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠉⠀⢀⣀⠀⠀⠈⠉⠀⠀⣀⣀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⣀⣶⣿⣿⣿⣾⣇⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⣼⡏⠀⠀⠀⣀⣀⣉⠉⠩⠭⠭⠭⠥⠤⢀⣀⣀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⠈⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
#           ⠀⠀⠀⠀⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
#           ⠀⠀⠀⠀⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
#           ⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣶⣤⣄⣠⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
#           ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
#           ⠀⠀⣀⠀⢸⡿⠿⣿⡿⠋⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠻⠿⠟⠉⢙⣿⣿⣿⣿⣿⣿⡇
#           ⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⢿⡿⣿⠳⠀
#           ⠀⠀⡞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⡀⠀⠀
#           ⢀⣸⣀⡀⠀⠀⠀⠀⣠⣴⣾⣿⣷⣆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⢿⣿⠿⠃⠀
#           ⠘⢿⡿⠃⠀⠀⠀⣸⣿⣿⣿⣿⣿⡿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⡸⠁⠀⠀⠀
#           ⠀⠀⠳⣄⠀⠀⠀⠹⣿⣿⣿⡿⠛⣠⠾⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠳⣄⠙⠛⠿⠿⠛⠉⠀⠀⣀⠜⠁⠀⠀⠀⠀
#           ⠀⠀⠀⠈⠑⠢⠤⠤⠬⠭⠥⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠢⠤⠤⠤⠒⠊⠁⠀⠀⠀⠀⠀⠀



# Global BST root
ownerRoot = None

########################
# 0) Read from CSV -> HOENN_DATA
########################


def read_hoenn_csv(filename):
    """
    Reads 'hoenn_pokedex.csv' and returns a list of dicts:
      [ { "ID": int, "Name": str, "Type": str, "HP": int,
          "Attack": int, "Can Evolve": "TRUE"/"FALSE" },
        ... ]
    """
    data_list = []
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')  # Use comma as the delimiter
        first_row = True
        for row in reader:
            # It's the header row (like ID,Name,Type,HP,Attack,Can Evolve), skip it
            if first_row:
                first_row = False
                continue

            # row => [ID, Name, Type, HP, Attack, Can Evolve]
            if not row or not row[0].strip():
                break  # Empty or invalid row => stop
            d = {
                "ID": int(row[0]),
                "Name": str(row[1]),
                "Type": str(row[2]),
                "HP": int(row[3]),
                "Attack": int(row[4]),
                "Can Evolve": str(row[5]).upper()
            }
            data_list.append(d)
    return data_list


HOENN_DATA = read_hoenn_csv("hoenn_pokedex.csv")

########################
# 1) Helper Functions
########################

def read_int_safe(prompt):
    """
    Prompt the user for an integer, re-prompting on invalid input.
    """
    while True:
        user_input = input(prompt)
        # Check if the input is valid for an integer (including negatives)
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        print("Invalid input.")
    
    

def get_poke_dict_by_id(poke_id):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by ID, or None if not found.
    """
    for pokemonData in HOENN_DATA:
        if pokemonData['ID'] == poke_id:
            return pokemonData.copy()
    return None

def get_poke_dict_by_name(name):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by name, or None if not found.
    """
    for pokemonData in HOENN_DATA:
        if pokemonData['Name'].lower() == name.lower():
            return pokemonData.copy()
    return None

def display_pokemon_list(poke_list):
    """
    Display a list of Pokemon dicts, or a message if empty.
    """
    if not poke_list:
        print("There are no Pokemons in this Pokedex that match the criteria.")
        return
    for pokemon in poke_list:
        print(f"ID: {pokemon['ID']}, Name: {pokemon['Name']}, Type: {pokemon['Type']}, HP: {pokemon['HP']}, "
        f"Attack: {pokemon['Attack']}, Can Evolve: {pokemon['Can Evolve']}")



########################
# 2) BST (By Owner Name)
########################

def create_owner_node(owner_name, first_pokemon=None):
    """
    Create and return a BST node dict with keys: 'owner', 'pokedex', 'left', 'right'.
    """
    newOwner = {
        'owner' : owner_name,
        'pokedex': [first_pokemon],
        'left' : None,
        'right': None
    }
    return newOwner

def insert_owner_bst(root, new_node):
    """
    Insert a new BST node by owner_name (alphabetically). Return updated root.
    """
    #No owners
    if root == None:
        root = new_node
        return root
    #Duplicates Owners
    if root['owner'].lower() == new_node['owner'].lower():
        return root
    #
    if root['owner'].lower() < new_node['owner'].lower():
        if root['right'] == None:
            root['right'] = new_node
            return root
        else:
            insert_owner_bst(root['right'], new_node)

    if root['owner'].lower() > new_node['owner'].lower():
        if root['left'] == None:
            root['left'] = new_node
            return root
        else:
            insert_owner_bst(root['left'], new_node)
    return root




def find_owner_bst(root, owner_name):
    """
    Locate a BST node by owner_name. Return that node or None if missing.
    """
    if root == None:
        return None
    
    if root['owner'].lower() == owner_name.lower():
        return root

    if owner_name.lower() < root['owner'].lower():
        return find_owner_bst(root['left'], owner_name)
    else:
        return find_owner_bst(root['right'], owner_name)

def min_node(node):
    """
    Return the leftmost node in a BST subtree.
    """
    temp = node
    while (temp['left'] != None):
        temp = temp['left']
    return temp
        

def delete_owner_bst(root, owner_name, skip = 0):
    """
    Remove a node from the BST by owner_name. Return updated root.
    handles also owners that do not exists.
    print outputs.
    """
    if skip == 0:
        if find_owner_bst(root, owner_name) == None:
            print(f"Owner '{owner_name}' not found.")
            return root
        skip = 1
    print(f"Deleting {owner_name}'s entire Pokedex...")
    print("Pokedex deleted.")
    if (root['owner'].lower() > owner_name.lower()):
        root['left'] = delete_owner_bst(root['left'], owner_name)
    if (root['owner'].lower() < owner_name.lower()):
        root['right'] = delete_owner_bst(root['right'], owner_name)
    
    if (root['right'] == None) and (root['left'] == None):
        return None
    if (root['right'] != None) and (root['left'] == None):
        return root['right']
    if (root['right'] == None) and (root['left'] != None):
        return root['left']
    if (root['right'] != None) and (root['left'] != None):
        temp = root['right']
        while(temp['left'] != None):
            temp = temp['left']
        root['owner'] = temp['owner']
        root['pokedex'] = temp['pokedex']
        root['right'] = delete_owner_bst(root['right'], temp['owner'])
        return root        




########################
# 3) BST Traversals
########################

def bfs_traversal(root):
    """
    BFS level-order traversal. Print each owner's name and # of pokemons.
    """
    queue = [root]
    while (len(queue) != 0):
        temp = queue.pop(0)
        if(temp['right'] is not None):
            queue.append(temp['right'])
        if(temp['left'] is not None):
            queue.append(temp['left'])
        owner_print(temp)



def pre_order(root):
    """
    Pre-order traversal (root -> left -> right). Print data for each node.
    """
    if root is None:
        return
    owner_print(root)
    pre_order(root['left'])
    pre_order(root['right'])
    


def in_order(root):
    """
    In-order traversal (left -> root -> right). Print data for each node.
    """
    if root is None:
        return
    
    in_order(root['left'])
    owner_print(root)
    in_order(root['right'])

def post_order(root):
    """
    Post-order traversal (left -> right -> root). Print data for each node.
    """
    if root is None:
        return
    
    post_order(root['left'])
    post_order(root['right'])
    owner_print(root)


########################
# 4) Pokedex Operations
########################

def add_pokemon_to_owner(owner_node):
    """
    Prompt user for a Pokemon ID, find the data, and add to this owner's pokedex if not duplicate.
    """
    id_choice = read_int_safe("Enter Pokemon ID to add: ")
    choice_poke_dict = get_poke_dict_by_id(id_choice)
    if choice_poke_dict==None:
        print(f"ID {id_choice} not found in Honen data.")
    elif choice_poke_dict in owner_node['pokedex']:
        print("Pokemon already in the list. No changes made.")
    else:
        owner_node['pokedex'].append(choice_poke_dict)
        print(f"Pokemon {choice_poke_dict['Name']} (ID {choice_poke_dict['ID']}) added to {owner_node['owner']}'s Pokedex.")
        

    

def release_pokemon_by_name(owner_node):
    """
    Prompt user for a Pokemon name, remove it from this owner's pokedex if found.
    """
    original_name_to_remove = input("Enter Pokemon Name to release: ")
    name_to_remove = original_name_to_remove.strip().capitalize()
    dict_to_remove = get_poke_dict_by_name(name_to_remove)
    if dict_to_remove == None or (dict_to_remove not in owner_node['pokedex']):
        print(f"No Pokemon named '{original_name_to_remove}' in {owner_node['owner']}'s Pokedex.")
    else:
        owner_node['pokedex'].remove(dict_to_remove)
        print(f"Releasing {dict_to_remove['Name']} from {owner_node['owner']}.")

def evolve_pokemon_by_name(owner_node):
    """
    Evolve a Pokemon by name:
    1) Check if it can evolve
    2) Remove old
    3) Insert new
    4) If new is a duplicate, dont even insert it.
    
    """
    original_name_to_evolve = input("Enter Pokemon Name to evolve: ")
    name_to_evolve = original_name_to_evolve.strip().capitalize()
    dict_to_evolve = get_poke_dict_by_name(name_to_evolve)
    if dict_to_evolve == None or (dict_to_evolve not in owner_node['pokedex']):
        print(f"No Pokemon named '{original_name_to_evolve}' in {owner_node['owner']}'s Pokedex.")
        return
    evolved_dict = get_poke_dict_by_id(dict_to_evolve['ID'] + 1)
    if (dict_to_evolve['Can Evolve'] == False):
        print(f"{dict_to_evolve['Name']} cannot evolve.")
    elif (evolved_dict in owner_node['pokedex']):
        print(f"Pokemon evolved from {dict_to_evolve['Name']} (ID {dict_to_evolve['ID']}) to {evolved_dict['Name']} (ID {evolved_dict['ID']}).") #No CODING StYlE 
        print(f"{evolved_dict['Name']} was already present; releasing it immediately.")
        owner_node['pokedex'].remove(dict_to_evolve)
    else:
        owner_node['pokedex'].remove(dict_to_evolve)
        owner_node['pokedex'].append(evolved_dict)
        print(f"Pokemon evolved from {dict_to_evolve['Name']} (ID {dict_to_evolve['ID']}) to {evolved_dict['Name']} (ID {evolved_dict['ID']}).")



########################
# 5) Sorting Owners by # of Pokemon
########################

def gather_all_owners(root, arr):
    """
    Collect all BST nodes into a list (arr). collect in-order so it will be alphabetical at first.
    """
    if root == None:
        return
    
    gather_all_owners(root['left'], arr)
    arr.append(root)
    gather_all_owners(root['right'], arr)


def sort_owners_by_num_pokemon():
    """
    Gather owners, sort them by (#pokedex size, then alpha), print results.
    """
    if ownerRoot == None:
        print("No owners at all.")
    else:
        all_owners = []
        gather_all_owners(ownerRoot, all_owners)
        all_owners.sort(key=lambda x: len(x['pokedex']))
        print("=== The Owners we have, sorted by number of Pokemons ===")
        for owner in all_owners:
            print(f"Owner: {owner['owner']} (has {len(owner['pokedex'])} Pokemon)")


########################
# 6) Print All
########################

def print_all_owners():
    """
    Let user pick BFS, Pre, In, or Post. Print each owner's data/pokedex accordingly.
    """
    if ownerRoot is None:
        print("No owners in the BST.")
        return
    print("""1) BFS
2) Pre-Order
3) In-Order
4) Post-Order""")
    print_choice = read_int_safe("Your choice: ")
    if print_choice == 1:
        bfs_traversal(ownerRoot)
    elif print_choice == 2:
        pre_order(ownerRoot)
    elif print_choice == 3:
        in_order(ownerRoot)
    elif print_choice == 4:
        post_order(ownerRoot)
    else:
        print("Invalid choice.")

def owner_print(node):
    """
    Helper to print data in BST.
    """
    print("")
    print(f"Owner: {node['owner']}")
    display_pokemon_list(node['pokedex'])



########################
# 7) The Display Filter Sub-Menu
########################

def display_filter_sub_menu(owner_node):
    """
    1) Only type X
    2) Only evolvable
    3) Only Attack above
    4) Only HP above
    5) Only name starts with
    6) All
    7) Back
    """
    while True:
        print("""
-- Display Filter Menu --
1. Only a certain Type
2. Only Evolvable
3. Only Attack above __
4. Only HP above __
5. Only names starting with letter(s)
6. All of them!
7. Back""")
        display_choice = read_int_safe("Your choice: ")
        if display_choice == 1:
            type_input = input("Which Type? (e.g. GRASS, WATER): ").strip().capitalize()
            display_pokemon_list([pokemon for pokemon in owner_node['pokedex'] if pokemon['Type'] == type_input])
        elif display_choice == 2:
            display_pokemon_list([pokemon for pokemon in owner_node['pokedex'] if pokemon['Can Evolve'] == 'TRUE'])
        elif display_choice == 3:
            attack_input = read_int_safe("Enter Attack threshold: ")
            display_pokemon_list([pokemon for pokemon in owner_node['pokedex'] if pokemon['Attack'] > attack_input])
        elif display_choice == 4:
            health_input = read_int_safe("Enter HP threshold: ")
            display_pokemon_list([pokemon for pokemon in owner_node['pokedex'] if pokemon['HP'] > health_input])
        elif display_choice == 5:
            letters_input = input("Starting letter(s): ").strip().capitalize()
            display_pokemon_list([pokemon for pokemon in owner_node['pokedex'] if pokemon['Name'].startswith(letters_input) ])
        elif display_choice == 6:
            display_pokemon_list(owner_node['pokedex'])
        elif display_choice == 7:
            print("Back to Pokedex Menu.")
            return
        else:
            print("Invalid choice.")
            continue


########################
# 8) Sub-menu & Main menu
########################

def existing_pokedex():
    """
    Ask user for an owner name, locate the BST node, then show sub-menu:
    - Add Pokemon
    - Display (Filter)
    - Release
    - Evolve
    - Back
    """
    currentOwnerName = input("Owner name: ").strip()
    currentOwnerNode = find_owner_bst(ownerRoot, currentOwnerName)
    if currentOwnerNode == None:
        print(f"Owner '{currentOwnerName}' not found.")
        return
    else:
        while(True):
            print(f"""
-- {currentOwnerNode['owner']}'s Pokedex Menu --
1. Add Pokemon
2. Display Pokedex
3. Release Pokemon
4. Evolve Pokemon
5. GUI
6. Back to Main""")
            userChoice = read_int_safe("Your choice: ")
            if userChoice == 1:
                add_pokemon_to_owner(currentOwnerNode)
            elif userChoice == 2:
                display_filter_sub_menu(currentOwnerNode)
            elif userChoice == 3:
                release_pokemon_by_name(currentOwnerNode)
            elif userChoice == 4:
                evolve_pokemon_by_name(currentOwnerNode)
            elif userChoice == 5:
                show_Pokedex_GUI(currentOwnerNode["pokedex"])
            elif userChoice == 6:
                print("Back to Main Menu.")
                return
            else:
                print("Invalid choice.")


def main_menu():
    userChoice = 0
    global ownerRoot
    while (userChoice != 6):
        print("""
=== Main Menu ===
1. New Pokedex
2. Existing Pokedex
3. Delete a Pokedex
4. Display owners by number of Pokemon
5. Print All
6. Exit""")
        userChoice = read_int_safe("Your choice: ")
        if userChoice < 1 or userChoice > 6:
            print("Invalid choice.")
            continue

        #New Pokedex
        if userChoice == 1:
            newOwnerName = input("Owner name: ").strip()
            if find_owner_bst(ownerRoot, newOwnerName) != None:
                print(f"Owner '{newOwnerName}' already exists. No new Pokedex created.")
            else:
                print("""Choose your starter Pokemon:
1) Treecko 
2) Torchic 
3) Mudkip""")
                pokemonChoice = read_int_safe("Your choice: ")
                if pokemonChoice<1 or pokemonChoice>3:
                    print("Invalid. No new Pokedex created.")
                else:

                    ownerRoot = insert_owner_bst(ownerRoot, create_owner_node(newOwnerName, get_poke_dict_by_id(pokemonChoice*3 -2)))
                    print(f"New Pokedex created for {newOwnerName} with starter {get_poke_dict_by_id(pokemonChoice*3 -2)['Name']}.")

        #Existing Pokedex
        elif userChoice == 2:
            existing_pokedex()

        #Delete Pokedex
        elif userChoice == 3:
            owner_to_remove = input("Enter owner to delete: ")
            ownerRoot = delete_owner_bst(ownerRoot, owner_to_remove)

        #Display owners by num of pokemons
        elif userChoice == 4:
            sort_owners_by_num_pokemon()
        
        #Print all owners
        elif userChoice == 5:
            print_all_owners()
        #Exit.
        elif userChoice == 6:
            print("Goodbye!")
            exit()
            #memory? wut?
        

def main():
    """
    Entry point: calls main_menu().
    """
    main_menu()


if __name__ == "__main__":
    main()
