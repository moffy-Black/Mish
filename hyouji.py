# !/usr/bin/env python
# coding: utf8

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

if __name__ == "__main__":
    fig = plt.figure(1, figsize=(12, 4))
    ax = fig.add_subplot(1, 1, 1)
    img = Image.open("music0.00.png")
    ax.imshow(img, alpha=1.0)
    plt.show()