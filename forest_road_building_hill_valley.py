# here I am using dictionaries to store position and their corresponding
# paths to go to
Locations = {0: "Quit",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}
Ways = ({'North': 5, 'East': 3, 'West': 2, 'South': 4, 'Quit': 0},
        {'North': 5, 'Quit': 0},
        {'West': 1, 'Quit': 0},
        {'North': 1, 'West': 2, 'Quit': 0},
        {'South': 1, 'West': 2, 'Quit': 0})

user_input = 1
while user_input != 0:
    choice_list = []
    go = 0
    print("Available ways are given below, choose one: ")
    for i in dict(Ways[user_input - 1]).values():
        choice_list.append(i)
        print(i, ':', Locations[i])
    while go != 1:
        print("Now Please select from the above options:")
        user_input = int(input())
        if user_input in choice_list:
            go = 1
        else:
            print("That option is not available. Try again:")
            go = 0
print("Well played!!! Come back soon!!!")
