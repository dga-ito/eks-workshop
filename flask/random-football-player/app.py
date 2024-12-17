from flask import Flask, render_template
import datetime
from random_app import get_random_menu


app = Flask(__name__)


@app.route('/')
def home():
    menu = get_random_menu()
    today = datetime.datetime.now().strftime("%A" ", " "%B" " " "%Y")

    return render_template(
        "index.html",
        today=today,
        menu=menu,
    )


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0")