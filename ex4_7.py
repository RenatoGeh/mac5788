import numpy as np
import numpy.random

all_states = []
max_n, max_m = 20, 20

def poisson_sample(l):
  return np.random.poisson(l)

def get_state(n, m):
  return all_states[m+n*max_n]

def init_env():
  for i in range(0, max_n):
    for j in range(0, max_m):
      all_states.append(State(i, j))

class State:
  # Number of cars in each location.
  n = 0
  m = 0

  def __init__(self, n, m):
    self.n = n
    self.m = m

  # Returns possible actions from this state, and their respective rewards.
  def actions(self):
    A = []
    l_n, l_m = max(0, n-5), max(0, m-5)
    u_n, u_m = min(20, n+5), min(0, m+5)
    dln, dun = self.n-l_n, u_n-self.n
    dlm, dum = self.m-l_m, u_m-self.m
    for i in range(l_n, self.n):
      A.append((dln << 1, get_state(i, self.m + dln)))
    for i in range(self.n, u_n):
      A.append((dun << 1, get_state(i, self.m + dun)))
    for j in range(l_m, self.m):
      A.append((dlm << 1, get_state(self.n + dlm, j)))
    for j in range(self.m, u_m):
      A.append((dum << 1, get_state(self.n + dum, j)))
    return A

class MDP:
  # Set of states.
  S = []
  # Set of actions.
  A = []
  # Discount rate.
  g = 0.9
  # Max number of cars in each location.
  max_n, max_m = 20, 20

  def __init__(self, max_n = 20, max_m = 20, g = 0.9):
    self.g = g
    self.max_n, self.max_m = max_n, max_m

