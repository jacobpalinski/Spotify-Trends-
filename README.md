## Spotify Popular Songs Analysis
### Project Overview 
The Spotify Popular Songs Analysis project is an analysis of almost 5000 songs across the genres of:
- Trance
- Rock
- Country 
- Rap
- R&B

These songs came from public Top 1000 playlists for each of these genres. Why 1000? I wanted larger playlists so I could have ample data to work with when 
predicting song popularity. The primary objective of the project was to identify the features of tracks and their relative importance for a number of different genres.

### About the Data 
- Track Data: Five playlists, each having ~1000 songs with the exception of the Country genre. Total of 4736 rows and 41 columns.
- Audio Features: Retrieved using Track ID from Track Data. Same number of rows and 20 columns.

Both datasets were retreived from the Spotify API and had to be normalized from JSON formats to dataframes.

#### Audio Features Used
- **Acousticness**: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
- **Danceability**: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, 
and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- **Energy**: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. 
For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, 
perceived loudness, timbre, onset rate, and general entropy.
- **Instrumentalness**: Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are 
clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent 
instrumental tracks, but confidence is higher as the value approaches 1.0.
- **Loudness**: the overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of 
tracks. 
Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
- **Speechiness**: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audiobook, poetry), 
the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks 
that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other 
non-speech-like tracks.
- **Valence**: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive 
(e.g. happy, cheerful, euphoric),while tracks with low valence sound more negative (e.g. sad, depressed, angry).
- **Tempo**: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from 
the average beat duration.

## Steps Taken
1. Retreived data from API and normalized into dataFrames. 
2. Cleaned Data: Deleted irrelevant columns, dropped duplicates, changed data types, removed null values using Pandas
3. Data Analysis: Developed visualisations and performed statistical analysis of features.
4. Developed Predictive Model for Song Popularity

Libraries Used: Numpy, Pandas, Matplotlib, Seaborn, Scipy.Stats, Requests
Model: RandomForestRegressor

## Analysis of Results
The rock, country and trance genres had a left-tailed release year distribution. Trance is the most modern genre with earliest released song being in 1995 compared to the
1960s for country and rock. Rap has a more normal distribution with a mean around the 2000s, with the 1970s and 2000s representing r&b songs. 

Explicity was only "common" in the rap genre. 

Song popularity tended to increase with release year for the country and trance genres, however this was not the case for rock, rap and r&b music.

For all songs, duration distribution was positively skewed. For the r&b and country genres, duration had a normal distribution according to the Shapiro Wilks Test 
with p-values> 0.05. I utilised ANOVA to comparing duration means with differences between means being statistically siginificant to reject the null hypothesis that
durations between genres are equal.

Loudness had a positive correlation with energy with an r-squared value of 0.52. There was a mild negative relationship between Acoustincess and Energy. 
Release Year and Energy had a positive relationship, however that could be explained by the fact that the majority of trance songs were released >2010. 
Energy and acousticness, and loudness and acoustincess had negative correlations with r-squared values of -0.6 and -0.44 respectively.

RandomForestRegressor was used to predict popularity based on explcity, danceability, energy, loudness, speechiness, acousticness, instrumentalness, valence, tempo,
duration and release year as features. Best N estimator was tested for each genre. 

Top 3 most important features for predicting song popularity (with feature importance value) were:
- Rock: release year 0.23, energy 0.16, acousticness 0.14
- Country: duration 0.21, loudness 0.21, acousticness 0.19
- Rap: release year 0.16, loudness 0.13, danceability 0.12
- R&B: release year 0.12, duration 0.12, loudness 0.12
- Trance: release year 0.16, instrumentalness 0.15, acousticenss, 0.10

