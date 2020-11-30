import os
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import librosa
import librosa.display


if __name__ == "__main__":
  WAV_FILE = '01_Track/bass.wav'
  y, sr = librosa.load(WAV_FILE)
  S = np.abs(librosa.stft(y))

  plt.figure(figsize=(10, 4))
  librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time')
  plt.title('Power spectrogram')
  plt.colorbar(format='%+2.0f dB')
  plt.tight_layout()
  plt.show() 