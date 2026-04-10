from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    # LOAD LOGS
    logs = []
    if os.path.exists("logs.txt"):
        with open("logs.txt", "r", encoding="utf-8") as f:
            logs = f.readlines()

    # LOAD VIDEOS
    videos = []
    if os.path.exists("recordings"):
        videos = os.listdir("recordings")

    return render_template("dashboard.html",
                           logs=logs[-20:],
                           videos=videos)

if __name__ == "__main__":
    app.run(debug=True)