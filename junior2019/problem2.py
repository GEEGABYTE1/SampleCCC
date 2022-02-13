# Problem 2 
import math

# p = target amount of people
# N = number of people who have the disease
# R = How many people it affects per days
# Output the day 

p = int(input(''))
n = int(input(''))
r = int(input(''))

def growth(p , n, r):
    people = n
    day_count = 0 
    past_number_of_people = n
    while people <= p:
        day_count += 1
        new_people = r * past_number_of_people
        people += new_people
        past_number_of_people = new_people
    

    return day_count

print(growth(p, n, r))

        