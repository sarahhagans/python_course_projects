



#Part 1.1 Create 2 dictonaries



Stanley = {
    'type' : 'Cat',
    'Color' : 'Grey',
    'nickname' : 'Wooloo',
    'owner' : 'Sarah'
    }
Loretta = {
    'type' : 'Cat',
    'Color' : 'Calico',
    'nickname' : 'Shmergetta',
    'owner' : 'Javin'
}

# Part 1.2 Iterate dictonaries so that the output has each Key-value pair on a new line.
for key, value in Stanley.items():
    print("Key =", key, "\tValue =", value)

for key, value in Loretta.items():
    print("Key =", key, "\tValue =", value)




#Part 2.1 Add 3 new dictionaries. Each should represent a city around the world.

#Part 2.2 Add this dictionary.

england = {'Capital': 'London'}
france = {'Capital': 'Paris'}
belgium = {'Capital': 'Brussels'}

# Part2.3 
#Population

#The population of England is 53.01 million
england['population'] = '53.01 million'
france['population'] = '6.9 million'
belgium['population'] = '11.35 million'
#The population of France is 66.9 million
#The population of Belgium is 11.35 million
#Interesting Fact
england['fact'] = 'Jumping a queue can be illegal'
france['fact'] = 'France Is Smaller Than Texas'
belgium['fact'] = 'Audrey Hepburn was born in Brussels'
#Top Language Spoken by Locals
england['language'] = 'english'
france['language'] = 'french'
belgium['language'] = 'dutch'
#Part 2.4 loop through each one and print out all key-value pairs.

for key, value in england.items():
    print(key + ": ", value)

for key, value in france.items():
    print(key + ": ", value)

for key, value in belgium.items():
    print(key + ": ", value)



#Part 3.1
pizza_order = {
    'customer_name' : 'Max',
    'size' : 'large',
    'crust' : 'pan',
    'toppings' : "pepperoni , pepper, olives"
}
#Part 3.2 print customers order;
print('Thank you for your order', pizza_order.get('customer_name'))
print('You have ordered a', pizza_order.get('size'), pizza_order.get('crust'),'crust pizza with the following toppings:')
print(pizza_order.get('toppings'))

