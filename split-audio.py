from pydub import AudioSegment
import math

# Carica il file audio
audio_file = "/path/to/your/audio_file.mp3"  # Sostituisci con il percorso del tuo file
audio = AudioSegment.from_file(audio_file)

# Durata di ogni segmento in millisecondi (30 minuti = 30 * 60 * 1000)
segment_duration_ms = 30 * 60 * 1000

# Calcola il numero di segmenti necessari
num_segments = math.ceil(len(audio) / segment_duration_ms)

# Dividi e salva i segmenti
for i in range(num_segments):
    start_time = i * segment_duration_ms
    end_time = start_time + segment_duration_ms
    segment = audio[start_time:end_time]
    segment.export(f"/path/to/save/directory/segment_{i+1}.mp3", format="mp3")
    print(f"Segmento {i+1} salvato.")