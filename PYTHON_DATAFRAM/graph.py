import matplotlib.pyplot as plt
from scipy.fftpack import fft
import pandas as pd
import numpy as np
from scipy.signal import find_peaks


df=pd.read_csv("Vibration.csv")

sarr=df['Vibration_Az'].to_numpy()
y= fft(sarr)

x=np.arange(524286)
plt.plot(x,y)


