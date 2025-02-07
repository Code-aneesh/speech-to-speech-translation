# 🎤 Real-Time Speech-to-Speech Translator (Offline & Free)

This project allows users to **speak in one language and hear the translated speech in another language** in real-time. It uses:

- **Speech Recognition (Google Speech-to-Text API - Free)**
- **Translation (Google Translator API & Backup Translator - Free)**
- **Text-to-Speech (pyttsx3 - Offline & Free)**

---

## 📂 Features

- 🎤 **Speech Recognition:** Listens to spoken words and converts them to text
- 🌐 **Translation:** Uses Google Translator API for free text translation
- 🌎 **Backup Translation:** Uses `mtranslate` as a backup in case of Google API failure
- 🔊 **Text-to-Speech:** Converts the translated text back into speech (Offline using `pyttsx3`)

---

## 📚 Requirements

Ensure you have **Python 3.x** installed. Then install the following dependencies:

```bash
pip install speechrecognition pyttsx3 deep-translator mtranslate pyaudio
```

- `speechrecognition` - Recognizes speech using Google's free API
- `pyttsx3` - Converts text to speech (Offline)
- `deep-translator` - Uses Google Translator API for free text translation
- `mtranslate` - Provides backup translation in case of Google failure
- `pyaudio` - Enables microphone input

> **Note:** If you get errors related to `pyaudio`, install it with:
>
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🔍 How It Works

1. **Listens** to user speech via microphone 🎤
2. Converts **speech to text** (Google Speech Recognition) 📘
3. **Translates** the text using Google Translator API (or backup) 🌐
4. Converts **translated text to speech** (Offline) 🎧

---

## 💻 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Code-aneesh/speech-to-speech-translation.git
   cd speech-to-speech-translation
   ```

2. **Run the script:**

   ```bash
   python main.py
   ```

3. **Speak into the microphone**

4. The system **translates your speech** and speaks the translation aloud! 🎧

---

## 🎉 Supported Languages

- By default, **English to Spanish** (change `'es'` to another language code in `translate(text, "es")`)
- Some language codes:
  - French: `fr`
  - German: `de`
  - Hindi: `hi`
  - Japanese: `ja`
  - Chinese: `zh-cn`

---

## 📝 Customization

### 🎤 Change Target Language

Modify this line in `main.py`:

```python
translated_text = translate(text, "es")  # Change 'es' to any language code
```

### 🎶 Adjust Speech Speed

Change the speech rate in `main.py`:

```python
engine.setProperty("rate", 150)  # Adjust speed (default: 150)
```

---

## ✨ Future Improvements

- Support for **more translation APIs**
- Better **speech synthesis quality**
- Offline translation capabilities

---

## 🏆 Contribution

Feel free to **fork** the repo and contribute! PRs are welcome.

---

💡 **Have any issues?** Open an issue on GitHub!

🚀 Happy Coding! 🚀

