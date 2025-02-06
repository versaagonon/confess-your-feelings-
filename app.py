from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")

if __name__ == "__main__":
    app.run(debug=True)
