import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

audio_path = "01_frontinstrument/bass.wav"
y, sr = librosa.load(audio_path, sr=4096)

S = np.abs(librosa.stft(y))
S_left = librosa.stft(y, center=False)

D_short = librosa.stft(y, hop_length=64)

fig, ax = plt.subplots()
img = librosa.display.specshow(
    librosa.amplitude_to_db(S, ref=np.max), y_axis="log", x_axis="time", ax=ax
)
ax.set_title("Power spectrogram")
fig.colorbar(img, ax=ax, format="%+2.0f db")
plt.show()