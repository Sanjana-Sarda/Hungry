import numpy as np


"""
Compute transition function needs to update the state
s0 = np.zeros((20, 1))
"""
# decay_rate = [2, 2, 2, 2, 2, 4, 2, 3, 4, np.inf, np.inf, 12, 2, 2, 1, 2, 12, np.inf, 12, 12]

def compute_transition(num_states, num_actions):

    t_matrix_list = []

    for i in range(num_actions):
        temp_matrix = np.zeros((num_states, num_states))
        for j in range(num_states):
            if j+i < num_states:
                temp_matrix[j, j+i] = 1
            else:
                temp_matrix[j, j] = 1
        t_matrix_list.append(temp_matrix)

    return t_matrix_list


t_matrices = compute_transition(5, 5)
print(t_matrices[1])