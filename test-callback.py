import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()


""" app = Flask(__name__)

@app.route("/callback", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
def callback():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) """


print("LINE_TOKEN:", os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))