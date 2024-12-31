from flask import Flask

app = Flask(__name__)

@app.route("/wish")
def pleaseWish():
    return "Hello, Jenkins"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
    
# the default port number is always 5000
# 0.0.0.0 --> from any computer with any ip address we can connect to this flask application
