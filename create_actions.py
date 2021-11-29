

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

def get_items_and_bounds(data):
    # currently, this function only calculates the bound as the highest amount it finds. We can make this looser.
    items = {}
    for purchase in data:
        product = purchase['product']
        if product in items: # if we've seen the product, change the bound if the one we've found is higher
            if items.get(product)['bound'] < purchase['amount']:
                items.get(product)['bound'] = purchase['amount']
        else: # if we haven't seen the product, add it to the dictionary
            items[product] = { "bound" : purchase['amount'], "unit" : purchase['unit'] }
    return items

# this is increments that we can find of all of the type of units, so we can step accordingly. 
step_size_dict = { "gallon": 0.5, 
              "lb" : 0.5,
              "pack": 1,
              "box": 1,
              "single": 1,
              "oz": 1,
              "crown": 1,
              "pack": 6,
              "count": 1
            }

def discretize_action_space(items):

    # start with action space of size 0 so as to update it
    action_space_size = 0
    # state space is the amount of items we have
    state_space_size = len(items)
    # iterate through the items to get the largest action space
    for name in items:
        item = items.get(name)
        step_size = step_size_dict.get(item['unit'])
        num_actions = int(item['bound']/step_size)
        if num_actions > action_space_size:
            action_space_size = num_actions
    
    # now, we create the action space as the size of the largest action space previously calculated
    action_space = np.zeros((state_space_size, action_space_size))
    for ind, name in enumerate(items):
        item = items.get(name)
        step_size = step_size_dict.get(item['unit'])
        num_actions = int(item['bound']/step_size)
        action = 0
        for i in range(num_actions):
            action =  action + step_size
            action_space[ind, i] = action
    
    return action_space


def main():
    data = get_data("/Users/natbishay/Hungry/data.json")
    items = get_items_and_bounds(data)
    action_space = discretize_action_space(items)
    print(items)
    print(action_space)

main()