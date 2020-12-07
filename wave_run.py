import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pandas as pd
import IPython.display
from IPython.display import display

audio_path = "01_frontinstrument/bass.wav"

y, sr = librosa.load(audio_path, sr=4096)

# 波形の表示
mpl_collection = librosa.display.waveplot(y, sr=sr)
mpl_collection.axes.set(title="音声波形", ylabel="波形の振幅")
# plt.show()

D = librosa.stft(y)
S, phase = librosa.magphase(D)
Sdb = librosa.amplitude_to_db(S)
librosa.display.specshow(Sdb, sr=sr, x_axis='time', y_axis='log')
plt.show()
