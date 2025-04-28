from src.config.config import *
import os


class ArrangeData():
  def __init__(self):
    self.directory_path = data_directory_path


  def run(self):
    if not os.path.isdir(self.directory_path):
      print("Directory is not found.")
      return

    csv_files = [
      os.path.join(self.directory_path, f)
      for f in os.listdir(self.directory_path)
      if f.endswith(".csv") and os.path.isfile(os.path.join(self.directory_path, f))
    ]

    if not csv_files:
      print("No CSV files found.")
      return

    for file_path in csv_files:
      self._process_file(file_path)


  def _process_file(self, file_path: str):
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
      lines = f.readlines()

    # "sec," の行を探す（これ以降が必要）
    header_idx = None
    for i, line in enumerate(lines):
      if line.startswith("sec,"):
        header_idx = i
        break

    if header_idx is None:
      print(f"[{os.path.basename(file_path)}] Header not found.")
      return

    header = lines[header_idx].strip().split(',')

    # 整形済みチェック
    if header[1].startswith("V1"):
      print(f"[{os.path.basename(file_path)}] Already arranged.")
      return

    # 新しいヘッダー生成
    new_header = ['time'] + [f'V{i+1}' for i in range(len(header) - 1)]
    lines[header_idx] = ','.join(new_header) + '\n'

    # ヘッダー行から最後までを再構成して保存
    trimmed_lines = lines[header_idx:]

    with open(file_path, 'w', newline='', encoding='utf-8') as f:
      f.writelines(trimmed_lines)

    print(f"[{os.path.basename(file_path)}] Arranged successfully.")