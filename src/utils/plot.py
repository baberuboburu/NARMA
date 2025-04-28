from src.config.config import *
import os
import matplotlib.pyplot as plt
import pandas as pd


class Plot():
  def __init__(self):
    self.img_dir = img_directory_path
    if not os.path.exists(self.img_dir):
      os.makedirs(self.img_dir)


  def run(self, target_df: pd.DataFrame, pred_df: pd.DataFrame, filename: str = "narma_result.png"):
    """
    Plot predicted and target values, and save the figure as PNG.

    Args:
      target_df (pd.DataFrame): Ground truth with column 'y_hat'.
      pred_df (pd.DataFrame): Predicted values with column 'y_k'.
      filename (str): Output filename for the plot image.
    """
    # Plot
    plt.figure(figsize=(10, 4))
    plt.plot(target_df['y_k'].values, label='Target (y_hat)', linewidth=1.5)
    plt.plot(pred_df['y_hat'].values, label='Predicted (y_k)', linewidth=1.5)
    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.title("NARMA Task Result")
    plt.legend()
    plt.tight_layout()

    # Save
    path = os.path.join(self.img_dir, filename)
    plt.savefig(path)
    plt.close()

    print(f"Plot saved to: {path}")
  
  
  def input_wave(self, df: pd.DataFrame, filename: str = "input_wave.png"):
    """
    Plot a single input wave and save as PNG.

    Args:
      df (pd.DataFrame): Input signal of shape (T, 1).
      filename (str): Output filename for the plot image.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df.values, label=df.columns[0], linewidth=1)
    plt.xlabel("Time Step")
    plt.ylabel("Input Value")
    plt.title("Input Wave")
    plt.legend()
    plt.tight_layout()

    path = os.path.join(self.img_dir, filename)
    plt.savefig(path)
    plt.close()
    print(f"Input wave plot saved to: {path}")


  def output_wave(self, df: pd.DataFrame, filename: str = "output_wave.png"):
    """
    Plot all output waves in one figure and save as PNG.

    Args:
      df (pd.DataFrame): Output features of shape (T, 7).
      filename (str): Output filename for the plot image.
    """
    plt.figure(figsize=(10, 5))
    for col in df.columns:
      plt.plot(df[col].values, label=col, linewidth=1)

    plt.xlabel("Time Step")
    plt.ylabel("Output Value")
    plt.title("Output Waves")
    plt.legend(loc="upper right", ncol=3)
    plt.tight_layout()

    path = os.path.join(self.img_dir, filename)
    plt.savefig(path)
    plt.close()
    print(f"Output wave plot saved to: {path}")