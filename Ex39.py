
things = ['a', 'b', 'c', 'd']

print(things[1])

things[1] = 'z'
print(things[1])

print(things)

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "San Francisco"

stuff[1] = "Wow"
stuff[2] = "Neato"

print(stuff[1])
print(stuff[2])

print(stuff)

del stuff['city']

print(stuff)

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR', # 俄勒冈州
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'detroit', # 底特律
    'FL': 'Jacksonville', # 杰克逊维尔
    'NY': 'New York',
    'OR' : 'Portland' # 波特兰 （奥勒冈州最大城市）
}

# print out some cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

# print some states
print('-'*10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
for abbrev, city in cities.items():
    print("%s has the city %s" %(abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

# get a city with default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is : %s" % city)

