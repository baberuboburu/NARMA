# 変数を一元管理するファイル


# サンプリングレート, ファイル名に'-1'や'-0.1'のように命名する
sampling_rate = 1

# NARMAの次元, NARMA2なら,2に設定する
ORDER = 2

# 得たデータの最初に取る点
start_point = 50

# 印加する電圧のスケール化
up_scale = 0.5
bottom_scale = -0.5

# input.csvのファイルパス
file_path_input = '../data/csv/input.csv'

# データが入っているcsvのディレクトリパス
dir_path_data = '../data/csv'

# 測定したデータのコラム名，'time', 'input', 'output'を並び替える。'trash'は不要な列
data_columns = ['time', 'input' ,'output', 'trash']

# データの行数
num_data = 512

# パルスの幅, 1つのパルスに何点含まれているか
num_point_in_pulse = 100


if sampling_rate == 1:
  start_point = 50
  num_point_in_pulse = 100
elif sampling_rate == 0.1:
  start_point = 5
  num_point_in_pulse = 10