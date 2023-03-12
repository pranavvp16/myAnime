
# myAnime
![Banner Poster](https://i1.wp.com/wayofthesigmamale.com/wp-content/uploads/2021/08/mugen_s_shadow_by_gdroland_d47u4l9-fullview.jpg?resize=768%2C160&ssl=1)

myAnime is project that gives anime fans recommendations based 
on the anime they liked in the past. It a Content-Based filtering recommendation system
therefore ,the recommendations are specific to the User only and not 
affected by the interests of others(Collaborative-Based-filtering)



## Dataset

This Recommendation model was built from dataset having 3409 Anime data which was furthur processed to 3181 Anime data
 - [Kaggle link to Datset](https://www.kaggle.com/code/beautifulmelodies/anime-dataset-analysis-from-1990-to-2022)
 
 ![Types in the Dataset](https://www.kaggleusercontent.com/kf/99156706/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..cIlzhMA4LKINWnkfDdtvkg.kO4Cqat3c5oSE17Pe9Om1X3YV1oWY2Ty6QKpHPcf5mZgb2RpnpBI-je_TRlnnbAtMpRYz10tJcqsoipRIjT4JdJdjo-SMcQ41bmI6yEBb5yHaH4l7w2N1EIiM7ve4XYN5jbS29a_73oNuPZkbZjAeeXPPs5yegprxV1yxNEM61BDLV3N10mundDt4dMiUem-NngvUJloFdAC7LRlNT6nNRIL6sOnOAIgN0UFrJzo0gEYGJW0cQcgSr-i2i_vPm1VGkH4asYOLFpMSBvdDQqy3c01BKg7O0IUsvrgUoHoWDBNZ6s5bFnBoE1zsOUx7V5VzRKpCDBZSL4H-uyhNz7Kcr9pBVC299Fj6Ah53K4GcEVqCLYJvEh7aXxFTHA4Xl7fPKcRrbukfcT7ldQt17lwnN5kiINiAGmiynnT3TQEuE5LoIvxT5WAymzaULnVXKqTCSiyA7aAPTGtcjIbBwq6lvXy1-YTm_TzFJhNLg4gBuOG9qgCGfKRWCgYdK1gWyNID08J-RRjTNFrZBgK4sG5iMRx_stiznW0wHV4VCnAIia6TenfxqS4SUkobUQxoPSln3U5YkC6otstzonR5DxL_RItiKZZ_3KDiBdtd80_ZdirksQ_qJd6JMUvAcWllhRLSclmNC1rJFpAEAmrKAX8PBT9j4nsTQufZ79jdca8uxONvgaSWnH1N0ofjFwGRa7ISRdJ9QJwy14KF1AKBMhYVg.Vo8U5gNPbvwGlHbWkNYcyQ/__results___files/__results___22_0.png)

The above image shows the different types of anime in the dataset through a histogram. "Pelicula" in the image refers to "Movie". 
### Pickle data
Similarity array is coverted to similarity.pkl to avoid training model everytime , similarily dataset and image urls are coverted to pickle to start directly working on web app.


## Demo

This Project is Deployed on Heroku [Link]( https://anime-recommendation-mlh.herokuapp.com)

## Run Locally

Clone the project

```bash
  git clone https://github.com/pranavvp16/AnimeOnly.git
```

Go to the project directory --> open "anime_posters" --> download the posters using download_posters.py


Install dependencies

```bash
  pip install flask
```

Start the server

```bash
  flask run 
```


### Support

For support, email pranavprajapati586@gmail.com.


## Screenshots

![App Screenshot](app_screenshots/homepage.png)

