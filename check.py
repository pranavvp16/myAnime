import pickle as pkl
import pandas as pd
anime_dict = pkl.load(open('pickle_data/anime_dict.pkl','rb'))
anime = pkl.load(open('pickle_data/anime_info.pkl','rb'))
anime_info_df = pd.DataFrame.from_dict(anime)

print(anime_info_df.description[:5])