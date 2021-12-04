

# go through items to get upper bound. This needs to be generous so the model isn't surprised later
# discretize based on "possible actions" -- like 32 for sugar, 1 for milk, etc. 
# get MAX_POSSIBLE_ACTIONS
# create action space, with action space size being MAX_POSSIBLE_ACTIONS
# TODO
# Initialize reward based on possible actions vector, with not possible actions being -inf

# tbh i think our model can output weird numbers of actions to take, it's not perfect :)

import json
import numpy as np

def get_data(dirpath):
    with open(dirpath, "r") as fb:
        return json.load(fb)

items_dict = {
    "whole milk",
    "Strawberries",
    "medium yellow onions",
    "sugar",
    "butter"
}

def get_items_and_bounds(data):
    # currently, this function only calculates the bound as the highest amount it finds. We can make this looser.
    items = {}
    ind = 0
    for purchase in data:
        product = purchase['product']
        if product in items_dict: 
            if product in items: # if we've seen the product, change the bound if the one we've found is higher
                if items.get(product)['bound'] < purchase['amount']:
                    items.get(product)['bound'] = purchase['amount']
            else: # if we haven't seen the product, add it to the dictionary
                items[product] = { "bound" : purchase['amount'], "unit" : purchase['unit'], 'num' : ind }
                ind = ind + 1
    return items

# this is increments that we can find of all of the type of units, so we can step accordingly. 
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

def discretize_action_and_state_space(items):

    # start with action space of size 0 so as to update it
    action_space_size = 0
    # state space is the amount of items we have
    item_space_size = len(items)
    # iterate through the items to get the largest action space
    for name in items:
        item = items.get(name)
        step_size = step_size_dict.get(item['unit'])
        num_actions = int(item['bound']/step_size)
        if num_actions > action_space_size:
            action_space_size = 2*(num_actions) + 1
            state_space_size = action_space_size
    
    # now, we create the action space as the size of the largest action space previously calculated
    action_space = np.zeros((item_space_size, action_space_size))
    state_space = np.zeros((item_space_size, state_space_size))
    for name in items:
        item = items.get(name)
        step_size = step_size_dict.get(item['unit'])
        num_actions = 2*int(item['bound']/step_size)
        ind = item['num']
        action = 0
        action_space[ind, 0] = 0
        state_space[ind, 0] = 0
        for i in range(num_actions-1):
            action =  action + step_size
            action_space[ind, i+1] = action
            state_space[ind, i+1] = action
        action_space[ind, num_actions] = 2*item['bound']
        state_space[ind, num_actions] = 2*item['bound']

    return state_space, action_space