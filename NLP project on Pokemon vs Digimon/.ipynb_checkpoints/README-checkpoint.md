#  ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3 - NLP project on Pokemon vs Digimon

**Primary Learning Objectives:**
1. Creating a classification model


# Problem Statement

We want to use word input by users to help recommend whether pokemon or digimon is more suitable for a user. This is to recommend the correct subreddit link or merchandise to the user.


# Data set
* [`pokemon_data.csv`](./datasets/pokemon_data.csv): pokemon data set collected from pokemon subreddit
* [`digimon_data.csv`](./datasets/digimon_data.csv): digimon data set collected from pokemon subreddit
* [`combine_df.csv`](./datasets/combine_df.csv): combine pokemon and digimon data for futher cleaning
* [`clean_combine_df`](./datasets/clean_combine_df.csv): Pre-processed data set for training


# Technical Report 

The technical report is split into 3 part in the code file:

1. Data_collection: Data collecting from reddit
2. EDA: Data Analysis with visual plot
3. Data_cleaning_modeling: Prepare Data and conduct modeling


# EDA
- Pokemon wordcloud
![image](./plot/wordcloud_pokemon.png)


###

- Digimon wordcloud
![image2](./plot/wordcloud_digimon.png)

###

- Top word in Data
![image3](./plot/1word_count.png)



###

- Top Bi-Gram in Data
![image5](./plot/2word_count.png)

###
- Coefficient for Pokemon
![image6](./plot/coef_pokemon.png)

###
- Coefficient for Pokemon
![image7](./plot/coef_digimon.png)

# Performance of model

- Table of 4 different model score
![image8](./plot/model_compare.png)


# Conclusions and Recommendation:

From EDA, Data from both digimon and pokemon subreddits have similar words being mentioned. 

For example:'pokemon','game','super effective'. 

From digimon data, we can also tell that users also know about pokemon, but from the pokemon data we can tell users who know pokemon might not know about digimon as it is rarely mentioned. 

Therefore if we recommend a subreddit link or merchandise to a new user by using his/her input, we will likely recommend pokemon as compared to digimon. In this project, Naive Bayes model was chosen due to the higher accuracy and recall compared to other model.



# Things to be improve in the future:
1. I will want to collect more data so the model will be more accurate. as the current model have only 2000+ data.

2. I may akso want to collect age and gender of user from reddit to better improve our model. 

