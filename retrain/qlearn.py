from os import write
import numpy as np
import pandas as pd
import random
import sys
import time


num_of_observations = 50000
max_steps = 100
alphas = np.linspace(1.0, 0.2, 100)
alpha = 1.0
gamma = 1.0
eps = 0.2
q_table = dict()

def q_value(state, action=None):
    if state not in q_table:
        q_table[int(state)] = np.zeros(len(actions))
    if action is None:
        return q_table[state]
    return q_table[state][action]

def action(state):
    if random.uniform(0, 1) < eps:
        return random.choice(actions)
    else:
        return np.argmax(q_value(state))+1     

def setup(D):
    global actions 
    #actions = [1, 2, 3, 4, 5, 6, 7] #
    actions = D['a'].unique()
    print(actions)
    #for o in range (num_of_observations):
        #state = start_state
        
    for epochs in range (100):    
        alpha = alphas[epochs]
        for o in range (D.shape[0]):
            state, action, reward, next_state = D.iloc[o]
        
        #action = action(state)
        #next_state, reward, done = act(state, action)
            q_value(state)[int(action)-1] = q_value(state, int(action)-1) + alpha*(reward+gamma*np.max(q_value(next_state)) - q_value(state, int(action)-1))
        #state = next_state
        #if done:
            #break

def make_policy(n):
    act = []
    for s in range(n):
        act.append(action(s+1))
    return act
        

def write_policy(action, filename):
    with open(filename, 'w') as f:
        for a in action:
            f.write("{}\n".format(a))



def compute(infile, n, outfile):
    start = time.time()
    D = pd.read_csv(infile) #dataset   
    setup(D)
    #if(infile=="milk.csv"):
     #   n = 4
    #elif(infile=="orange1.csv"):
     #   n = 5
    #elif(infile=="bread.csv"):
     #   n = 3
    action = make_policy(int(n))
    write_policy(action, outfile)
    #vars = D.nunique(axis=0)
    #print(vars)
    print (time.time()-start)
