


# don't want to do anymore until we figure out if we can even input dicts into an MDP solver

def update_reward(actions, opt_actions, reward):
    # actions is a dictionary of lists
    # opt_actions is a vector of index to optimal amounts to purchase
    # reward is a dictionary of lists

    # might need to create a way to update these as time goes on, something to think about
    lessPenalty = 0.7
    wastePenalty = 1

    # This iteration works based on the fact that the rewards and actions are organized 
    # in increasing order; i.e. 3 apples, 5 apples, 7 apples. 
    for item, rewards in reward.items():
        best_action_index = opt_actions.get(item)
        best_action = actions.get(item)[best_action_index]
        for i, action_reward in enumerate(rewards):
            if i < best_action_index:
                rewards[i] = action_reward - lessPenalty*abs(action_reward-best_action)
            if i > best_action_index:
                rewards[i] = action_reward - wastePenalty*abs(action_reward-best_action)
            if i == best_action_index:
                rewards[i] = action_reward + 1