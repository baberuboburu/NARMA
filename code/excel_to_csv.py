import pandas as pd


# パスの設定
file_name = 'input'
excel_file_path = f'../data/excel/{file_name}.xlsx'
csv_file_path = f'../data/csv/{file_name}.csv'


# エクセルファイルの読み込み
df = pd.read_excel(excel_file_path)


# csvの出力
df.to_csv(csv_file_path, index=False)
