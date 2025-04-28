from src.components.base import BASE
import numpy as np
import pandas as pd


class NARMA10(BASE):
  def __init__(self):
    super().__init__()

  
  def predict(self):
    return

  
  def prepare_target(self, input_data: pd.DataFrame):
    """
    Create target data as a pandas DataFrame based on the NARMA10 model.

    Args:
      input_data (pd.DataFrame): Input data with one column 'u_k'.

    Returns:
      pd.DataFrame: Target data with one column 'y_k'.
    """
    u_k = input_data['u_k'].values
    y_k = np.zeros_like(u_k)
    
    # Initialize first 10 values to 0
    for i in range(10):
      y_k[i] = 0

    for k in range(10, len(u_k)):
      y_k[k] = (
        self.alpha10 * y_k[k - 1]
        + self.beta10 * y_k[k - 1] * np.sum(y_k[k - 10:k])
        + self.gamma10 * u_k[k] * u_k[k - 9]
        + self.delta10
      )

    return pd.DataFrame({'y_k': y_k})