# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Experiment: FFTs on Input Data

# %%
print("hello world")

# %%
from pydub import AudioSegment

# %%
import numpy as np

# %%
import plotly.graph_objects as go

# %%
cncaudio = AudioSegment.from_mp3("data/experiments/cncsounds.mp3")

# %%
if cncaudio.channels >1 :
    cncaudio = cncaudio.set_channels(1)


# %%
samples = np.array(cncaudio.get_array_of_samples())

# %%
# Compute the FFT

# %%
frequencies = np.fft.rfftfreq(len(samples), 1/cncaudio.frame_rate)

# %%
spectrum = np.abs(np.fft.rfft(samples))

# %%
fig = go.Figure()

# %%
# Add the data to the plot
fig.add_trace(go.Scatter(x=frequencies, y=spectrum, mode='lines'))
# Set the axes type to loglog
fig.update_layout(
    xaxis_type="log",
    yaxis_type="log",
    title='Fourier Spectrum of Audio',
    xaxis_title='Frequency (Hz)',
    yaxis_title='Amplitude'
)
# Display the plot
fig.show()

# %%
