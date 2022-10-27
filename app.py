from flask import flask , render_template
import pickle as pkl 

anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
similarity = pkl.load(open('pickle_data/similarity.pkl','rb'))


@app.route('/'){
 def anime_name(){
    return anime
 }
}


