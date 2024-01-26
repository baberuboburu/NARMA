import numpy as np
import pandas as pd
from typing import List
import param


# 変数の取得
num_data = param.num_data
up_scale = param.up_scale
bottom_scale = param.bottom_scale
file_path_input = param.file_path_input
data_columns = param.data_columns


class Arrange():
  def __init__(self, sampling_rate: float):
    self.columns = data_columns
    self.columns_input = ['input']
    self.sampling_rate = sampling_rate


  def arrange(self, file_path: str):
    # データの読み込み
    df = pd.read_csv(file_path)
  
    # コラムの調整
    df = self.set_column(df, columns=self.columns, flag=True)
  
    # 不要コラムの削除
    df = self.del_column(df, 'trash')
  
    # データをピックアップして配列にする
    time = self.pick_up_data(df, 'time')
    input = self.pick_up_data(df, 'input')
    output = self.pick_up_data(df, 'output')

    return time, input, output
  
  
  # 1行目のデータをコラムからデータにし，コラム名を新しく設定する
  def set_column(self, df, columns: List[str], flag=False):
    data_0_list = df.columns.tolist()
    for i in range(len(data_0_list)):
      data_0_list[i] = float(data_0_list[i])
    data_0 = pd.DataFrame([data_0_list], columns=columns)
    df.columns = columns
    df = pd.concat([data_0, df], axis=0).reset_index(drop=True)
    if flag == True:
      df.iloc[:, 1] = -1 * df.iloc[:, 1]
    return df
  
  
  def del_column(self, df, column_name: str):
    df = df.drop(column_name, axis=1)
    return df
  
  
  def pick_up_data(self, df, column_name: str):
    pulse_width = int(df.shape[0]/num_data)
    start = self.sampling_rate * 50
    
    selected_data = df.iloc[start::pulse_width]
    col_data = selected_data[column_name].tolist()
    return col_data
  

  def arrange_input(self):
    df = pd.read_csv(file_path_input)
    df = self.set_column(df, self.columns_input)
    input = np.array(df['input'].tolist())
    input_min = input.min()
    input_max = input.max()
    normalized_data = (input - input_min) / (input_max - input_min)
    scaled_input = normalized_data * (up_scale - (bottom_scale)) + (bottom_scale)
    return scaled_input
  

# 使用例
# file_path = '../data/1-3-1ms_t.csv'
# time, input, output = Arrange().arrange(file_path)