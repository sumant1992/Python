import matplotlib.pyplot as plt
from scipy.fftpack import fft
import pandas as pd
import numpy as np
from scipy.signal import find_peaks


sample= 100
timestep=0.05




df=pd.read_csv("Vibration.csv")

sarr=df['Vibration_Az'].to_numpy()
y= fft(sarr)

amplitude=np.abs(y)
power=amplitude**2


angle=np.angle(y)

amp_frq=np.array([amplitude,100])
amp_po=np.array(amp_frq[0:])
print(max(amp_po))






