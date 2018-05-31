Locations = {0: "Quit",
             1: "Your current location is on the Road",
             2: "You are currently on the Hill",
             3: "Currently you are inside a Building",
             4: "You are in the Valley",
             5: "Now you are in the Forest",
             6: "Help"}
Ways = {0: 'Quit',
        1: {'N': 5, 'E': 3, 'W': 2, 'S': 4, 'Q': 0, 'H': 6},
        2: {'N': 5, 'Q': 0, 'H': 6},
        3: {'W': 1, 'Q': 0, 'H': 6},
        4: {'N': 1, 'W': 2, 'Q': 0, 'H': 6},
        5: {'S': 1, 'W': 2, 'Q': 0, 'H': 6}}

Possible_answers = {'Q': ['Q', 'QUIT', 'EXIT', 'STOP', 'END', '0'],
                    'N': ['N', 'NORTH', 'UP'],
                    'E': ['E', 'EAST', 'RIGHT'],
                    'W': ['W', 'WEST', 'LEFT'],
                    'S': ['S', 'SOUTH', 'DOWN'],
                    'H': ['H', 'HELP']}
curr_location = 1
k = ''
while curr_location != 0:
    print("=>=>=>", Locations[curr_location])
    possible_ways = ','.join(Ways[curr_location].keys())
    print("Which way do you want to go: ", possible_ways)
    user_input = input().upper().split()
    for i in Possible_answers.values():
        for j in i:
            if j in user_input:
                user_input = i[0]
                go = 1
                break
            else:
                go = 0
        if go == 1:
            break
    if go == 1:
        now = curr_location
        curr_location = Ways[curr_location].get(user_input, curr_location)
        if now == curr_location:
            print("O o you can't go that way now.")
        if curr_location == 6:
            print("Following hints are there to help you: ")
            for i in Possible_answers.values():
                print(i)
            curr_location = now
    if go == 0:
        print("Sorry This is not a valid input. Try again.")
