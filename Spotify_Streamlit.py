import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


header = st.beta_container()
date_distribution = st.beta_container()
popularity = st.beta_container()
correlation_plot = st.beta_container()
ml_model= st.beta_container()

@st.cache
def get_data():
    song_data = pd.read_csv(r'C:\Users\kpali\Documents\Python_Projects\Spotify\song_data.csv')
    return song_data

with header:
    st.title('Spotify Popular Songs Project')
    st.subheader('Project Purpose')
    st.markdown('The Spotify Popular Songs Analysis project is an analysis of almost 5000 songs across the genres of: Trance, Rock, Country, Rap and R&B. These songs come from top 1000 playlists for these genres. The primary objective of the analysis was to identify the features of tracks and their relative importance for a number of different genres.')

with date_distribution:
    st.subheader('Release Date Distribution by Genre')
    
    song_data = get_data()

    genre = st.selectbox('Which Genre?',['Rock', 'Country', 'Rap', 'R&B', 'Trance'])
    fig,ax=plt.subplots(figsize=(10,5))
    ax.hist('release_year',data=song_data[song_data['genre'] == genre],edgecolor='black')
    st.pyplot(fig)

with popularity:
    st.subheader('Popularity by Release Year')
    fig,ax=plt.subplots(figsize=(10,5))
    ax.scatter(x='release_year',y='track.popularity',c='green',data=song_data[song_data['genre'] == genre],edgecolor='black')
    st.pyplot(fig)

with correlation_plot:
    st.subheader('Correlation between Track Features')
    fig,ax=plt.subplots(figsize=(12,6))
    sns.heatmap(song_data[song_data['genre'] == genre].corr(), annot=True)
    st.write(fig)

with ml_model:
    st.subheader('Detecting Feature Importance')

    n_estimators=st.slider('n_estimators of the model', min_value=10, max_value=300, value=20, step=10)
    
    predictors = ['track.explicit','danceability','energy','loudness','speechiness','acousticness','instrumentalness',
           'valence','tempo','duration','release_year']
    outcome = 'track.popularity'
    X=song_data[song_data['genre'] == genre ][predictors]
    y=song_data[song_data['genre'] == genre ][outcome]

    X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.3)
    rf=RandomForestRegressor(n_estimators=n_estimators,random_state=1)
    rf.fit(X_train, y_train)

    fig,ax=plt.subplots(figsize=(12,6))
    plt.barh(predictors, rf.feature_importances_, color='cyan')
    plt.title('Feature Importance '+genre)
    plt.xlabel('Feature Importance')
    plt.ylabel('Predictor')
    st.pyplot(fig)













