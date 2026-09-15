n = int(input())
onl = 0
offl = 0 

for i in range(n):
    inf = input(f"in_{i + 1} ").split()
    if inf[3] == "True":
        offl += 1
    else:
        onl += 1

print(offl, onl)
        