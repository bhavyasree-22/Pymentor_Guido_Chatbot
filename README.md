# 🐍 Pymentor Guido: Your Voice-Powered Python Sensei

**Guido** is an advanced, voice-interactive Python tutor powered by the **Google Gemini AI** engine. Instead of just reading tutorials, you can now *talk* to your tutor. Guido listens to your questions, processes them using state-of-the-art AI, and speaks the answers back to you in real-time.

---

## 🚀 Key Highlights

* 🎙️ **Hands-Free Learning:** Uses `SpeechRecognition` to understand your spoken commands.
* 🔊 **Natural Interaction:** Responds verbally via `pyttsx3`, making learning feel like a real conversation.
* 🧠 **Gemini-Powered Brain:** Leverages the `gemini-pro` model for highly accurate and concise coding advice.
* 🔍 **Deep Dives:** Supports interactive follow-ups like "explain in detail" for complex topics.
* ⚡ **Simple Exit:** Just say "exit" to wrap up your learning session instantly.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3 |
| **AI Model** | Google Gemini Pro |
| **Ear (STT)** | SpeechRecognition Library |
| **Voice (TTS)** | pyttsx3 Engine |
| **Audio Driver**| PyAudio |

---

## ⚙️ Installation

### ✅ Prerequisites
Make sure you have the following installed:
* **Python 3.8 or higher**

### 📦 Required Python Libraries
Install these using pip:
* `google-generativeai`
* `SpeechRecognition`
* `pyttsx3`
* `pyaudio`

---

### 📦 Setup Instructions
### 1. Clone the Repository
* Run the following commands in your terminal:
```bash
git clone <your-repo>   # Replace <your-repo> with GitHub repository link
cd <your-repo-folder>   # Replace <your-repo-folder> with your project folder name
 ```
### 2. Create a Virtual Environment
* It's recommended to use a virtual environment to manage dependencies.
* Run the following line in your terminal which will create a virtual environment named myenv:
```bash
python3 -m venv myenv
 ```
### 3. Activate the Virtual Environment
* On macOS/Linux:
```bash
source myenv/bin/activate
 ```
* On Windows:
``` bash
myenv\Scripts\activate
 ```
### 4. Install Dependencies
* If you'd prefer to install all required packages at once, you can use the provided requirements.txt file:
```bash
pip3 install -r requirements.txt
 ```
(Alternative Method for step 4):
* Once the virtual environment is activated, install the required packages:
* For `google-generativeai`:
```bash
pip3 install google-generativeai
 ```
* For `SpeechRecognition`:
```bash
pip3 install SpeechRecognition
 ```
* For `pyttsx3`:
```bash
pip3 install pyttsx3
 ```
* For `pyaudio`:
```bash
pip3 install pyaudio
 ```
 * You can all install at a time
```bash
pip3 install google-generativeai SpeechRecognition pyttsx3 pyaudio
 ```

 ### 5. Google Generative AI API Key and Model
* For API Key: Visit Google AI Studio to get your API key.
* Replace the placeholder in the code with your key:
```bash
API_KEY = 'Your_API_Key'
 ```
* For Model: If you want to use a different model than the default (`gemini-pro`), you can:
* Visit the [Google AI Studio](https://aistudio.google.com/) to browse and select the model that best suits your needs.
* Copy the model name and in your code, update the line:
```bash
model = ai.GenerativeModel("your-model-name")  # Replace the model name you have copied
```

---

### ⚠️ Note:
* Google provides a free tier for Generative AI with limited monthly usage.
* If you exceed the free quota or use premium models, charges may apply.
* Use Responsibly, stay within free limits and avoid unexpected charges.
---
## 🚀 Usage
#### 1. Run the script:
```bash
python pymentor.py
```
#### 2. Speak your Python-related question when prompted. 
#### 3. Guido will respond with a spoken answer. 
#### 4. Say "explain in detail" or "give me more details" if you want a longer explanation.
#### 5. Say "exit" anytime to stop the program.
