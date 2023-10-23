'''
Link for working colab file : 
https://colab.research.google.com/drive/1hO0qcKkQAnHemEXhtkpsCV9Bn_99FTlv?usp=sharing
'''

import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

# Initialize the recognizer
recognizer = sr.Recognizer()

# Replace with the path to your MP3 file
mp3_file = "transcript.mp3"

# Convert the MP3 file to WAV format
wav_file = "converted_audio.wav"
audio = AudioSegment.from_mp3(mp3_file)
audio.export(wav_file, format="wav")

# Perform speech recognition on the WAV file
with sr.AudioFile(wav_file) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except Exception as e:
    print(f"An error occurred: {e}")