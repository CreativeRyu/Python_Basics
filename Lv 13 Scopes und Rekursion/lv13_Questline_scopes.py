# # # # Lv 12 Functions and Scopes # # # #

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    # Was wird hier ausgegeben?

increase_enemies()
print(f"enemies outside function: {enemies}")
# und was wird hier ausgegeben?

#########################################

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
#print(potion_strength)

#########################################

# Global Scope
player_health = 10


def show_player_health():
    print(player_health)


show_player_health()

#########################################


def increase_global_enemies():
    global enemies  # ist möglich, sollte aber tunlichst vermieden werden
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_global_enemies()
print(f"enemies outside function: {enemies}")

########################################### ->


def increase_returned_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_returned_enemies()


###############################################################


####################################################################################

"""
 _                 _          ___ _     _          _ 
| |   ___  __ __ _| | __ __  / __| |___| |__  __ _| |
| |__/ _ \/ _/ _` | | \ \ / | (_ | / _ \ '_ \/ _` | |
|____\___/\__\__,_|_| /_\_\  \___|_\___/_.__/\__,_|_|
"""

# Beispiel 1
def spam_global():
    print(eggs)
eggs = 10 # globale Variablen Definition

spam_global()

################################

# Beispiel 2
def spam_local():
    print(eggs)
    eggs = 42
eggs = 10

spam_local()

################################

def spam_chaos():
    global eggs
    eggs = 43

####################################################################################

"""
 ___     _               _          
| _ \___| |___  _ _ _ __(_)___ _ _  
|   / -_) / / || | '_(_-< / _ \ ' \ 
|_|_\___|_\_\\_,_|_| /__/_\___/_||_|
"""

def twist_numbers(number):
    if number > 7:
        number = number - 1
        number = twist_numbers(number)
        return number
    return number


