# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import numpy as np
from pydub import AudioSegment
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Read the MP3 file
audio = AudioSegment.from_file('./data/experiments/cncsounds.mp3')

# Convert to mono and get the raw audio data
mono_audio = audio.set_channels(1)
sample_rate = audio.frame_rate
audio_data = np.array(mono_audio.get_array_of_samples())

# Segment length (e.g., 1 second)
segment_length = sample_rate

# Process each segment
for i in range(0, len(audio_data), segment_length):
    segment = audio_data[i:i + segment_length]

    # Apply FFT
    yf = fft(segment)
    xf = fftfreq(segment_length, 1 / sample_rate)

    # Plot the power spectrum
    plt.figure()
    plt.plot(xf, np.abs(yf))
    plt.title(f"Frequency Spectrum of Segment {i // segment_length}")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power")
    plt.xlim(0, sample_rate // 2)  # Show only positive frequencies
    plt.show()

# Note: Denoising steps would go here

# -


