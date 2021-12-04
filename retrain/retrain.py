from os import write
import numpy as np
import pandas as pd
import sys
import time
import qlearn as q


            
def updateobs(observations, items):
    obs = pd.read_csv(observations).sort_values(["Items"], ascending=True)
    obs = obs.set_index(["Items"])
    for item in (items):
        print (item)
        obs.loc[item].to_csv(item+'.csv', mode='a', index=False, header=False)

def compute(observations, items):
    start = time.time()
    litems = pd.read_csv(items).columns.values #items   
    #updateobs(observations, litems)
    #generate(litems, num)
    for item in litems:
        q.compute(item+".csv", 7, item+".policy")
    print (time.time()-start)
    
    
def main():
    if len(sys.argv) != 3:
        raise Exception("usage: python retrain.py observations.csv items")
    
    observations = sys.argv[1]
    items = sys.argv[2]
    compute(observations, items)


if __name__ == '__main__':
    main()