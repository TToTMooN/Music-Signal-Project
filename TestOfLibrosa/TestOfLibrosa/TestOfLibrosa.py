from __future__ import print_function
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


filename = "luv.wav"
y, sr = librosa.load(filename, duration = 1)

## stft
D = librosa.stft(y, n_fft=2048*4, hop_length=2048/4)
S = np.abs(D)
### filter the signal
alpha = 0.1 # the threhold for the filtering
S_filtered = S
time_length = np.shape(S_filtered)[1]
freq_length = np.shape(S_filtered)[0]
max_freq = np.max(S_filtered)
for i in range(1, time_length):
    for j in range(1,freq_length):
        if S_filtered[j,i] < alpha*max_freq :
            S_filtered[j,i]=0
### gather information at certain time
for i in range(1, time_length):
    target = S_filtered[:,i]
    target_freqs = get_char_freq(target, freq_length)
### plot the 
A = librosa.amplitude_to_db(S_filtered, ref=np.max)
librosa.display.specshow(A, y_axis='log', x_axis='time')
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
plt.axis([0, 10, 128, 1024])
plt.title('Input spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.show()