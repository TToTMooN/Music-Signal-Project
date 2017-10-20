from __future__ import print_function
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = librosa.util.example_audio_file()
print(filename)
y, sr = librosa.load(filename)

#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

#beat_times = librosa.frames_to_time(beat_frames, sr=sr)

#print('Saving output to beat_times.csv')
#librosa.output.times_csv('beat_times.csv', beat_times)

D = librosa.stft(y)
D_left = librosa.stft(y, center=False)
D_short = librosa.stft(y, hop_length=64)
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
plt.title('Power spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()