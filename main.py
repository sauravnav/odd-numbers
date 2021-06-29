l = [1, 3, 5,7] #9  11
n = int(input("enter numbers of next odd number you want to print:"))
d = l[-1]
for i in range(n): #0 1
    e = d+2   # 0 11
    l.append(e)  #9 11
    d = l[-1]   # 9 0
print(l)