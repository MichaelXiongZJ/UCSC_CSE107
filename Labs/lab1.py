import random

def flip_a_coin(pHead):
    outcome = random.random()
    if outcome <= pHead:
        return True
    else:
        return False

def run_test(pHead, num_of_trials):
    num_of_bob_more_head = 0
    for i in range(num_of_trials):
        #bob
        bob_heads = 0
        for k in range(n_of_bob):
            if flip_a_coin(pHead):
                bob_heads += 1
        #alice
        alice_heads = 0
        for k in range(n_of_alice):
            if flip_a_coin(pHead):
                alice_heads += 1
        #count times of bob more heads
        if bob_heads > alice_heads:
            num_of_bob_more_head += 1
    relative_frequency = num_of_bob_more_head/num_of_trials
    return relative_frequency

#numbers of coins
n_list = (5, 10, 50, 100)

#number of trials
num_of_trials = 1000

#probabilities of head of coin
pHead_fair = 0.5
pHead_loaded_list = (0.2, 0.3, 0.4, 0.6, 0.7, 0.8)

for n in n_list:
    print("\n================= For n =", n, "=================")
    n_of_bob = n + 1
    n_of_alice = n
    relative_frequency_fair = run_test(pHead_fair, num_of_trials)
    print("Fair:")
    print("     P(head) =", pHead_fair, ", Relative frequency =", relative_frequency_fair)
    print("Loaded:")
    for pHead_loaded in pHead_loaded_list:
        relative_frequency_loaded = run_test(pHead_loaded, num_of_trials)
        print("     P(head) =", pHead_loaded, ", Relative frequency =", relative_frequency_loaded)