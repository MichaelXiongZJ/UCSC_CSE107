import random
import copy
import numpy as np

# basically how i did was
# a matrix for mean
# a matrix for second moment
# a matrix for variance
# a list of all the probability
# loop i, p through list of prob(enumerate):
#   loop j, q through list of prob(enumerate): 
#     heads counter
#     second moment counter
#     loop through 10_000 trials:
#       n counter 
#       while:
#         flip a coin 
#         increment n
#         if coin is the prob(p):
#           break
#         else:
#           continue
#       loop through n:
#         flip a coin 
#         if coin is the prob(q):
#           increment heads
#       second moment = heads**2+second moment
#     after the trials are done set the heads counter and second     moment to their respective place in their matrices

def init_table(n):
    table = []
    for i in range(n):
        col = []
        for j in range(n):
            col.append(0)
        table.append(col)
    return table

def print_table(table):
    print("   q: ", end='')
    for i in prob_list:
        print("%.1f\t"%i, end='')
    print("\np    ------------------------------------------------------------------------")
    for i in range(len(table)):
        print("%.1f | "%prob_list[i], end='')
        for j in range(len(table[i])):
            print("%.3f\t" % table[i][j], end='')
        print()


prob_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
num_trial = 10000

mean_table = init_table(len(prob_list))
sec_moment_table = init_table(len(prob_list))
var_table = init_table(len(prob_list))

for p in prob_list:
    for q in prob_list:
        head_count = 0
        sec_moment_count = 0
        for i in range(num_trial):
            trial_head = 0
            n_count = 0
            while True:
                n_count += 1
                if(random.random() < p):
                    break
                else:
                    continue
            for j in range(n_count):
                if(random.random() < q):
                    trial_head += 1
            head_count += trial_head
            sec_moment_count += trial_head**2
        x = int(q*10 - 1)
        y = int(p*10 - 1)
        mean_table[y][x] = head_count/num_trial
        sec_moment_table[y][x] = sec_moment_count/num_trial
        var_table[y][x] = sec_moment_table[y][x] - (mean_table[y][x])**2

print("Mean")
print_table(mean_table)
print("\nVariance")
print_table(var_table)