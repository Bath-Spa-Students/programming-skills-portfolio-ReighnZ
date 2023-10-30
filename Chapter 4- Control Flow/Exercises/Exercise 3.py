''' This code provides three versions, each with a different color for an alien.
It uses an if-elif-else chain to determine the color of the alien and print a corresponding message about the points the player earns for shooting that alien.
The points vary based on the color: 5 points for green, 10 points for yellow, and 15 points for red. '''

# Version 1
alien_color = 'green'

if alien_color == 'green':
    print("The player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("The player just earned 10 points for shooting the yellow alien.")
else:
    print("The player just earned 15 points for shooting the red alien.")

# Version 2
alien_color = 'yellow'

if alien_color == 'green':
    print("The player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("The player just earned 10 points for shooting the yellow alien.")
else:
    print("The player just earned 15 points for shooting the red alien.")

# Version 3
alien_color = 'red'

if alien_color == 'green':
    print("The player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("The player just earned 10 points for shooting the yellow alien.")
else:
    print("The player just earned 15 points for shooting the red alien.")