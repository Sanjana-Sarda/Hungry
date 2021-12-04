
import numpy as np

# don't want to do anymore until we figure out if we can even input dicts into an MDP solver
# reward function needs to take prices into account so it can be MDP solvable...

def initialize_reward(action_space):
    # This function initializes eligible rewards to 0 and ineligible rewards to -infinity.
    state_space_size, action_space_size = np.shape(action_space)
    reward = np.zeros((state_space_size, action_space_size))
    for i in range(state_space_size):
        for j in range(action_space_size):
            if j == 0: # this is wrong
                reward[i,j] = 0
            else:
                reward[i,j] = -np.Inf if action_space[i,j] == 0 else 0
    return reward


def update_reward(opt_actions, reward):
    # actions is an array of size state_space_size x action_space_size
    # opt_actions is a vector of index to optimal amounts to purchase
    # reward is an array of size state_space_size x action_space_size

    # might need to create a way to update these as time goes on, something to think about
    lessPenalty = 0.7
    wastePenalty = 1

    # This iteration works based on the fact that the rewards and actions are organized 
    # in increasing order; i.e. 3 apples, 5 apples, 7 apples. 
    for ind, item_reward in enumerate(reward):
        best_action = opt_actions[ind]
        for i, action_reward in enumerate(item_reward):
            if action_reward < best_action:
                item_reward[i] = action_reward - lessPenalty*abs(action_reward-best_action)
            if action_reward > best_action:
                item_reward[i] = action_reward - wastePenalty*abs(action_reward-best_action)
            if action_reward == best_action:
                item_reward[i] = action_reward + 1

step_size_dict = { "gallon": 0.5, 
              "lb" : 0.5,
              "pack": 1,
              "box": 1,
              "single": 1,
              "oz": 4,
              "crown": 1,
              "pack": 6,
              "count": 1
            }

items_dict = {
    0 : "whole milk",
    1 : "medium yellow onions",
    2 : "sugar",
    3 : "butter",
    4 : "Strawberries",
}

def new_reward_update(obs, state, rewards, items):
    # observations is a 5 item vector
    # states are the previous amounts you have, a 5 item vector
    # reward is a 5 element dict of 
    opt_amounts = obs + state
    
    for item_amount in opt_amounts: # get the optimal amount
            for reward in rewards.keys():


                






def get_week_actions(data, items):
    week_actions = {}
    date = 0
    for purchase in data:
        currentdate = purchase['date']
        product = purchase['product']
        ind = items.get(product)['num']
        if date != currentdate: # we've moved to a new date, start a new list
            date = currentdate
            week_actions[date] = np.zeros((len(items)))
            week_actions.get(date)[ind] = purchase['amount']
        if date == currentdate:
            week_actions.get(date)[ind] = purchase['amount']

    return week_actions

#def first_reward_creation(actions, reward):
