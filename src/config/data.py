import os


sampling_rate = 10000
start_index = 4613
end_index = 45113
discard_index = 20
sampling_width = 20
origin = 'sorajit/EG0'
task = 'NARMA2'
data_directory_path = f'./data/{origin}'
file_origin = 'inp8_random_pulse_1Hz_10000'
# file_origin = 'EG10_rp_0.1Hz_1000sampling_t'
file_name = f'{file_origin}.csv'
data_file_path = os.path.join(data_directory_path, file_name)
img_directory_path = f'./result/{origin}/{task}/{file_origin}'
input_columns = ['V4']
output_columns = ['V1', 'V2', 'V3', 'V5', 'V6', 'V7']
is_scaling = 'min_max'  # 'min_max' or 'none'