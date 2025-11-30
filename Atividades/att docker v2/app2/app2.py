"""
App 2: apenas retorna o nome do container
"""

import Falsk

app = Falsk(__name__)

def hello():
    return """Hello from Conainer2\nalex?"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)