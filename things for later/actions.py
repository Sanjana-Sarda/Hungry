actions = dict()

def add_action(product, quantity):
    if product not in actions:
        actions[product] = [0, quantity]
    else:
        actions[product] = actions[product].append(quantity)
