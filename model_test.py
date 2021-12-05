# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:18:04 2021

@author: MeghanaBharadwaj
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Policy array order: [oranges milk bread flour onions]
def eval_model():

    bread = pd.read_csv("Policies/Bread.policy", header=None).to_numpy()
    orange = pd.read_csv("Policies/Oranges.policy", header=None).to_numpy()
    milk = pd.read_csv("Policies/Milk.policy", header=None).to_numpy()
    onion = pd.read_csv("Policies/Onions.policy", header=None).to_numpy()
    flour = pd.read_csv("Policies/Flour.policy", header=None).to_numpy()

    # Get test data 
    
    test_data = pd.read_csv('Test - Actual Test Data.csv')
    baseline_policies_list = np.zeros((5, 8))
    optimal_policies_list = np.zeros((5, 8))
    optimal_reward_list = np.zeros((5, 8))
    baseline_reward_list = np.zeros((5, 8))
    actual_action_list = np.zeros((5, 8))
    actual_reward_list = np.zeros((5, 8))
    
    for i in range(8):
        curr_time = test_data.iloc[i*5:i*5 + 5]

        state = curr_time["State"].to_numpy().reshape((5, 1))
        action = curr_time["Action "].to_numpy().reshape((5, 1))
        #cost = np.array([0.107994, 0.764595, 0.362859,0.466532, 0.233266]).reshape((5, 1)) 
        cost = curr_time["Cost"].to_numpy().reshape((5, 1))
        total_use = curr_time["Total Use"].to_numpy().reshape((5, 1))
        actual_use = curr_time["Actual Use"].to_numpy().reshape((5, 1))
        expired = curr_time["Expired"].to_numpy().reshape((5, 1))
        reward = curr_time["Reward"].to_numpy().reshape((5, 1))
                
        # Get policies
        opt_policy = np.zeros((5, 1))
        opt_policy[0] = orange[state[0]]
        opt_policy[1] = milk[state[1]]
        opt_policy[2] = bread[state[2]]
        opt_policy[3] = flour[state[3]]
        opt_policy[4] = onion[state[4]]
        
        # Get baseline policies
        baseline_policy = np.random.randint(1, 7, (5, 1))
        
        # Compute optimal policy reward
        optimal_reward = compute_reward(state, cost, opt_policy, expired, total_use, actual_use)
        
        # Compute baseline policy reward
        baseline_reward = compute_reward(state, cost, baseline_policy, expired, total_use, actual_use)
    
        # Add computed information to lists
        baseline_policies_list[:, i] = baseline_policy.reshape((5,))
        optimal_policies_list[:, i] = opt_policy.reshape((5,))
        optimal_reward_list[:, i] = optimal_reward.reshape((5,))
        baseline_reward_list[:, i] = baseline_reward.reshape((5,))
        actual_action_list[:, i] = action.reshape((5,))
        actual_reward_list[:, i] = reward.reshape((5,))
    
    return baseline_policies_list, optimal_policies_list, optimal_reward_list, baseline_reward_list, actual_action_list, actual_reward_list
    

def compute_reward(state, cost, action, expired, total_use, actual_use):

    total_use = np.minimum(state + action, total_use)
    expired = total_use - actual_use
    
    # cost * (action - 1) - (5 * cost*Expired) + (5*used)
    reward = -cost*(action - 1) - (0.5* expired) + (0.5* actual_use)
    return reward
        
        
bpl, opl, orl,brl, aal, arl = eval_model()
print("Baseline Policy:", bpl)
print("Optimal Policy:", opl)
print("Actual Actions:", aal)

print("Baseline Reward:", brl)
print("Optimal Rewards List:", orl)
print("Actual Reward:", arl)

plt.plot([brl.T)
