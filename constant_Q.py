# !/usr/bin/env python
# coding: utf8

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def replacement(n):
    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j] <= -5:
                n[i][j] = -80
    return n


if __name__ == "__main__":
    audio_path = "output/紅蓮華/vocals.wav"
    y, sr = librosa.load(audio_path)

    C = librosa.cqt(y, sr)

    # f_min = 32.70
    # fmax = f_min * ((2 ** (1 / 12)) ** 84)

    fig = plt.figure(1, figsize=(12, 4))
    ax = fig.add_subplot(1, 1, 1)
    log_cqt_power = librosa.amplitude_to_db(np.abs(C), ref=np.max)  # 振幅をdB(デシベル)音の強さに変換

    # 置き換え -5dB以上のものだけ表示
    # replacement_log_cqt_power = replacement(log_cqt_power)
    # librosa.display.specshow(
    #     log_cqt_power, x_axis="time", y_axis="cqt_note"  # cqt_hz,cqt_note
    # )  # cqtの表示

    chroma = librosa.feature.chroma_cqt(C=C, sr=sr)
    librosa.display.specshow(chroma, x_axis="time", y_axis="chroma")
    plt.colorbar()
    plt.show()
    # print(len(log_cqt_power))
