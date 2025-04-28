from src.config.config import *
from src.components.base import BASE
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm


class NARMA2(BASE):
  def __init__(self):
    super().__init__()


  def fit_predict(self, input_df: pd.DataFrame, target_df: pd.DataFrame):
    """
    Perform ridge regression using torch with optional scaled target, return prediction and NRMSE.

    Args:
      input_df (pd.DataFrame): Input features of shape (T, 7)
      target_df (pd.DataFrame): Target values of shape (T, 1) with column 'y_k'

    Returns:
      Tuple of:
        - pd.DataFrame with one column 'y_hat' (predictions)
        - float value of NRMSE
    """
    # Scaling
    if is_scaling == 'min_max':
      scaler = MinMaxScaler()
      y_scaled = scaler.fit_transform(target_df.values)
    else:
      scaler = None  # スケーラを無効化
      y_scaled = target_df.values  # そのまま使う

    # Convert to tensors
    X = torch.tensor(input_df.values, dtype=torch.float32)
    y = torch.tensor(y_scaled, dtype=torch.float32)

    # Define ridge regression model
    class RidgeModel(nn.Module):
      def __init__(self, input_dim: int, alpha: float):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1, bias=True)
        self.alpha = alpha

      def forward(self, x):
        return self.linear(x)

      def l2_penalty(self):
        return self.alpha * torch.sum(self.linear.weight ** 2)

    model = RidgeModel(input_dim=X.shape[1], alpha=self.alpha2)
    optimizer = optim.Adam(model.parameters(), lr=self.lr)
    criterion = nn.MSELoss()

    # Training loop
    for _ in tqdm(range(self.epochs)):
      model.train()
      optimizer.zero_grad()
      output = model(X)
      loss = criterion(output, y) + model.l2_penalty()
      loss.backward()
      optimizer.step()

    # Predict
    model.eval()
    with torch.no_grad():
      y_pred_scaled = model(X).squeeze().numpy().reshape(-1, 1)

      if scaler is not None:
        # スケールを戻す
        y_pred = scaler.inverse_transform(y_pred_scaled).squeeze()
      else:
        # そのまま
        y_pred = y_pred_scaled.squeeze()

    pred_df = pd.DataFrame({'y_hat': y_pred})

    # NRMSE計算
    y_target = target_df['y_k'].values.squeeze()
    nrmse = self.nrmse(y_pred, y_target)

    # Debug prints
    print("Target y_k min/max:", target_df['y_k'].min(), target_df['y_k'].max())
    print("Predicted (before inverse_transform) min/max:", y_pred_scaled.min(), y_pred_scaled.max())
    if scaler is not None:
      print("Predicted (after inverse_transform) min/max:", y_pred.min(), y_pred.max())

    return pred_df, nrmse

  
  def prepare_target(self, input_data: pd.DataFrame):
    """
    Create target data as a pandas DataFrame based on the NARMA2 model.

    Args:
      input_data (pd.DataFrame): Input data with one column 'input_column'.

    Returns:
      pd.DataFrame: Target data with one column 'y_k'.
    """
    u_k = input_data[input_columns].values
    y_k = np.zeros_like(u_k)
    
    # Initialize first 2 values to 0
    for i in range(2):
      y_k[i] = 0

    for k in range(2, len(u_k)):
      y_k[k] = (
      self.alpha2 * y_k[k - 1]
      + self.beta2 * y_k[k - 1] * y_k[k - 2]
      + self.gamma2 * u_k[k] * u_k[k - 1]
      + self.delta2
    )
    y_k = y_k.squeeze()
    y_k = y_k[discard_index:]

    return pd.DataFrame({'y_k': y_k})