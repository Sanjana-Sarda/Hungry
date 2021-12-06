from os import write
import numpy as np
import pandas as pd
import random
import sys
import time


def policyit(b, item, num, total, state):
    #policy = pd.read_csv("../train/"+item+".policy", header=None).to_numpy()
    policy = pd.read_csv("../retrain/"+item+".policy", header=None).to_numpy()
    #state = 1
    pol = []
    states = []
    print (item)
    for a in range (int(num)):
        p = int(policy[int(state)-1][0])
        e = max(state -1 - total[a][b], 0) 
        state = max(state + p - total[a][b] - e -1, 1)
        pol.append(p)
        states.append(state)
        
    return pol, states

def generate (litems, num): 
    total = pd.read_csv("ret_use.csv", header=None).to_numpy()
    #total = pd.read_csv("total.csv", header=None).to_numpy()
    total = total[0].reshape(int(num), len(litems))
    actions = np.zeros((int(num), len(litems)))
    exp = np.zeros((int(num), len(litems)))
    states = [3, 2, 2, 2, 2]
    for a in range (len(litems)):
        actions[:,a], exp[:,a] =  policyit(a, litems[a], num, total, states[a])
    write_policy(actions.flatten(), exp.flatten())
    
def write_policy(action, exp):
    with open("ret_automated", 'w') as f:
    #with open("automated", 'w') as f:
        for a in action:
            f.write("{}\n".format(int(a)))
    with open("exp", 'w') as f:
        for e in exp:
            f.write("{}\n".format(int(e)))

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