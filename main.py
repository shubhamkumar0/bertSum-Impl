import time
from summarizer import Summarizer

from flask import Flask, request, render_template

app = Flask(__name__)
model = Summarizer()


@app.route("/")
def home():
    try:
        return render_template("home2.html")
    except Exception as e:
        print(e)


@app.route("/predict", methods=["POST"])
def predict():
    print("1")
    text = [x for x in request.form.values()]
    print("2")
    print("text: {}".format(text[0]))
    if not model:
        loc_model = Summarizer()
    else:
        loc_model = model
    print("3")
    tic = time.perf_counter()
    result = loc_model(text[0], min_length=1, max_length=10000)
    toc = time.perf_counter()
    print(f"Ran the model in {toc - tic:0.4f} seconds")
    print("4")
    summary = "".join(result)
    return render_template("suggestion2.html", summary=summary)


@app.route("/favicon.ico")
def random():
    return render_template("home2.html")


if __name__ == '__main__':
    # app.run(debug=True, port=5100)
    app.run(host='0.0.0.0', port=8080)
