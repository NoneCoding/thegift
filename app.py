from flask import Flask, render_template
from datetime import date
app = Flask(__name__)

@app.route("/")
def check_date():
    dt = date.today()

    ans = "É hoje!" if dt == "2023-09-17" else "Ainda não!"

    return render_template("index.html", ans=ans)
