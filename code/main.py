from arrange import Arrange
from narma import NARMA
from plot import Plot
from generate_wave import GenerateWave
import param
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


# 変数の取得
ORDER = param.ORDER
sampling_rate = param.sampling_rate


# 定数の定義
d_init = [0] * ORDER


# データの取得
arrange = Arrange(sampling_rate=sampling_rate)
input = arrange.arrange_input()


# Narmaの定義
narma = NARMA(m=ORDER, a1=0.4, a2=0.4, a3=0.6, a4=0.1)


# 目標波形の生成 (Narmaモデルの作成)
steps = np.arange(1, len(input)+1)
target = narma.narma(time=len(steps), input=input, d_init=d_init)


# 学習用データ
generate = GenerateWave(sampling_rate=sampling_rate)
data = generate.generate()


# 回帰
model = LinearRegression()
model.fit(data, target)
pred = model.predict(data)

'''
# 性能の評価
# MAEの計算
mae = mean_absolute_error(target, pred)
print("Mean Absolute Error (MAE):", mae)

# MSEの計算
mse = mean_squared_error(target, pred)
print("Mean Squared Error (MSE):", mse)

# ピアソン相関係数の計算
correlation = np.corrcoef(target.ravel(), pred.ravel())[0, 1]
print("Pearson Correlation Coefficient:", correlation)
'''

# グラフの表示
plot = Plot()
plot.plot(x=steps[10:], y=target[10:], title='target_wave', xlabel='Time/s', ylabel='Voltage/V', mode=False)
plot.plot(x=steps[10:], y=pred[10:], title='narma_wave', xlabel='Time/s', ylabel='Voltage/V', mode=True)