import numpy as np
import matplotlib.pyplot as plt
from scipy import hamming
import librosa
import librosa.display


def FFT(x):
    N = x.shape[0]

    # 再起動作の一番最後
    if N == 1:
        return x[0]

    x_even = x[0:N:2]
    x_odd = x[1:N:2]

    # ここで再帰動作をする
    X_even = FFT(x_even)
    X_odd = FFT(x_odd)

    # DFTと同じようにWを求める
    W = []
    for t in range(N // 2):
        W.append(np.exp(-1j * ((2 * np.pi * t) / N)))
    W = np.array(W)

    # ここで型をcomplexに指定しないとエラーを吐くので注意
    X = np.zeros(N, dtype="complex")
    X[0 : N // 2] = X_even + W * X_odd
    X[N // 2 : N] = X_even - W * X_odd

    return X


def STFT(x, win_length, hop=0.5):
    """
    今回はwin=Mとして実装。
    データサイズも簡単のため2のべき乗に制限。
    hopはデフォルトで窓幅の半分とする。
    """
    hop_length = int(win_length * hop)

    # 窓関数をかける時に端点が問題になります。
    # 今回はlibrosaのデフォルトに習って反転パディングをしてみます。
    pad_first = x[:hop_length]
    pad_last = x[-hop_length:][::-1]
    x_pad = np.concatenate([pad_first, x, pad_last])

    # データのサンプル数
    N = x_pad.shape[0]

    # FFTの結果を半分にした長さ
    M = int(win_length // 2) + 1

    # 窓関数を適用する回数
    T = int((N - hop_length) / hop_length)

    # 今回はハミング窓（ハン窓）を利用します
    han = hamming(win_length)

    # 結果を格納する箱です
    spec = np.zeros((M, T), dtype="complex")

    for t in range(T):
        # まず窓関数を適用します
        windowed_x = x_pad[t * hop_length : t * hop_length + win_length] * han

        # 次にFFTを実行します。
        spec[:, t] = FFT(windowed_x)[: int(win_length // 2) + 1]
    return spec


if __name__ == "__main__":
    WAV_FILE = "01_frontinstrument/bass.wav"
    y, sr = librosa.load(WAV_FILE)
    spec = STFT(y, 1024, 0.5)
    spec_db = librosa.amplitude_to_db(np.abs(spec))
    librosa.display.specshow(spec_db, y_axis="log")
    plt.show()