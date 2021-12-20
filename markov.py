import numpy as np


def run_markov_chain(transition_matrix, n=10, print_transitions=False):
  """
    Takes the transition matrix and runs through each state of the
    Markov chain for n times step. When the chain reaches a steady
    state, returns the transition probabilities and the time step of the
    convergence.
    
      @params:
      - transition_matrix: transition probabilities
      - n: no of time steps to run. default is 10
      - print_transitions: tells if we want to print the transition matrix
      at each time step
  """
  
  setp = transition_matrix
  
  for time_step in range (1, n):
    if print_transitions:
      print('Transition Matrix at step:' + str(time_step))
      print(step)
      print('-------------------------')
      
    next_step = np.matmul(step, transition_matrix).round(2)
    
    if np.array_equal(step, next_step):
      print('Markov chain reached steady-state at time-step = ' + str(time_step))
      
      if not print_transitions:
        print(step)
        
      return step
    else:
      step = next_step
    return step
