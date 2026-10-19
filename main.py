import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote_plus

# Voice setup
speaker = pyttsx3.init()
speaker.setProperty("rate", 165)


def speak(message):
    print("\nAssistant:", message)
    speaker.say(message)
    speaker.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now!")
            recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )
            audio = recognizer.listen(
                source, timeout=8, phrase_time_limit=12
            )

        question = recognizer.recognize_google(audio)
        print("You:", question)
        return question.lower().strip()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Please repeat.")
    except sr.WaitTimeoutError:
        print("No voice detected. Try again.")
    except sr.RequestError:
        speak("Please check your internet connection.")
    except OSError:
        speak("Please check your microphone.")

    return ""


def answer_question(question):
    now = datetime.datetime.now()

    if "hello" in question or question == "hi":
        speak("Hello! How can I help you?")

    elif "time" in question:
        speak("The time is " + now.strftime("%I:%M %p"))

    elif "date" in question or "today" in question:
        speak("Today's date is " + now.strftime("%d %B %Y"))

    elif "who are you" in question:
        speak("I am your personal voice assistant.")

    elif "how are you" in question:
        speak("I am fine. Thank you for asking!")

    elif "open youtube" in question:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in question:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif question.startswith("search "):
        topic = question.replace("search ", "", 1).strip()
        if topic:
            speak("Searching Google for " + topic)
            webbrowser.open(
                "https://www.google.com/search?q="
                + quote_plus(topic)
            )
        else:
            speak("Please tell me what to search for.")

    elif question in ["exit", "stop", "quit", "goodbye"]:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("I will search Google for your question.")
        webbrowser.open(
            "https://www.google.com/search?q="
            + quote_plus(question)
        )

    return True


def main():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak(
        "Your voice assistant is ready. "
        "Ask a question or say search followed by a topic. "
        "Say exit to close."
    )

    while True:
        question = listen()

        if question:
            keep_running = answer_question(question)
            if not keep_running:
                break


if __name__ == "__main__":
    main()