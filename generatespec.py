
# coding: utf-8

# ## Generate spectrograms for all downloaded tracks
# 
# Find all tracks, then use ffmpeg to convert them to wav. Then, using matplotlib functions, create grayscale spectrograms and save them as .png files.

# In[3]:


import glob
from multiprocessing import Pool
from tqdm import tnrange, tqdm
import os
from tempfile import mktemp
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import subprocess
import ffmpeg
from utils import make_logger
import logging

logger = make_logger('log/generatespec.log')

dpi = 92
resolution = 128

def make_spectrogram(filename):
    wname = mktemp('.wav')
    ffmpeg.input(filename).output(wname, ac=1).global_args('-loglevel', 'error').run()
    sample_rate, samples = wavfile.read(wname)
    os.unlink(wname)

    fig, ax = plt.subplots(frameon=False)
    fig.set_size_inches(resolution / dpi, resolution / dpi)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.specgram(samples, Fs=sample_rate, cmap='Greys_r')
    fname = os.path.abspath(filename.replace('.mp3', '.png').replace('.m4a', '.png'))
    fig.savefig(fname, dpi=92)
    plt.close()


files = glob.glob('tracks/**/*.mp3', recursive=True) + glob.glob('tracks/**/*.m4a', recursive=True)

logger.info("Generating spectrogram data for all audio samples...")
p = Pool(25)
r = p.imap(make_spectrogram, files)
# Workaround to make the progress bar work, for some reason it doesnt work properly with subprocess
for i in tqdm(r, total=len(files)):
    pass
logger.info("Generated spectrogram data for audio samples successfully")

