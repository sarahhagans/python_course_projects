


#Part1 
#Part 1.1 make variables day month year to reflect my birthday.
day = "2nd"
month = "August"
year = "1994"


#Part 1.2 Concatenate to read as your birthday in one line

#Part1.3 Assign the concatenation to a fourth variable named my_birthday.
my_birthday = month + " " + day + ", " + year

#Part 1.4 Finally, print the variable my_birthday. OUTPUT : November 11, 1991
print(my_birthday)

# Part 2

first = "happy"
second = "birthday"
third = "to"
fourth = "you"

final = first + " " + second + " " + third + " " + fourth

print(final.upper())


#Part 3

#If under the age of 10, print Not permitted
#If under the age of 15, print Permitted with a parent
#If under the age of 18, print Permitted with anyone over 18
#If 18 or over, print Permitted to attend alone

age = 15

if age < 10:
  print("Not permitted")
elif age < 15:
  print("Permitted with a parent")
elif age < 18:
  print("Permitted with anyone over 18")
elif age >= 18:
  print("Permitted to attend alone")
