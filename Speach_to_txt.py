import speech_recognition as sr
def listen():
    r = sr.Recognizer()
    r.energy_threshold = 3500

    with sr.Microphone() as source:
                #print("\n\n\nSay something!")
                r.adjust_for_ambient_noise
                audio = r.listen(source)
                return ( r.recognize_google(audio))