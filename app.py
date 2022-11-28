from flask import Flask , render_template ,request
import pickle as pkl 
import pandas as pd
import random

app = Flask(__name__)
app.run(debug=True)

anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
similarity = pkl.load(open('pickle_data/similarity.pkl','rb'))
animes = pd.DataFrame.from_dict(anime_dict)
titles = animes["title"].values

def anime_info(anime):
  anime_index=animes[animes['title'] == anime].index[0]
  return anime_index




def recommender(anime):
  anime_index = animes[animes['title'] == anime].index[0]
  distances = similarity[anime_index]
  anime_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
  anime_list5 =random.sample(anime_list,k=5)

  recommended_list = []
  poster_image=[]

  for i in anime_list5:
    recommended_list.append(animes.iloc[i[0]].title)
    poster_image.append("static/images/anime_posters/"+str(i[0]) + '.jpg')
  return recommended_list, poster_image


page_titles =["myAnime","recommend","recomendations"]

@app.route('/')
@app.route('/home')
def anime_name():
    return render_template('index.html',web_title=page_titles[0])

@app.route('/recommend')
def recommend():
    return render_template('recommend.html' ,titles = titles , web_title=page_titles[1])

@app.route('/recommendation', methods=["POST","GET"])
def recommendation():
    anime_title = ""
    #if request.method =="POST":
    anime_title = request.form.get("title")
    if not anime_title:
       return render_template('recommendation_empty.html',titles=titles,web_title=page_titles[1])
    name,image=recommender(anime_title)
    return render_template('recommendations.html' , names=name ,images=image , titles=titles , web_title=page_titles[2])

     #else:
      #return "Something went wrong"
