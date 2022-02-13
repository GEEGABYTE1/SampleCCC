''' Thuc likes finding cyclic shifts of strings. A cyclic shift of a string is obtained by moving characters
from the beginning of the string to the end of the string. We also consider a string to be a cyclic
shift of itself. For example, the cyclic shifts of ABCDE are:
ABCDE, BCDEA, CDEAB, DEABC, and EABCD. '''


total_text = str(input(''))
desired_text = str(input(''))


def string(t, s):

    desired_string = t 
    desired_permutations = [desired_string]
    for i in range(len(t)):
        last_letter = desired_string[-1]
        t_updated = last_letter + desired_string[:-1]   
        desired_string = t_updated
        desired_permutations.append(desired_string)


    string = s
    for i in range(len(s)):
        for t in desired_permutations:
            if t in string:
                return 'yes'
        
        last_letter = string[-1]
        s_updated = last_letter + string[:-1]
        string = s_updated
    
    return 'no'

            

print(string(desired_text, total_text))