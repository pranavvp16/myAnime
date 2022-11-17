from cgitb import html
from flask import Flask , render_template
import pickle as pkl 
import pandas as pd
app = Flask(__name__)
app.run(debug=True)

anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
similarity = pkl.load(open('pickle_data/similarity.pkl','rb'))
anime_df = pd.DataFrame.from_dict(anime_dict)


@app.route('/')
def anime_name():
    return render_template('index.html')

@app.route('/recommend')
def recommendation():
    return " ON recommendation page"