import google.generativeai as ai
import speech_recognition as sr
import pyttsx3
import os


#API and Model setup
API_KEY = 'Your_api_key'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()


# Default prompt
default_prompt = "You are Guido, a friendly Python tutor. Provide concise Python programming answers. Don't use emojis. Be interactive."

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()



# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Guido : Listening... Speak clearly.")
        speak("Listening speak clearly")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=30)
            text = recognizer.recognize_google(audio).lower()
            print(f"Guido: You said: {text}")
            return text
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            print("Guido: I couldn't hear or understand you. Please Try again.")
            speak("I couldn't hear or understand you. Please Try again")
            return None

# Function to speak a response
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to inform the user that the system is processing information
def processing_info():
    print("Guido: I'm processing your request, please wait...")
    speak("I'm processing your request, please wait")

# Chatbot loop
print("Guido PyMentor. Say 'exit' to stop.")
print("Guido: Hi, I'm Guido! Shall we dive into Python together? You can ask questions, share thoughts, or simply say exit to stop anytime.")
speak("Hi, I'm Guido! Shall we dive into Python together? You can ask questions, share thoughts, or simply say exit to stop anytime.")



while True:
    user_input = listen()

    if user_input:
        if "exit" in user_input:
            print("Guido: Exiting PyMentor...")
            speak("Exiting PyMentor")
            speak("Goodbye! Keep coding!")
            break

        # Check if the user wants a detailed explanation
        if "explain in detail" in user_input or "give me more details" in user_input:
            modified_prompt = "Provide a detailed explanation of Python concepts."
        else:
            modified_prompt = default_prompt

        # Inform the user that Guido is processing the request
        processing_info()

        # Send modified prompt + user input to API
        response = chat.send_message(f"{modified_prompt}\nUser: {user_input}")

        # Chatbot response
        bot_response = response.text
        print(f"Guido: {bot_response}")
        speak(bot_response)
