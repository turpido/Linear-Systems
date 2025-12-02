import lib.AudioHandler as ah
import numpy as np
audio = ah.AudioHandler()
x = audio.record(5)

# x : input signal (list or n
# umpy array)
# D : delay in samplesWWWW
# a : echo attenuation (0 < a < 1)
D = 15000
a = 0.6
y = []

# Create empty array (size = original + delay)
y = np.zeros((len(x) + D, 1), dtype='float32')

# Copy original sound to the start
y[:len(x)] += x

# Add quieter echo starting at delay D
y[D:] += x * a

# Play the mix
audio.play(y)