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
- `Tweets.csv`: The dataset used in this project, contains tweets about US airlines.

## Getting Started

To run the Airline Tweet Sentiment Dashboard locally, follow these steps:

1. **Install Python and Required Libraries**:
   - Ensure Python is installed on your system. If not, download it from [python.org](https://www.python.org/downloads/).
   - Install Streamlit, Pandas, Plotly, WordCloud, Matplotlib, and other necessary libraries. You can install all required libraries using pip:
     ```
     pip install -r requirements.txt
     ```

2. **Clone This Repository**:
   - Use Git to clone the repository to your local machine:
     ```
     git clone https://github.com/Arya12Singh/AirlineTweetSentimentDash.git
     ```

3. **Navigate to the Project Directory**:
   - Change your directory to the cloned repository:
     ```
     cd AirlineTweetSentimentDash
     ```

4. **Run the Application**:
   - Start the dashboard using Streamlit by running the following command in your terminal:
     ```
     streamlit run app.py
     ```
   - This will start the Streamlit server, and the dashboard should automatically open in your default web browser.

By following these steps, you will be able to set up and run the Airline Tweet Sentiment Dashboard on your local environment. This allows you to interact with the sentiment analysis visualizations and explore the data.

For a more detailed version of the project, check my blog https://aryasingh.hashnode.dev/harnessing-twitter-sentiment-analysis-for-us-airlines-a-streamlit-dashboard-exploration/

## License
This project is open-source and available under the MIT License.

## Contact
For questions or feedback, please open an issue in this GitHub repository.
