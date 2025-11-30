"""
App 1: apenas retorna o nome do container
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """Hello from Conainer1\nmarty?"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)