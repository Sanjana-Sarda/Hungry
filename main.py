import numpy as np
import reward as rw
import create_actions as ca

def main():
    data = ca.get_data("/Users/natbishay/Hungry/data.json")
    items = ca.get_items_and_bounds(data)
    action_space = ca.discretize_action_space(items)
    reward = rw.initialize_reward(action_space)

main()
