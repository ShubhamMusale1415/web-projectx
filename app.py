import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
# for installing streamlit pip install streamlit
# commnads to run:streamlit run app.py
API_KEY = "1e2ab794"


def fetch_movie_poster(mov):
    """Fetches movie poster from OMDB API using IMDB ID"""
    url = f"https://www.omdbapi.com/?i={mov}&apikey=1e2ab794"
    response = requests.get(url)
    data = response.json()
    return data.get("Poster", "No poster found")



st.title("movie recommendation system")
movieslist=pickle.load(open("movex.pkl","rb"))
cxf=pickle.load(open("cxf.pkl","rb"))
moviname=movieslist["title"].values
option = st.selectbox(
    "How would you like to be contacted?",
    # ("Email", "Home phone", "Mobile phone"),
    moviname
)


def recommend(movie):
    y=[]
    movieid = movieslist[movieslist["title"] == movie].index[0]
    idlist = sorted(list(enumerate(cxf[movieid])), reverse=True, key=lambda x: x[1])[1:6]
    ids=[]
    for i in idlist:
        y.append(movieslist["title"][i[0]])
        ids.append(i[0])
    return  [y,ids]

px=pickle.load(open("px.pkl","rb"))

# if st.button("Recommend 5 movies"):
#     list=recommend(option)
#     # for i in list[0]:
#     #     st.write(i)
#     # for j in list[1]:
#     #     j=movieslist["id"][j]
#     #     xmt=px[px['id_tmdb'] == j].iloc[0]["id_imdb"]
#     #     poster_url=fetch_movie_poster(xmt)
#     #     if poster_url != "No poster found":
#     #         st.image(poster_url, width=300)
#     #     else:
#     #         st.error("Poster not found! Check the Movie ID.")
#     #         st.write(j)
#     #         st.write(px[px['id_tmdb'] == j].iloc[0]["id_imdb"])
#     for i,j in zip(list[0],list[1]):
#         st.write(i)
#         j=movieslist["id"][j]
#         xmt=px[px['id_tmdb'] == j].iloc[0]["id_imdb"]
#         poster_url=fetch_movie_poster(xmt)
#         if poster_url != "No poster found":
#             st.image(poster_url, width=300)
#         else:
#             st.error("Poster not found! Check the Movie ID.")
#             st.write(j)
#             st.write(px[px['id_tmdb'] == j].iloc[0]["id_imdb"])
#

# if st.button("Recommend 5 movies"):
#     recommended = recommend(option)
#     titles = recommended[0]
#     indices = recommended[1]
#
#     cols = st.columns(5)  # Show posters in 5 columns
#
#     for i in range(5):
#         with cols[i]:
#             st.markdown(f"**{titles[i]}**")
#             tmdb_id = movieslist["id"][indices[i]]
#             try:
#                 imdb_id = px[px['id_tmdb'] == tmdb_id].iloc[0]["id_imdb"]
#                 poster_url = fetch_movie_poster(imdb_id)
#                 if poster_url != "No poster found":
#                     st.image(poster_url, use_container_width=True)
#                 else:
#                     st.warning("Poster not found")
#             except:
#                 st.warning("IMDb ID not found")

if st.button("Recommend 5 movies"):
    recommended = recommend(option)
    titles = recommended[0]
    indices = recommended[1]

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown(f"**{titles[i]}**", unsafe_allow_html=True)
            tmdb_id = movieslist["id"][indices[i]]
            try:
                imdb_id = px[px['id_tmdb'] == tmdb_id].iloc[0]["id_imdb"]
                poster_url = fetch_movie_poster(imdb_id)
                if poster_url != "No poster found":
                    st.image(poster_url, use_container_width=True)
                else:
                    st.warning("Poster not found")
            except:
                st.warning("IMDb ID not found")

            # Add vertical space after each movie block
            st.markdown("<br><br>", unsafe_allow_html=True)
