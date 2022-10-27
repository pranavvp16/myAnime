import streamlit as st
import pickle as pkl
import pandas as pd
import os
#FOLDER_PATH='anime_posters'
#filenames=os.listdir(FOLDER_PATH)

def recommend(animes):
  anime_index = anime[anime['title'] == animes].index[0]
  distances = similarity[anime_index]
  anime_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]

  recommended_list = []
  poster_image=[]

  for i in anime_list:
    recommended_list.append(anime.iloc[i[0]].title)
    poster_image.append("anime_posters/"+str(i[0]) + '.jpg')
  return recommended_list , poster_image

anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
anime = pd.DataFrame(anime_dict)
similarity  = pkl.load(open('pickle_data/similarity.pkl','rb'))
#image = pkl.load(open('image_urls.pkl','rb'))

st.title('Anime recommendation system')
selected_anime= st.selectbox(
    'Select your anime',
    (anime['title'].values))
if st.button('Recommend'):
    #st.write(selected_anime)
    names,posters=recommend(selected_anime)

    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.caption(names[0])
        st.image(posters[0])

    with col2:
        st.caption(names[1])
        st.image(posters[1])

    with col3:
        st.caption(names[2])
        st.image(posters[2])

    with col4:
        st.caption(names[3])
        st.image(posters[3])

    with col5:
        st.caption(names[4])
        st.image(posters[4])


