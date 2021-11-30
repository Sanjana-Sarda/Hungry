
import numpy as np

# don't want to do anymore until we figure out if we can even input dicts into an MDP solver
# reward function needs to take prices into account so it can be MDP solvable...

def initialize_reward(action_space):
    # This function initializes eligible rewards to 0 and ineligible rewards to -infinity.
    state_space_size, action_space_size = np.shape(action_space)
    reward = np.zeros((state_space_size, action_space_size))
    for i in range(state_space_size):
        for j in range(action_space_size):
            reward[i,j] = -np.Inf if action_space[i,j] == 0 else 0
    return reward


def update_reward(actions, opt_actions, reward):
    # actions is an array of size state_space_size x action_space_size
    # opt_actions is a vector of index to optimal amounts to purchase
    # reward is an array of size state_space_size x action_space_size

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