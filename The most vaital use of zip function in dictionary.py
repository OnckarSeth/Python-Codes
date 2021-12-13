names = []
rolls = []
a = int(input("the number of wanting value: "))
for i in range(1, a+1):
    b = input("Enter the name: ")
    names.append(b)
    c = int(input("Enter the roll number: "))
    rolls.append(c)
d = dict(zip(names, rolls))
while (True):
    e = input("enter the names: ")
    if e == "q":
        break
    
    else:
        
        print(d[e])
        continue
