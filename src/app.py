from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hii ROBOT, HOW ARE YOU????";

if __name__ == "__main__":
    app.run()

