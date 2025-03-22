import os
import pyttsx3
import google.generativeai as genai
import speech_recognition as sr
from flask import Flask, request, jsonify
from flask_cors import CORS
from langdetect import detect

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Set your Gemini API Key directly
GEMINI_API_KEY = "AIzaSyDmv_Io0LMNqkvFijTcLcOs2pc5UL12ydM"

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Function to get response from Gemini API
def get_gemini_response(text):
    try:
        model_name = "gemini-1.5-pro-latest"
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(text)
        return response.text.strip() if response and response.text else "I couldn't understand that."
    except Exception as e:
        return f"Error: {str(e)}"

# Route to process speech input
@app.route("/process", methods=["POST"])
def process_speech():
    data = request.json
    user_text = data.get("text")

    if not user_text:
        return jsonify({"error": "No text received"}), 400

    bot_response = get_gemini_response(user_text)

    # Print to terminal
    print("\n🗣️ User:", user_text)
    print("🤖 Gemini:", bot_response)

    engine.say(bot_response)


    return jsonify({"user_text": user_text, "bot_response": bot_response}), 200

    

if __name__ == "__main__":
    print("[🎤] Voice Assistant is Ready! Waiting for user input...")
    app.run(debug=True)
