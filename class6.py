import io
import numpy as np
import AudioHandler as ah
from Math import Math
from RW import FileHandler

# Instantiate helpers
audio_handler = ah.AudioHandler()
math_helper = Math()
file_handler = FileHandler(base_dir="output")

# Record a short clip
x = audio_handler.record(5)

# Echo parameters
D = 15000  # delay in samples
a = 0.6    # echo attenuation (0 < a < 1)

# Build an impulse response for the echo and convolve using Math.py
# impulse = [1, 0, 0, ..., 0, a]
impulse = [1.0] + [0.0] * (D - 1) + [a]
dry_signal = x[:, 0].tolist()
convolved = math_helper.convolve(dry_signal, impulse)
print(f"got here!")
# Back to numpy for playback/saving
y = np.array(convolved, dtype="float32").reshape(-1, 1)

# Play the mix
audio_handler.play(y)

# Save the processed audio using RW.py
buffer = io.BytesIO()
np.save(buffer, y)
saved_path = file_handler.save_file("echo.npy", buffer.getvalue())
print(f"Saved processed audio to {saved_path}")
