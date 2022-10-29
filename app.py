from cgitb import html
from flask import Flask , render_template
import pickle as pkl 
app = Flask(__name__)

anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
similarity = pkl.load(open('pickle_data/similarity.pkl','rb'))


@app.route('/')
def anime_name():
    return "Hello World THis "

