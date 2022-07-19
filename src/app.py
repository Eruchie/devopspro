from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Devops_Task_June"


if __name__ == "__main__":
    app.run()


