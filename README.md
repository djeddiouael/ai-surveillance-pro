# 🧠 AI Surveillance PRO System

A real-time AI-powered surveillance system using YOLO, PyTorch, OpenCV, and Flask dashboard.

---

## 🚀 Features

- 🎥 Real-time object detection (YOLOv8)
- 👤 People counting system
- 🚨 Crowd alert system
- 📝 Event logging system
- 💾 Video recording on detection
- 🌐 Professional web dashboard (Flask)

---

## 🛠️ Tech Stack

- Python 🐍
- PyTorch
- YOLOv8 (Ultralytics)
- OpenCV
- Flask (Dashboard)
- HTML/CSS

---

## 📁 Project Structure

```
ai_surveillance_pro/
│
├── main.py              # AI camera system
├── logger.py            # Logging system
├── app.py               # Flask dashboard
├── logs.txt             # Event logs
├── recordings/          # Saved videos
└── templates/
    └── dashboard.html   # Web UI
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-surveillance-pro.git
cd ai-surveillance-pro
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install ultralytics opencv-python torch torchvision flask
```

---

## ▶️ Run Project

### 1. Run AI Camera

```bash
python main.py
```

### 2. Run Dashboard

```bash
python app.py
```

Then open: `http://127.0.0.1:5000`

---

## 📊 System Overview

The system works like this:

```
Camera → YOLO Model → Detection → Counting → Alerts → Logs + Video Save → Dashboard
```

---

## 🚨 Alerts System

- If number of people > 2 → Crowd alert triggered
- Event is saved in logs
- Video is recorded automatically

---

## 🌐 Dashboard Features

- View logs in real-time
- See recorded events
- Clean dark UI interface

---

## 🔥 Future Improvements

- Face recognition system
- Live video streaming in dashboard
- Database integration (SQLite / MongoDB)
- Mobile app version