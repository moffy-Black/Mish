# !/usr/bin/env python
# coding: utf8

from swan import pycwt
import numpy as np
import matplotlib.pyplot as plt
import wave
from scipy import signal

if __name__ == "__main__":
  wavfile = '01_frontinstrument/bass.wav'
  wr = wave.open(wavfile, "rb")
  ch = wr.getnchannels()
  width = wr.getsampwidth()
  fr = wr.getframerate()
  fn = wr.getnframes()
  fs = fn / fr

  print('ch', ch)
  print('frame', fn)
  print('fr',fr)
  print('sampling fs ', fs, 'sec')
  print('width', width)
  origin = wr.readframes(wr.getnframes())
  data = origin[:fn]
  wr.close()
  amp = max(data)
  print(amp)
  halfn = fn / 2

  if type(fs) == float:
    fs = int(fs) + 1

  if type(halfn) == float:
    halfn = int(halfn)

  print('len of origin', len(origin))
  print('len of sampling: ', len(data))

  # ステレオ前提 > monoral
  y = np.frombuffer(data, dtype="int16")  /32768.0
  x = np.linspace(0,fs, halfn, endpoint=False)
  plt.plot(x, y)
  plt.show()
