# create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI',
    'New South Wales' : 'NSW',
    'Victoria' : 'VIC',
    'Australian Capital Territory' : 'ACT',
    'Tasmania' : 'TAS',
    'Western Australia' : 'WA',
    'Queensland' : 'QLD',
    'Northern Territory' : 'NT',
}

# create a basic set of states and some cities in them.
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville',
    'NSW' : 'Sydney',
    'VIC' : 'Melbourne',
    'ACT' : 'Canberra',
    'QLD' : 'Brisbane',
    'WA' : 'Perth',

}

# add some more cities
cities['NY'] = 'New York' # like doing 'NY' : 'New York' in cities
cities['OR'] = 'Portland'
cities['NT'] = 'Alice Springs'
cities['TAS'] = 'Hobart'
cities['WA'] = 'Broome'

# print out some cities
print('_' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])
print("TAS states has: ", cities['TAS'])
print("WA state has: ", cities['WA'])

# print some states
print('_' * 10)
print("Michigan's abbreviations is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
print("Northern Territories abbreviaton is: ", states['Northern Territory'])
print("New South Wales abbreviation is: ", states['New South Wales'])

# do it by using the state then cities dict
print('-' * 10)
# city = states['Michigan']
# print(">>>> Michigan states =", city)
# print("Michigan has: ", cities[city])
print("Michigan has: ",  cities[states['Michigan']]) # see how to debug above.
print("Florida has: ", cities [states['Florida']])
print("New South Wales has ", cities[states['New South Wales']])
print("Queensland has: ", cities[states['Queensland']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abreviated {abbrev}")

# print evrey city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()): #. is like state append(.) items
    print(f"{state} is abbreviated {abbrev} and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there.
state = states.get('Texas', None)

if not state:
    print("Sorry, No Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")





print("""
Study Drills

Q: Do this same kind of mapping with cities and states/regions in your country or some other country.
A: See above Australia states and cities

Q: Go find the python documentation for dicationaries (a.k.a dicts, dict) and try to do even more things to them.
A:""")
print('-' * 10)
print("Playing with dictionary Methods")
print("""
Dictionary Get method
Returns a value for a key if it exists in the dictionary
""")
print(states.get('Northern Territory')) #NT
print(states.get('NT')) # None

print("""
Dictionary items method
items returns a key-value pairs in a dictionary
""")
print(list(states.items()))
print(list(states.items())[1][0])
print(list(states.items())[1][1])

print("""
Dictionary items Keys method
Returns a list of keys in a dictionary""")
print("list of cities: ", list(cities.keys()))
print("list of states: ", list(states.keys()))

print("""
Dictionary Values method
Returns a list of values in a dictionary
""")
print("list of state values: ", list(states.values()))
print("list of citie values: ", list(cities.values()))

print("""
Dictionary Pop methods
Removes a key from a dictionary, if it's present, and returns it's value.
""")
print("list of states values: ", list(states.values()))
states.pop('Northern Territory')
print("list of states values: ", list(states.values()))
print("Can you see that NT is now missing?")

print("list of cities values: ", list(cities.values()))
cities.pop('NSW')
print("list of cities values: ", list(cities.values()))
print("What city was removed?")

print("""
Dictionary Pop item Method
Removes a key-value pair from a Dictionary
""")
print("list of states values: ", list(states.values()))
states.popitem()
print("list of states values: ", list(states.values()))
print("What state did we lose?")

print("""
Dictionary Update method
""")
print("This is what the states look like now: ", list(states.values()))
states2 = {
    'Northern Territory' : 'NT',
    'New Zealand' : 'NZ',
}
states.update(states2)
print("This is what states look like after compiling them together", list(states.values()))
print("Did you notice that NT that we removed back in pop method is back along with NZ.")
print("This is because we made a dictionary states2 with the variables", list(states2.values()))

print("""
Dictionary clear method
Clears a Dictionary
""")
states3 = {
}
states3.update(states)
print("Here are all the states: ", list(states3.values()))
states.clear() # clears the dictionary
print("Now all the states are gone! ", list(states.values()))
print("We better add them all back ")
states.update(states2)
print("Looks like we only got some of them back :( ", list(states.values()))
print("But I made a new states called states 3 maybe it has them all? ", list(states3.values()))

print("""
Q: Find out what you can't do with dictionaries. A big limitation is that they don not have order, so try playing with that.
A: For ordering dicts you would use collections.OrdedDirct data structure.
""")
