import random
import copy

def flip_a_coin(probability):
    outcome = random.random()
    if outcome <= probability:
        return True
    else:
        return False

def init_XY_table(n):
    XYresult = []
    for i in range(n+1):
        col = []
        for j in range(n+1):
            col.append(0)
        XYresult.append(col)
    return XYresult

def convert_to_relative_frequency(table, num_trials):
    for i in range(n+1):
        for j in range(n+1):
            table[i][j] /= num_trials

def run_test(num_trials, n, p, q, table):
    for i in range(num_trials):
        x = 0
        y = 0
        for j in range(n):
            if(flip_a_coin(p)):
                x += 1
                if(flip_a_coin(q)):
                    y += 1
        table[x][y] += 1
    convert_to_relative_frequency(table, num_trials)

def getPx(table):
    arr = []
    for row in table:
        px = 0
        for i in row:
            px += i
        arr.append(px)
    return arr

def getPy(table):
    arr = [0]*len(table)
    for row in table:
        for i in range(len(row)):
            arr[i] += row[i]
    return arr

def getXgivenY(pXY, pY):
    table = copy.deepcopy(pXY)
    for row in table:
        for i in range(len(row)):
            row[i] /= pY[i]
    return table

def getYgivenX(pXY, pX):
    table = copy.deepcopy(pXY)
    for i in range(len(table)):
        for j in range(len(table)):
            table[i][j] /= pX[i]
    return table

def print_table(table):
    print("    y:\t0\t1\t2\t3\t4\t5\t6\t7\t8")
    print("x  ---------------------------------------------------------------------------")
    for i in range(len(table)):
        print(i, "|", end="\t")
        for j in range(i+1):
            print("%.4f\t" % table[i][j], end='')
        print()

n = 8
p = 0.6
q = 0.7
num_trials = 100000

pXY = init_XY_table(n)

run_test(num_trials, n, p, q, pXY)

pX = getPx(pXY)
pY = getPy(pXY)

pXgivenY = getXgivenY(pXY, pY)
pYgivenX = getYgivenX(pXY, pX)

print("Joint PMF of X and Y")
print_table(pXY)

print("\nConditional PMF of X given Y")
print_table(pXgivenY)

print("\nConditional PMF of Y given X")
print_table(pYgivenX)