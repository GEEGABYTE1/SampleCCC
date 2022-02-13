# Write a program that reads several positive integers, one per
#       line.  For each integer n, output the number of orderings 
#       possible for a set of n distinct values.  n will not exceed 11.
#       The last line of input is indicated by 0


integers = input('')
string_integers = str(integers)
int_list = string_integers.split(' ')

def compute(lst):
    for number in lst:
        number = int(number)
        if number == 0:
            print(0)
        else:
            result = 1 
            for i in range(1, number + 1):
                result *= i 
            
            print(result)
print(compute(int_list))


