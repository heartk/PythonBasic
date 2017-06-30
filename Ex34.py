
animals = ['bear', 'tiger', 'penguin', 'zebra']
bear = animals[0]

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

for i in range(0, animals.__len__()):
    print("The animal at %d st. is at %d and is a %s" %(i+1 ,i , animals[i]) )
    i += 1
