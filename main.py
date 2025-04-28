from src.config.config import *
from src.components.narma2 import NARMA2
from src.components.narma10 import NARMA10
from src.utils.arrange_data import ArrangeData
from src.utils.data_processor import DataProcessor
from src.utils.plot import Plot


# Instanciation
narma = NARMA2()
# narma = NARMA10()
arrange_data = ArrangeData()
data_processor = DataProcessor()
plot = Plot()

# Arrange Data
arrange_data.run()
input_df, output_df = data_processor.run()
input_df = input_df / 4

# Plot data
plot.input_wave(input_df)
plot.output_wave(output_df)

# Create the target wave
target_df = narma.prepare_target(input_df)
input_df = input_df.iloc[discard_index:]
output_df = output_df.iloc[discard_index:]

# Ridge Regression
pred_df, nrmse = narma.fit_predict(output_df, target_df)
plot.run(target_df, pred_df)
print(f'NRMSE: {nrmse:.6f}')