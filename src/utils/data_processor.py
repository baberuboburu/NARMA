import os
import pandas as pd
from src.config.config import *


class DataProcessor():
  def __init__(self):
    self.data_file_path = data_file_path
    self.sampling_rate = sampling_rate
    self.sampling_width = sampling_width
    self.input_columns = input_columns
    self.output_columns = output_columns


  def run(self):
    if not os.path.isfile(self.data_file_path):
      raise FileNotFoundError(f"{self.data_file_path} is not found.")

    df = pd.read_csv(self.data_file_path)

    # Sampling data
    df = self.sampling(df)

    # start index & end index
    start = start_index // self.sampling_width
    end = end_index // self.sampling_width

    # Check bounds
    if end > len(df):
      raise ValueError(f"Insufficient data points: required {end}, but found {len(df)}")

    # V1〜V7 を取り出して return
    input_df = df.loc[start:end+discard_index-1, self.input_columns]
    output_df = df.loc[start:end+discard_index-1, self.output_columns]
    output_df = self.reproduce_data(output_df)

    if output_df.shape[0] < input_df.shape[0]:
      n = output_df.shape[0]
      input_df = input_df.iloc[:n]

    return input_df, output_df
  

  def sampling(self, df: pd.DataFrame):
    # Select every `sampling_width`-th row starting from the first row
    return df.iloc[::self.sampling_width].reset_index(drop=True)
  

  def reproduce_data(self, df: pd.DataFrame):
    """
    Reshape the input DataFrame to shape (n // sampling_width, 7 * sampling_width)
    by trimming the end so that n is divisible by sampling_width.

    Args:
      df (pd.DataFrame): Input DataFrame with shape (n, 7)

    Returns:
      pd.DataFrame: Reshaped DataFrame with shape (n // sampling_width, 7 * sampling_width)
    """
    n = df.shape[0]
    trimmed_n = (n // self.sampling_width) * self.sampling_width
    trimmed_df = df.iloc[:trimmed_n]

    reshaped = trimmed_df.values.reshape(-1, df.shape[1] * self.sampling_width)
    return pd.DataFrame(reshaped)

