



my_message = "Hello"
my_other_message = "how are you?"

# concatenate the above variables with a comma in between
my_final_message = my_message + ", " + my_other_message

print(my_final_message)
day = "1"
year = "2017"
month = "August"

today_is = month + " " + day + ", " + year

print(today_is)

#Converting Data to strings
day = 1
year = 2017
month = "August"

today_is = month + " " + day + ", " + year

print(today_is)

#turn the integers into strings with the str() function,
day = 1
year = 2017
month = "August"

today_is = month + " " + str(day) + ", " + str(year)

print(today_is)

#The str.format takes in the string and within the string are empty curly braces {}
day = 1
year = 2017
month = "August"

today_is = str.format("The date is {}, {} {} ", year, month, day)

print(today_is)
#The output will be 'The date is 2017, August 1'

#Changing Cases:
my_message = "THESE ARE ALL CAPS"

print(my_message.lower())
# Output: these are all caps

my_message = "these are all lower"

print(my_message.upper())
#OUTPUT : THESE ARE ALL LOWER

# expressions within parentheses are evaluated first
result = (5 * 2) + (4 * 2)
print(result)
# after simplifying the expressions within the parentheses...
# result = (10) + (8) = 18

# ---

# do you understand how the final result, below, is computed?
result = 2 ** 3 * (5 - (3 - 2)) / 4 + 9 // 4
print(result)
# result = 8 * (4) / 4 + 2 = 8 * 1 + 2 = 10.0

a = 15
b = 5
c = 0

c = a + b
print("1. C =", c)

c += a
print("2. C =", c)

c *= a
print("3. C =", c)

c /= a
print("4. C =", c)

c %= a
print("5. C =", c)

c //= b
print("6. C =", c)

c = 2
c **= a
print("7. C =", c)

#1. C = 20
#2. C = 35
#3. C = 525
#4. C = 35.0
#5. C = 5.0
#6. C = 1.0
#7. C = 32768

