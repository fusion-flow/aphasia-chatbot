import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
        print("listening started...")
        audio = r.listen(source)
        print("listening ended...")   
        transcription = r.recognize_google(audio)       
        print("Transcription: " + transcription)
        if (transcription=="stop"):
            print("Transcription Stopped")
            break