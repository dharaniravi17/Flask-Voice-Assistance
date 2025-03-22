# Flask Voice Assistant

This is a voice assistant project built with Flask that utilizes Google's Gemini API for NLP, SpeechRecognition for input, and pyttsx3 for text-to-speech conversion.

## Features
- **Speech-to-Text**: Uses `SpeechRecognition` for capturing and converting speech input.
- **Natural Language Processing**: Sends text to Google's Gemini API for intelligent responses.
- **Text-to-Speech**: Uses `pyttsx3` to convert the response into speech.
- **Flask API**: Runs a simple web server for handling voice commands and responses.
- **CORS Enabled**: Allows frontend applications to interact with the assistant.

## Installation
### Prerequisites
- Python 3.8 or later
- A valid Google Gemini API Key

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Dharaniravi17/flask_voice_assistant.git
   cd flask_voice_assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API key securely:
   - Create a `.env` file in the root directory.
   - Add the following line inside `.env`:
     ```plaintext
     GEMINI_API_KEY=your_actual_api_key_here
     ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

## API Endpoint
### POST `/process`
**Request Body:**
```json
{
  "text": "Hello, how are you?"
}
```
**Response:**
```json
{
  "user_text": "Hello, how are you?",
  "bot_response": "I'm doing great! How can I assist you?"
}
```

## License
This project is licensed under the MIT License.

## Author
[Dharaniravi17](https://github.com/Dharaniravi17)
