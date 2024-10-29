from moviepy.editor import AudioFileClip
import math

# Carica il file audio
audio_file = "/path/to/your/audio_file.mp3"
audio = AudioFileClip(audio_file)

# Durata di ogni segmento in secondi (30 minuti = 30 * 60)
segment_duration_sec = 30 * 60

# Calcola il numero di segmenti necessari
num_segments = math.ceil(audio.duration / segment_duration_sec)

# Dividi e salva i segmenti
for i in range(num_segments):
    start_time = i * segment_duration_sec
    end_time = min((i + 1) * segment_duration_sec, audio.duration)
    segment = audio.subclip(start_time, end_time)
    segment.write_audiofile(f"/path/to/save/directory/segment_{i+1}.mp3")
    print(f"Segmento {i+1} salvato.")