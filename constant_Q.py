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
    # 1 tempo推定
    audio_path = "output/紅蓮華/drums.wav"
    y, sr = librosa.load(audio_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    sixteen_frame_time = 60 / tempo * 16
    # 2 画像生成
    audio_path = "output/紅蓮華/bass.wav"
    for i in range(10):
        y, sr = librosa.load(
            audio_path, offset=i * sixteen_frame_time, duration=sixteen_frame_time
        )
        C = librosa.cqt(y, sr)

        # f_min = 32.70
        # fmax = f_min * ((2 ** (1 / 12)) ** 84)

        fig = plt.figure(1, figsize=(12, 4))
        # ax = fig.add_subplot(1, 1, 1)
        log_cqt_power = librosa.amplitude_to_db(
            np.abs(C), ref=np.max
        )  # 振幅をdB(デシベル)音の強さに変換

        # 置き換え -5dB以上のものだけ表示
        # replacement_log_cqt_power = replacement(log_cqt_power)
        librosa.display.specshow(
            log_cqt_power, x_axis="time", y_axis="cqt_note"  # cqt_hz,cqt_note
        )  # cqtの表示

        # chroma = librosa.feature.chroma_cqt(C=C, sr=sr)
        # librosa.display.specshow(chroma, x_axis="time", y_axis="chroma")
        # plt.colorbar()
        plt.savefig("music{:.2f}.png".format(i))
        # print(len(log_cqt_power))
        # print("Estimated tempo: {:.2f} beats per minute".format(tempo))
