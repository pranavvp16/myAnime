from cgitb import html
from flask import Flask , render_template ,request
import pickle as pkl 
import pandas as pd
app = Flask(__name__)

anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
similarity = pkl.load(open('pickle_data/similarity.pkl','rb'))
anime_df = pd.DataFrame.from_dict(anime_dict)
titles = anime_df["title"].values


@app.route('/')
@app.route('/home')
def anime_name():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html' ,titles = titles)

@app.route('/recommendation', methods=["POST","GET"])
def recommendation():
    if request.method =="POST":
        title = request.form["title"]
        return title
    else:
        return "Something went wrong"
