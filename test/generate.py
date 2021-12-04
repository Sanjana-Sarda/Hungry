from os import write
import numpy as np
import pandas as pd
import random
import sys
import time


def policyit(b, item, num, use, state):
    #policy = pd.read_csv("../train/"+item+".policy", header=None).to_numpy()
    policy = pd.read_csv("../retrain/"+item+".policy", header=None).to_numpy()
    #state = 1
    pol = []
    for a in range (int(num)):
        p = int(policy[state-1][0])
        state = state + p - use[a][b]
        if (state==0):
            p = p+1
            state = state+1
        pol.append(p)
        
    return pol

def generate (litems, num): 
    use = pd.read_csv("ret_use.csv", header=None).to_numpy()
    use = use[0].reshape(int(num), len(litems))
    actions = np.zeros((int(num), len(litems)))
    states = [3, 2, 2, 2, 2]
    for a in range (len(litems)):
        actions[:,a] =  policyit(a, litems[a], num, use, states[a])
    write_policy(actions.flatten())
    
def write_policy(action):
    with open("ret_automated", 'w') as f:
        for a in action:
            f.write("{}\n".format(int(a)))

def compute(items, num):
    start = time.time()
    litems = pd.read_csv(items).columns.values #items   
    generate(litems, num)
    print (time.time()-start)
    

def main():
    if len(sys.argv) != 3:
        raise Exception("usage: python generate.py items num")

    items = sys.argv[1]
    num = sys.argv[2]
    compute(items, num)


if __name__ == '__main__':
    main()