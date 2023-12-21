# Movies Capstone Project

## Problem Statement
This project is divided into two parts: 
* **The story of film:** This section objective is narrating the history, trivia and facts behind the world of cinema through the lens of data. Extensive Exploration Data Analysis (EDA) is performed on Movie Metadata about Movie Revenues, Casts, Crews, Budget, etc. through the years. Two predictive models are built to predict movie revenues and movie success. Through these models, what features have the most significant impact in determining revenue and success could be discovered later.
* **Movie recommender systems:** This part is concentrated on building multiple kinds of recommendation engines, named the Simple Generic Recommenders, the Content Based Filter and the User Based Collaborative Filter. The performance of the systems is evaluated in both a qualitative and quantitative manner.


## Approach 

The problem was divided into several steps:

1. **Data Collection:** Data was collected from the MovieLens [website](https://grouplens.org/datasets/movielens/) and through a script that queried for data from various TMDB Endpoints.

#### Data description

MovieLens has a publicly available *full dataset* containing approximately 33,000,000 ratings and 2,000,000 tag applications applied to 86,000 movies by 330,975 users between January 09, 1995 and July 20, 2023. Includes tag genome data with 14 million relevance scores across 1,100 tags. This dataset was generated on July 20, 2023. A *small subset* of the dataset, containing 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users between March 29, 1996 and September 24, 2018. The subset was generated on September 26, 2018.

One of the files contains the TMDB ID of every movie listed in the MovieLens dataset. Using this ID, the metadata, credits and keywords of all 86,000 movies were obtained by running a script that requested and parsed data from TMDB Open API. The data collected was initially in the JSON format but was converted into CSV files using Python’s Pandas Library.

More details about the contents and use of all these files is given in README.txt

The following files were used in the project from both MovieLens subset database and TMDB:

```
movies_metadata.csv
credits.csv
keywords.csv
links_small.csv
ratings_small.csv
```

2. **Data Wrangling:** The datasets were uploaded to a dataframe and explored. Null values were filled in wherever appropriate and polluted values were discarded or wrangled.

3. **EDA:** Extensive data visualisation and summary statistics were used to extract insights and pattern from the various datasets. The history, facts and trivia behind movies were narrated through data.

4. **Machine Learning:** Gradient Boosting Classifer and Regressor were trained on our feature engineered dataset to predict movie success and revenue respectively. Their feature importances were noted to gain insights into what factors influence the revenues of a movie relative to budget.

5. **Recommendation Systems:** Four different recommendation systems were built using various ideas and algorithms such as IMDB's Weighted Rating, Content Based Filtering and Collaborative Filtering.


## Final Results 

A Gradient Boosting Regressor and Classifier were built to predict Movie Revenue and Success respectively with a Score of 0.78 and 0.8 respectively.

In addition, four recommendation engines were built based on different ideas and algorithms:

* **Simple Recommender:** This system used overall TMDB Vote Count and Vote Averages to build Top Movies Charts, in general and for a specific genre. The IMDB Weighted Rating System was used to calculate ratings on which the sorting was finally performed.

* **Content Based Recommender:** I built two content based engines; one that took movie overview and taglines as input and the other which took metadata such as cast, crew, genre and keywords to come up with predictions. I also devised a simple filter to give greater preference to movies with more votes and higher ratings.

* **Collaborative Filtering:** I used the powerful Surprise Library to build a collaborative filter based on singular value decomposition. The RMSE obtained was less than 1 and the engine gave estimated ratings for a given user and movie.

* **Hybrid Engine:** I brought together ideas from content and collaborative filtering to build an engine that gave movie suggestions to a particular user based on the estimated ratings that it had internally calculated for that user.


## Repository Structure

1. **movies_eda.ipynb:** The Jupyter notebook that contains the EDA and narrates the Story of Film.

2. **movies_recommender.ipynb:** The Jupyter notebook containing code for the recommendation engines.

3. **Movies Final Report.pdf:** The Final Report.

4. **scraper:** The folder containing all the scrapers used to gather data from TMDB.


## Code credit

Code credits for this code go to [Rounak Banik](https://github.com/rounakbanik).

