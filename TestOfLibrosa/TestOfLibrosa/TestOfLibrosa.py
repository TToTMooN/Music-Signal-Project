from __future__ import print_function
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = "Time.mp3"
y, sr = librosa.load(filename, duration=20.0)

### Beats
#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#print('Saving output to beat_times.csv')
#librosa.output.times_csv('beat_times.csv', beat_times)

## stft
D = librosa.stft(y)
S = np.abs(D)
comps, acts = librosa.decompose.decompose(S, n_components=16)

plt.figure(figsize=(10,8))
plt.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(S,
                                                 ref=np.max),
                         y_axis='log', x_axis='time')
plt.title('Input spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.subplot(3, 2, 3)
librosa.display.specshow(librosa.amplitude_to_db(comps,
                                                 ref=np.max),
                         y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Components')
plt.subplot(3, 2, 4)
librosa.display.specshow(acts, x_axis='time')
plt.ylabel('Components')
plt.title('Activations')
plt.colorbar()
plt.subplot(3, 1, 3)
S_approx = comps.dot(acts)
librosa.display.specshow(librosa.amplitude_to_db(S_approx,
                                                 ref=np.max),
                         y_axis='log', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Reconstructed spectrogram')
plt.tight_layout()
plt.show()
### Pitch shift
#y_third = librosa.effects.pitch_shift(y, sr, n_steps=10)
#librosa.output.write_wav('Time_thirdup.wav', y_third, sr)