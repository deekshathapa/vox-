from flask import Flask
from flask_socketio import SocketIO, send
import datetime, random

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "Backend is running!"

@socketio.on("message")
def handle_message(msg):
    msg = msg.lower().strip()
    print(f"User said: {msg}")

    response = "I'm not sure how to help with that."

    # Greetings
    if "hello" in msg or "hi" in msg:
        response = "Hello, I am Vox AI! How can I assist you today?"

    # Time & Date
    elif "time" in msg:
        response = f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "date" in msg:
        response = f"Today's date is {datetime.datetime.now().strftime('%A, %d %B %Y')}"

    # YouTube
    elif "youtube" in msg:
        if "search" in msg:
            query = msg.replace("youtube search", "").strip()
            response = f"Searching YouTube for {query}..."
        else:
            response = "Opening YouTube..."

    # Google
    elif "google" in msg:
        if "search" in msg:
            query = msg.replace("google search", "").strip()
            response = f"Searching Google for {query}..."
        else:
            response = "Opening Google..."

    # General search
    elif msg.startswith("search "):
        query = msg.replace("search", "").strip()
        response = f"Searching Google for {query}..." if query else "Please tell me what to search for."

    # Wikipedia
    elif "wikipedia" in msg:
        response = "Opening Wikipedia..."

    # Calculator
    elif msg.startswith("calculate "):
        try:
            expression = msg.replace("calculate", "").strip()
            result = eval(expression)
            response = f"The result of {expression} is {result}"
        except Exception:
            response = "Sorry, I couldn’t calculate that."

    # Weather
    elif "weather in" in msg:
        city = msg.replace("weather in", "").strip()
        response = f"Showing weather in {city}..."
    elif "weather" in msg:
        response = "Showing today’s weather..."

    # News
    elif "news about" in msg:
        topic = msg.replace("news about", "").strip()
        response = f"Fetching latest news about {topic}..."
    elif "news" in msg:
        response = "Opening Google News..."

    # Jokes
    elif "joke" in msg or "funny" in msg:
        jokes = [
            "Why don’t programmers like nature? It has too many bugs.",
            "Parallel lines have so much in common… it’s a shame they’ll never meet.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        response = random.choice(jokes)

    # Motivation
    elif "motivate" in msg or "inspire" in msg or "quote" in msg:
        quotes = [
            "Push yourself, because no one else is going to do it for you.",
            "Dream it. Wish it. Do it.",
            "Great things never come from comfort zones.",
            "Don’t stop when you’re tired. Stop when you’re done."
        ]
        response = random.choice(quotes)

    # Fun facts
    elif "fact" in msg:
        facts = [
            "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.",
            "Bananas are berries, but strawberries are not.",
            "Octopuses have three hearts."
        ]
        response = random.choice(facts)

    # Music
    elif "music" in msg or "spotify" in msg:
        response = "Opening Spotify for music..."

    send(response)

if __name__ == "__main__":
    import eventlet
    import eventlet.wsgi
    socketio.run(app, host="0.0.0.0", port=5000)
