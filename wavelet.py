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

  Fs = 1/0.01
  omega0 = 2 #0.2 #1 #2 #8
  # (1)　Freqを指定してcwt
  freqs=np.arange(0.1,20,0.025)
  r=pycwt.cwt_f(y,freqs,Fs,pycwt.Morlet(omega0))
  rr = np.abs(r)
  
  plt.rcParams['figure.figsize'] = (10, 6)
  fig = plt.figure()
  ax1 = fig.add_axes([0.1, 0.75, 0.7, 0.2])
  ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.60], sharex=ax1)
  ax3 = fig.add_axes([0.83, 0.1, 0.03, 0.6])

  ax1.plot(x, y, 'k')

  img = ax2.imshow(np.flipud(rr), extent=[0, 3,0.1, 20], aspect='auto') 
  twin_ax = ax2
  twin_ax.set_yscale('log')
  twin_ax.set_xlim(0, 3)
  twin_ax.set_ylim(0.1, 20)
  ax2.tick_params(which='both', labelleft=False, left=False)
  twin_ax.tick_params(which='both', labelleft=True, left=True, labelright=False)
  fig.colorbar(img, cax=ax3)
  plt.show()
  # t = np.linspace(-1, 1, 200, endpoint = False) #(初期値,最終値,要素数,endpoint=は最終値を含めるかどうか)
  # sig = np.cos(2 * np.pi * 7 * t) + signal.gausspulse(t - 0.4, fc=2)
  
  # plt.plot(t, sig)
  # plt.pause(3)
    
  # widths = np.arange(1, 31)
  # cwtmatr = signal.cwt(sig, signal.ricker, widths)
  # plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
  #           vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
  # plt.show()