from dnnv.properties import *
import numpy as np

N = Network("N")
lb = -np.ones((1, 2))
ub = np.ones((1, 2))

Forall(x, Implies(lb <= x <= ub, N(x) >= 1))
