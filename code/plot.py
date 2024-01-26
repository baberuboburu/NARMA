import matplotlib.pyplot as plt


class Plot():
  def __init__(self):
    pass


  def plot(self, x, y, title, xlabel='Time/s', ylabel='Voltage/V', mode=True):
    fig, ax = plt.subplots(figsize=(12.8, 4.8), dpi=100, tight_layout=True)
    ax.scatter(x, y, s=12, c='red')
    ax.plot(x, y, c='blue')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    plt.show(block=mode)