#testpy2
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello() -> str:
    """Return a friendly HTTP greeting.
    
    Returns:
        A string with the words 'Hello World!'.
    """
    return "Hello World!"
#ssl hash key, cicd, version control 

if __name__ == "__name__":
    app.run(host="127.0.0.1", port=8800, debug=True)