n = 8

XYresult = []
for i in range(n):
    col = []
    for j in range(n):
        col.append(0)
    XYresult.append(col)

XYresult[4][3] += 1

for row in XYresult:
    for i in range(len(row)):
        print(i)