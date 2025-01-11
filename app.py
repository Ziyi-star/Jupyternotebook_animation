import os
import subprocess
from flask import Flask, redirect

# Create a Flask app
app = Flask(__name__)

# Health check endpoint
@app.route("/")
def health_check():
    return "Health Check Passed! Flask is running."

# Voilà endpoint
@app.route("/voila/")
def voila_app():
    # Bind Voilà to Heroku's $PORT
    port = os.environ.get("PORT", 5000)
    voila_command = [
        "voila",
        "Mittelwertsatz.ipynb",
        "--port=" + str(port),
        "--no-browser",
        "--strip_sources=True",
    ]
    # Launch Voilà
    subprocess.Popen(voila_command)
    return redirect(f"http://localhost:{port}")

if __name__ == "__main__":
    # Run Flask on Heroku's $PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
