import random
test_seed=int(input("create a seed number"))
random.seed(test_seed)

rand_side=random.randint(0,1)

if rand_side==1:
    print("Heads")
else:
    print("Tails")
