import numpy as np
from scipy.io import wavfile

def generate_calibration_key(filename="calibration_key.wav", duration=60, fs=44100):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    carrier = 144.0  # The 144Hz Foundation
    # PSK Modulation: Phase shifts represent the calibration data
    phase_data = np.pi * np.sign(np.sin(2 * np.pi * 0.5 * t)) 
    signal = np.sin(2 * np.pi * carrier * t + phase_data)
    
    # Normalize and convert to 16-bit PCM
    audio = (signal * 32767).astype(np.int16)
    wavfile.write(filename, fs, audio)
    print(f"File {filename} generated successfully.")

if __name__ == "__main__":
    generate_calibration_key()
  
