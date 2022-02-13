# Problem 1 

s = input('')
m = input('')
l = input('')


def happiness(s, m, l):
    
    s = int(s)
    m = int(m)
    l = int(l)

    result = (1*s) + (2*m) + (3*l)
    if result >= 10:
        return 'happy' 
    else:
        return 'sad'

print(happiness(s, m, l))