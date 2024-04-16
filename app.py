# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt

# Setting up the main title and sidebar title of the application
st.title("Sentiment analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment analysis of Tweets about US Airlines")

# Markdown descriptions for main page and sidebar
st.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets 🐦")
st.sidebar.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets 🐦")

# Data URL from which the data will be loaded
DATA_URL = "Tweets.csv"

# Function to load data with caching to improve load performance
@st.cache_data(persist=True)  # Updated caching decorator
def load_data():
    data = pd.read_csv(DATA_URL)
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])  # Converting tweet creation times to datetime format
    return data

# Load the data using the defined function
data = load_data()

# Sidebar setup to show a random tweet based on selected sentiment
st.sidebar.subheader("Show random tweet")
random_tweet = st.sidebar.radio('Sentiment', ('positive', 'neutral', 'negative'), key='radio_random_tweet')
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[["text"]].sample(n=1).iat[0,0])

# Sidebar setup to show the number of tweets by sentiment and allow visualization selection
st.sidebar.markdown("### Number of tweets by sentiment")
select = st.sidebar.selectbox('Visualization type', ['Histogram', 'Pie chart'], key='select_visualization')
sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index, 'Tweets':sentiment_count.values})

# Displaying the selected visualization type for sentiment count
if st.sidebar.checkbox("Show sentiment count", True, key='checkbox_show_sentiment'):
    st.markdown("### Number of tweets by sentiment")
    if select == "Histogram":
        fig = px.bar(sentiment_count, x='Sentiment', y='Tweets', color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)

# Display a map of all tweet locations
st.map(data)

# Sidebar setup for analyzing tweets based on the time of day
st.sidebar.subheader("When and where are users tweeting from?")
hour = st.sidebar.slider("Hour of day", 0, 23, key='slider_hour')
modified_data = data[data['tweet_created'].dt.hour == hour]
if not st.sidebar.checkbox("Close map", True, key='checkbox_close_map'):
    st.markdown("### Tweets locations based on the time of day")
    st.markdown(f"{len(modified_data)} tweets between {hour}:00 and {(hour + 1) % 24}:00")
    st.map(modified_data)
    if st.sidebar.checkbox("Show raw data", False, key='checkbox_show_raw'):
        st.write(modified_data)

# Sidebar setup for filtering tweets by airline and sentiment
st.sidebar.subheader("Breakdown airline tweets by sentiment")
choice = st.sidebar.multiselect(
    'Pick airlines',
    ('US Airways', 'United', 'American', 'Southwest', 'Delta', 'Virgin America'),
    key='multiselect_airlines'
)

# Display histogram of sentiments for selected airlines
if len(choice) > 0:
    choice_data = data[data.airline.isin(choice)]
    fig_choice = px.histogram(
        choice_data, x='airline', y='airline_sentiment', histfunc='count', 
        color='airline_sentiment', facet_col='airline_sentiment', 
        labels={'airline_sentiment': 'tweets'}, height=600, width=800
    )
    st.plotly_chart(fig_choice)

# Sidebar option to generate and display a word cloud based on tweet sentiment
st.sidebar.header("Word Cloud")
word_sentiment = st.sidebar.radio(
    'Display word cloud for what sentiment?',
    ('positive', 'neutral', 'negative'),
    key='radio_word_sentiment'
)

# Generate and display word cloud if the option is not closed
if not st.sidebar.checkbox("Close word cloud", True, key='checkbox_close_wordcloud'):
    st.header(f'Word cloud for {word_sentiment} sentiment')
    df = data[data['airline_sentiment'] == word_sentiment]
    words = ' '.join(df['text'])
    processed_words = ' '.join(
        [word for word in words.split() if 'http' not in word and not word.startswith('@') and word != 'RT']
    )
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', height=640, width=800).generate(processed_words)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()  # Display the generated word cloud
