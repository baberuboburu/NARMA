from src.config.config import * 
import numpy as np


class BASE():
  def __init__(self, lr: float = 1e-3, epochs: int = 1000):
    # NARMA2 Params
    self.alpha2 = ALPHA2
    self.beta2 = BETA2
    self.gamma2 = GAMMA2
    self.delta2 = DELTA2

    # NARMA10 Params
    self.alpha10 = ALPHA10
    self.beta10 = BETA10
    self.gamma10 = GAMMA10
    self.delta10 = DELTA10

    # Common
    self.sigma = SIGMA
    self.training_ratio = TRAINING_RATIO
    self.lr = lr
    self.epochs = epochs


  def nrmse(self, y_pred, y_target):
    mse = np.mean((y_pred - y_target) ** 2)
    variance = np.var(y_target)
    nrmse = np.sqrt(mse / variance)
    return nrmse
