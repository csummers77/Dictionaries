# Dictionaries
# Dictionaries are just like lists
# except.... instead of numbered indicies, they
# have english indicies

greg =[
    "Greg"
    "Male"
    "Tall"
    "Developer"
]
# If I wanted to know gregs job, I have to print greg[3], which is totally non-intutuve
# Instead you set it up like this:

# Key:value pair
# greg = {
#     "name": "Greg",
#     "gender": "Male",
#     "height": "Tall",
#     "Job": "Developer"
# }
# print greg["name"]
# print greg["Job"]

# Make a new dictionary
zombie = {} #dictionary
zombies = [] #list
# zombies.append()
zombie['weapon'] = "fist"
zombie['health'] = 100
zombie['speed1'] = 10
print zombie
print zombie['weapon']

for key, value in zombie.items():
    print "Zombie has a key %s with a value of %s" % (key, value)

# in our game, poor zombie loses his weapon (arm falls off)
# we nneed to remove his "weapon" key
del zombie['weapon']
print zombie
is_nighttime = True
if(is_nighttime):
    zombie['health'] += 50

# Put list and dictionaries together
zombies = []
zombies.append({
    'name': 'Hank',
    'weapon': 'baseball bat',
    'speed': 10
})
zombies.append({
    'name': 'Willie',
    'weapon': 'axe',
    'victims': [
        'squirrel',
        'rabbit',
        'fox'
    ]
})

print zombies[0] ['weapon']
# this will get the second victim, in the second zombies list of victims
print zombies[1] ['victims']