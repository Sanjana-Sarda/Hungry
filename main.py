import numpy as np
import reward as rw
import create_actions as ca

def main():
    data = ca.get_data("/Users/natbishay/Hungry/data.json")
    items = ca.get_items_and_bounds(data)
    #state_space, action_space = ca.discretize_action_and_state_space(items)
    print(items)
   # reward = rw.initialize_reward(action_space)
    #week_actions = rw.get_week_actions(data, items)
    #print(week_actions)

main()
