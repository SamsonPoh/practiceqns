# Simple web application using Flask framework
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Samson!</p>" #Line edited for Step 2

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

# This line is edited on Saturday Jan 13, 2024.
