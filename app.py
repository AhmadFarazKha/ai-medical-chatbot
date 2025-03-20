import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Google Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing. Please set it in .env file.")

genai.configure(api_key=GOOGLE_API_KEY)

# Ensure the correct model name
MODEL_NAME = "gemini-1.5-pro-latest"  # Verify this with list_models()

# Homepage Route
@app.route("/")
def index():
    return render_template("index.html")

# Chatbot Route
@app.route("/get_medicine", methods=["POST"])
def get_medicine():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"bot_response": "Error: No input provided."})

        # Use Gemini API
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(user_input)

        if response and response.text:
            bot_reply = response.text
        else:
            bot_reply = "Sorry, I couldn't generate a response."

    except Exception as e:
        bot_reply = f"An error occurred: {str(e)}"

    return jsonify({"bot_response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
