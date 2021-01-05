import time
from summarizer import Summarizer
from transformers import *

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    try:
        return render_template("home2.html")
    except Exception as e:
        print(e)
        logger.info(e)


@app.route("/predict", methods=["POST"])
def predict():
    print("1")
    text = [x for x in request.form.values()]
    print("2")
    print("text: {}".format(text[0]))
    custom_config = AutoConfig.from_pretrained('allenai/scibert_scivocab_uncased')
    custom_config.output_hidden_states = True
    custom_tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
    custom_model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased', config=custom_config)
    model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer)
    tic = time.perf_counter()
    result = model(text[0], min_length=1, max_length=10000)
    toc = time.perf_counter()
    print("4")
    summary = "".join(result)
    return render_template("suggestion2.html", summary=summary)


@app.route("/favicon.ico")
def random():
    return render_template("home2.html")


if __name__ == '__main__':
    app.run(debug=True)
