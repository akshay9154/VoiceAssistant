import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm currently offline.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    command = listen()

    if "search website" in command:
        speak("Sure, which website would you like me to search?")
        website = listen()

        if website:
            speak(f"What would you like to search on {website}?")
            query = listen()

            if query:
                search_url = f"https://www.{website}.com/search?q={query}"
                webbrowser.open(search_url)
                speak(f"Here are the search results for {query} on {website}.")
            else:
                speak("Sorry, I didn't catch the search query.")
        else:
            speak("Sorry, I didn't catch the website name.")
    elif "hello" in command:
        speak("Hello there!")
    elif "what is your name" in command:
        speak("I'm an AI assistant.")
    elif "goodbye" in command:
        speak("Goodbye!")
        break
