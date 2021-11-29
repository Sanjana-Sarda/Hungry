

# go through items to get upper bound. This needs to be generous so the model isn't surprised later
# discretize based on "possible actions" -- like 32 for sugar, 1 for milk, etc. 
# get MAX_POSSIBLE_ACTIONS
# create action space, with action space size being MAX_POSSIBLE_ACTIONS
# Initialize reward based on possible actions vector, with not possible actions being -inf

# tbh i think our model can output weird numbers of actions to take, it's not perfect :)

import json

def get_data(dirpath):
    with open(dirpath, "r") as fb:
        return json.load(fb)

def get_items_and_bounds(data):
    items = {}
    for purchase in data:
        product = purchase['product']
        if product in items:
            if items.get(product)['bound'] < purchase['amount']:
                items.get(product)['bound'] = purchase['amount']
        else:
            items[product] = {"bound" : purchase['amount'], "unit" : purchase['unit'] }
    return items






def main():
    data = get_data("/Users/natbishay/Hungry/data.json")
    items = get_items_and_bounds(data)
    print(data)

main()