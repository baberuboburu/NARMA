import os
import numpy as np
from arrange import Arrange
import param


# 変数の取得
num_data = param.num_data
dir_path_data = param.dir_path_data


class GenerateWave():
  def __init__(self, sampling_rate: float):
    self.dir = dir_path_data
    self.sampling_rate = sampling_rate
    self.string = f'-{sampling_rate}ms'
    self.outputs = []

  
  def generate(self):
    file_paths = self.get_filepath()
    for file_path in file_paths:
      _, _, output = Arrange(sampling_rate=self.sampling_rate).arrange(file_path)
      self.outputs.append(output)
    outputs = np.array(self.outputs).reshape(num_data, 7)
    return outputs


  def get_filepath(self):
    file_paths = []
    for root, _, files in os.walk(self.dir):
      for file in files:
        if self.string in file:
          file_name = os.path.relpath(os.path.join(root, file), self.dir)
          file_path = os.path.join(self.dir, file_name)
          file_paths.append(file_path)
    return file_paths


# 使用例
# generate = GenerateWave('-1ms')
# data = g.generate()