from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API Key
genai.configure(api_key=os.environ.get("AIzaSyCFiE6H_6avpcRlmqi5Mn9C_u34JQGFXWM"))

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    try:
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

