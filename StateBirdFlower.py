# State data.
states_data = {
    "alabama": ["Capital: Montgomery", "Bird: Yellowhammer", "Flower: Camellia"],
    "alaska": ["Capital: Juneau", "Bird: Willow Ptarmigan", "Flower: Forget Me Not"],
    "arizona": ["Capital: Phoenix", "Bird: Cactus Wren", "Flower: Saguaro Cactus Blossom"],
    "arkansas": ["Capital: Little Rock", "Bird: Mockingbird", "Flower: Apple Blossom"],
    "california": ["Capital: Sacramento", "Bird: California Valley Quail", "Flower: California Poppy"],
    "colorado": ["Capital: Denver", "Bird: Lark Bunting", "Flower: White and Lavender Columbine"],
    "connecticut": ["Capital: Hartford", "Bird: Robin", "Flower: Mountain Laurel"],
    "delaware": ["Capital: Dover", "Bird: Blue Hen", "Flower: Peach Blossom"],
    "florida": ["Capital: Tallahassee", "Bird: Mockingbird", "Flower: Orange Blossom"],
    "georgia": ["Capital: Atlanta", "Bird: Brown Thrasher", "Flower: Cherokee Rose"],
    "hawaii": ["Capital: Honolulu", "Bird: Nene", "Flower: Hibiscus"],
    "idaho": ["Capital: Boise", "Bird: Mountain Bluebird", "Flower: Syringa"],
    "illinois": ["Capital: Springfield", "Bird: Cardinal", "Flower: Purple Violet"],
    "indiana": ["Capital: Indianapolis", "Bird: Cardinal", "Flower: Peony"],
    "iowa": ["Capital: Des Moines", "Bird: Eastern Goldfinch", "Flower: Wild Prairie Rose"],
    "kansas": ["Capital: Topeka", "Bird: Western Meadowlark", "Flower: Sunflower"],
    "kentucky": ["Capital: Frankfort", "Bird: Cardinal", "Flower: Goldenrod"],
    "louisiana": ["Capital: Baton Rouge", "Bird: Eastern Brown Pelican", "Flower: Magnolia"],
    "maine": ["Capital: Augusta", "Bird: Chickadee", "Flower: White Pine Cone and Tassel"],
    "maryland": ["Capital: Annapolis", "Bird: Baltimore Oriole", "Flower: Black-Eyed Susan"],
    "massachusetts": ["Capital: Boston", "Bird: Chickadee", "Flower: Mayflower"],
    "michigan": ["Capital: Lansing", "Bird: Robin", "Flower: Apple Blossom"],
    "minnesota": ["Capital: Saint Paul", "Bird: Common Loon", "Flower: Pink and White Lady Slipper"],
    "mississippi": ["Capital: Jackson", "Bird: Mockingbird", "Flower: Magnolia"],
    "missouri": ["Capital: Jefferson City", "Bird: Bluebird", "Flower: White Hawthorn Blossom"],
    "montana": ["Capital: Helena", "Bird: Western Meadowlark", "Flower: Bitterroot"],
    "nebraska": ["Capital: Lincoln", "Bird: Western Meadowlark", "Flower: Goldenrod"],
    "nevada": ["Capital: Carson City", "Bird: Mountain Bluebird", "Flower: Sagebrush"],
    "new hampshire": ["Capital: Concord", "Bird: Purple Finch", "Flower: Purple Lilac"],
    "new jersey": ["Capital: Trenton", "Bird: Eastern Goldfinch", "Flower: Violet"],
    "new mexico": ["Capital: Santa Fe", "Bird: Roadrunner", "Flower: Yucca Flower"],
    "new york": ["Capital: Albany", "Bird: Bluebird", "Flower: Rose"],
    "north carolina": ["Capital: Raleigh", "Bird: Cardinal", "Flower: Dogwood"],
    "north dakota": ["Capital: Bismarck", "Bird: Western Meadowlark", "Flower: Wild Prairie Rose"],
    "ohio": ["Capital: Columbus", "Bird: Cardinal", "Flower: Scarlet Carnation"],
    "oklahoma": ["Capital: Oklahoma City", "Bird: Scissor-Tailed Flycatcher", "Flower: Mistletoe"],
    "oregon": ["Capital: Salem", "Bird: Western Meadowlark", "Flower: Oregon Grape"],
    "pennsylvania": ["Capital: Harrisburg", "Bird: Ruffed Grouse", "Flower: Mountain Laurel"],
    "rhode island": ["Capital: Providence", "Bird: Rhode Island Red", "Flower: Violet"],
    "south carolina": ["Capital: Columbia", "Bird: Great Carolina Wren", "Flower: Yellow Jessamine"],
    "south dakota": ["Capital: Pierre", "Bird: Ring-Necked Pheasant", "Flower: Pasque Flower"],
    "tennessee": ["Capital: Nashville", "Bird: Mockingbird", "Flower: Iris"],
    "texas": ["Capital: Austin", "Bird: Mockingbird", "Flower: Bluebonnet"],
    "utah": ["Capital: Salt Lake City", "Bird: California Seagull", "Flower: Sego Lily"],
    "vermont": ["Capital: Montpelier", "Bird: Hermit Thrush", "Flower: Red Clover"],
    "virginia": ["Capital: Richmond", "Bird: Cardinal", "Flower: Dogwood"],
    "washington": ["Capital: Olympia", "Bird: Willow Goldfinch", "Flower: Pink Rhododendron"],
    "west virginia": ["Capital: Charleston", "Bird: Cardinal", "Flower: Rhododendron"],
    "wisconsin": ["Capital: Madison", "Bird: Robin", "Flower: Wood Violet"],
    "wyoming": ["Capital: Cheyenne", "Bird: Western Meadowlark", "Flower: Indian Paintbrush"],
    }

# Start prompt.
print('\n**** Welcome to the state data application! ****')

# Menu prompt.
def menu():
    print('\n\nSelect from the following menu:\n\
        \n1. Display all U.S. States in Alphabetical order along with Capital and Flower\
        \n2. Search for a specific state and display the appropriate Capital and Bird\
        \n3. Update a Bird for a specific state\n4. Exit the program\n')

# Displays state data.
def stateData():
    for state, data in states_data.items():
        print (f'{state.title()}:  {data}')

# Finds state.
def findState(state):
    if state in states_data:
        print (f'%s: %s' % (state.title(), states_data[state]))
    else:
        print ('\nState not found.')

# Updates bird.
def updateBird(state):
    if state in states_data:
        new_bird = input((f"Enter %s's new State Bird:") % state.title())
        states_data[state][1] = (f'State Bird: %s' % new_bird)
        print (f'New entry for %s follows:' % state.title())
        print (f'%s: %s' % (state.title(), states_data[state]))
    else:
        print ('\nState not found.')

# Holds loop status in memory.
loop = True

# Sentinel while loop
while loop:
    menu()
    try:
        # Holds the user input in memory.
        userInput = int(input())

        if userInput == 1:
            stateData()
        if userInput == 2:
            state = input('Please enter a state: ')
            print('Your choice: ' + state)
            findState(state.lower())
        if userInput == 3:
            state = input('Please enter a state: ')
            print('Your choice: ' + state)
            updateBird(state.lower())
        if userInput == 4:
            print('\nYou selected 4.\n\nThanks for trying the State Data Application.\
                \n\n*********************************************************\n')
            loop = False # Ends loop and consequently, the program.
    except:
        ValueError
        print('\nEnter a valid integer.')
