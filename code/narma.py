import numpy as np
from typing import List


class NARMA():
  def __init__(self, m: int, a1: float, a2: float, a3: float, a4: float):
    self.m = m
    self.a1 = a1
    self.a2 = a2
    self.a3 = a3
    self.a4 = a4


  def narma(self, time: int, input: List[float], d_init: List[float]):
    n = self.m
    d = d_init

    while n < time:
        d_n = self.a1*d[n-1] + self.a2*d[n-1]*d[n-2] + self.a3*(input[n-1]**3) + self.a4
        d.append(d_n)
        n += 1

    return np.array(d)