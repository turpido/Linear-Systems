import sounddevice as sd
import numpy as np

class AudioHandler:
    def __init__(self, sample_rate=44100, channels=1):
        """
        Initializes the AudioHandler with specific settings.
        """
        self.sample_rate = sample_rate
        self.channels = channels
        self.last_recording = None  # To store the most recent recording

    def record(self, duration_seconds):
        """
        Records audio for x seconds.
        Returns the numpy array and also stores it in self.last_recording.
        """
        print(f"Recording for {duration_seconds} seconds...")
        
        # Record
        recording = sd.rec(
            int(duration_seconds * self.sample_rate), 
            samplerate=self.sample_rate, 
            channels=self.channels,
            dtype='float32'
        )
        sd.wait()  # Wait for recording to finish
        
        print("Recording finished.")
        self.last_recording = recording
        return recording

    def play(self, audio_array=None):
        """
        Plays the provided array. 
        If no array is provided, plays the last recording made by this object.
        """
        # If no input provided, try to use the saved last recording
        if audio_array is None:
            if self.last_recording is not None:
                audio_array = self.last_recording
            else:
                print("No audio data provided and no previous recording found.")
                return

        print("Playing audio...")
        sd.play(audio_array, samplerate=self.sample_rate)
        sd.wait()
        print("Playback finished.")

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Instantiate the class (Create the object)
    my_audio = AudioHandler(sample_rate=44100, channels=1)
    
    try:
        # 2. Call the record method on the object
        duration = float(input("Enter duration in seconds: "))
        
        # This returns the array AND saves it inside the object
        sound_data = my_audio.record(duration)
        
        # 3. Play it back
        # Option A: Pass the data explicitly
        # my_audio.play(sound_data)
        
        # Option B: Call play() without arguments to play the last thing recorded
        my_audio.play()

    except KeyboardInterrupt:
        print("\nStopped.")