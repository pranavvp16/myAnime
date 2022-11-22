from cgitb import html
from flask import Flask , render_template ,request
import pickle as pkl 
import pandas as pd
import random

app = Flask(__name__)

anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
similarity = pkl.load(open('pickle_data/similarity.pkl','rb'))
anime = pd.DataFrame.from_dict(anime_dict)
titles = anime["title"].values


def recommender(animes):
  anime_index = anime[anime['title'] == animes].index[0]
  distances = similarity[anime_index]
  anime_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
  anime_list5 =random.sample(anime_list,k=5)

  recommended_list = []
  poster_image=[]

  for i in anime_list5:
    recommended_list.append(anime.iloc[i[0]].title)
    poster_image.append("static/images/anime_posters/"+str(i[0]) + '.jpg')
  return recommended_list, poster_image


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
        anime_title = request.form["title"]
        name,image=recommender(anime_title)
        return render_template('recommendations.html' , names=name ,images=image)

    else:
        return "Something went wrong"
