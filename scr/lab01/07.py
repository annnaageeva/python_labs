from string import *
set_in = input("in: ")
result = ""
upper = ascii_uppercase
is_digits = digits
ind = []

for i in range(len(set_in) - 1):
    if set_in[i] in upper:
        result += set_in[i]
        ind.append(i)
    if set_in[i] in is_digits:
        ind.append(i)
        break
different = ind[1] - ind[0] 

for i in set_in[ind[1] + 1::different + 1]:
    result += i
print(f"out: {result}")