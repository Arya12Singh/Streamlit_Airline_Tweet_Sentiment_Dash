# US Airlines Tweet Sentiment Analysis Dashboard

## Overview
This project utilizes a Streamlit dashboard to analyze and visualize the sentiment of tweets regarding US airlines. The application is designed to provide insights into public sentiment by analyzing tweets from a dataset, helping users understand customer perceptions and experiences with different airlines.

## Features
- **Tweet Sentiment Visualization**: View random tweets categorized by sentiment (positive, neutral, negative).
- **Sentiment Distribution Charts**: Dynamic histograms and pie charts showing the distribution of sentiments across all tweets.
- **Geographic Tweet Mapping**: Interactive maps displaying the locations from which tweets were sent, with filters for time of day.
- **Airline Sentiment Breakdown**: Analysis of tweet sentiments by specific airlines.
- **Word Clouds**: Visual representations of the most common words found in tweets, categorized by sentiment.

## Technologies Used
- **Streamlit**: For creating the web application.
- **Pandas**: For data manipulation and analysis.
- **Plotly Express**: For interactive data visualization.
- **WordCloud and Matplotlib**: For generating word clouds and other visualizations.

## Project Structure
- `app.py`: The main Python file with Streamlit code that runs the dashboard.
- `Tweets.csv`: The dataset used in this project, containing tweets about US airlines.

## Installation
To run this project locally, you need to have Python installed on your machine. You can then follow these steps:

1. Clone this repository to your local machine using:
git clone https://github.com/Arya12Singh/StreamlitAirlineSentiment.git

2. Navigate to the project directory:
cd StreamlitAirlineSentiment

3. Install the required Python libraries:
pip install -r requirements.txt

## Running the Application
Execute the following command in the terminal:
streamlit run app.py

This will start the Streamlit server, and the dashboard should open in your default web browser.

## Contributing
Contributions to this project are welcome! Please fork this repository and submit a pull request with your proposed changes.

## License
This project is open-source and available under the MIT License.

## Contact
For questions or feedback, please open an issue in this GitHub repository.
