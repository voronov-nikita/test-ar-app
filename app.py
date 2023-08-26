from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run("192.168.0.18", port=443)