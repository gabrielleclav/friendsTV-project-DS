# friendsTV-project-DS

## Background
Friends is a 90s sitcom, based in Manhattan, NYC, where six friends go through life experiences imaginable together, whether it was breakups, pregnancys, new jobs, love, and more. The six friends are: Phoebe Buffay, Chandler Bing, Rachel Green, Ross Geller, Monica Geller, and Joey Tribbiani, respectively.
![alt text](https://github.com/gabrielleclav/friendsTV-project-DS/blob/main/images/all-friends-color.jpg?raw=true)

I chose to do this project because I love the show Friends and I love NLP or anything that is AI related! I loved binge watching Friends when I was younger, so I decided to do an Natural Langauge Processing project using their dialogues.


## Problem Statement 
Through Natural Language Processing, people can give computers to understand text and spoken words. This project is aimed to read in the Friends dataset from Enmory NLP's repository (Character Mining) with the season, episode, character, and transcript columns, and build different models to see if each one can correctly determine a character's dialogue.


## Data Dictionary 

#### friends-modeling.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|season|*object*|friends-modeling.csv|corresponds to which season the line from each character came from 
|episode|*object*|friends-modeling.csv|the episode where the dialogue came from
|character|*object*|friends-modeling.csv|which character said the corresponding dialouge
|dialouge|*object*|friends-modeling.csv|what was said in that episode from the character

#### friends-modeling.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|season|*object*|friends-modeling.csv|corresponds to which season the line from each character came from 
|episode|*object*|friends-modeling.csv|the episode where the dialogue came from
|character|*object*|friends-modeling.csv|which character said the corresponding dialouge
|dialouge|*object*|friends-modeling.csv|what was said in that episode from the character

#### chandler-word-importance.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|index(word)|*object*|chandler-word-importance.csv|the word that had an important part in predictions 
|Chandler Bing|*object*|chandler-word-importance.csv|the score of the word for Chandler
|Joey Tribbiani|*object*|chandler-word-importance.csv|the score of the word for Joey
|Monica Geller|*object*|chandler-word-importance.csv|the score of the word for Monica
|Phoebe Buffay|*object*|chandler-word-importance.csv|the score of the word for Phoebe
|Rachel Green|*object*|chandler-word-importance.csv|the score of the word for Rachel
|Ross Geller|*object*|chandler-word-importance.csv|the score of the word for Ross

#### joey-word-importance.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|index(word)|*object*|joey-word-importance.csv|the word that had an important part in predictions 
|Chandler Bing|*object*|joey-word-importance.csv|the score of the word for Chandler
|Joey Tribbiani|*object*|joey-word-importance.csv|the score of the word for Joey
|Monica Geller|*object*|joey-word-importance.csv|the score of the word for Monica
|Phoebe Buffay|*object*|joey-word-importance.csv|the score of the word for Phoebe
|Rachel Green|*object*|joey-word-importance.csv|the score of the word for Rachel
|Ross Geller|*object*|joey-word-importance.csv|the score of the word for Ross

#### monica-word-importance.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|index(word)|*object*|monica-word-importance.csv|the word that had an important part in predictions 
|Chandler Bing|*object*|monica-word-importance.csv|the score of the word for Chandler
|Joey Tribbiani|*object*|monica-word-importance.csv|the score of the word for Joey
|Monica Geller|*object*|monica-word-importance.csv|the score of the word for Monica
|Phoebe Buffay|*object*|monica-word-importance.csv|the score of the word for Phoebe
|Rachel Green|*object*|monica-word-importance.csv|the score of the word for Rachel
|Ross Geller|*object*|monica-word-importance.csv|the score of the word for Ross

#### phoebe-word-importance.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|index(word)|*object*|phoebe-word-importance.csv|the word that had an important part in predictions 
|Chandler Bing|*object*|phoebe-word-importance.csv|the score of the word for Chandler
|Joey Tribbiani|*object*|phoebe-word-importance.csv|the score of the word for Joey
|Monica Geller|*object*|phoebe-word-importance.csv|the score of the word for Monica
|Phoebe Buffay|*object*|phoebe-word-importance.csv|the score of the word for Phoebe
|Rachel Green|*object*|phoebe-word-importance.csv|the score of the word for Rachel
|Ross Geller|*object*|phoebe-word-importance.csv|the score of the word for Ross

#### rachel-word-importance.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|index(word)|*object*|rachel-word-importance.csv|the word that had an important part in predictions 
|Chandler Bing|*object*|rachel-word-importance.csv|the score of the word for Chandler
|Joey Tribbiani|*object*|rachel-word-importance.csv|the score of the word for Joey
|Monica Geller|*object*|rachel-word-importance.csv|the score of the word for Monica
|Phoebe Buffay|*object*|rachel-word-importance.csv|the score of the word for Phoebe
|Rachel Green|*object*|rachel-word-importance.csv|the score of the word for Rachel
|Ross Geller|*object*|rachel-word-importance.csv|the score of the word for Ross

#### ross-word-importance.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|index(word)|*object*|ross-word-importance.csv|the word that had an important part in predictions 
|Chandler Bing|*object*|ross-word-importance.csv|the score of the word for Chandler
|Joey Tribbiani|*object*|ross-word-importance.csv|the score of the word for Joey
|Monica Geller|*object*|ross-word-importance.csv|the score of the word for Monica
|Phoebe Buffay|*object*|ross-word-importance.csv|the score of the word for Phoebe
|Rachel Green|*object*|ross-word-importance.csv|the score of the word for Rachel
|Ross Geller|*object*|ross-word-importance.csv|the score of the word for Ross

#### common-words.csv
|Feature|Type|Dataset|Description|
|---|---|---|---|
|word|*object*|common-words.csv|one of the top 50 most common words from the dataset
|count|*int*|common-words.csv|how many times the corresponding word appeared in the dialogue column from friends-modeling.csv


## Data Cleaning and EDA Process
In the dataset I found from [github](https://github.com/emorynlp/character-mining/tree/master/tsv), I used the season, episode, speaker, and the transcript. I made a dataframe that only contained the six main characters in the show: Joey, Chandler, Ross, Rachel, Phoebe, and Monica. I reanmed the columns to season, episode, character, and dialogue, then dropped the 15 columns that had null values in the dialogue column since they were not going to help and I did not know which lines they were supposed to be. I made two new columns for the word count and the length, and explored more with those two columns. I also graphed how many lines each character had throughout the whole show and for each season. I also looked at the max, min, avg, median, and standard deviation of the word count and lengths columns and graphed some of these. I looked that the top 50 most common words used in the dialogue and graphed those. I also looked at the sentiment values and explored more into that, and graphed the average per score for each character. 

From the EDA process, I noticed two major things. First of all, I did not expect Ross and Rachel to have the most lines and Phoebe has the least amount of lines. I also noticed that per season, usually rachel and ross are the top two or one of them are in the top two (expect for some seasons). From these, I expected my models to better predict Ross and Rachel and may have a difficult time predicting Phoebe unless it is something like 'smelly cat' or 'philange'.

**INORDER TO VIEW PLOTLY GRAPHS GO TO: [NBVIEWER](https://nbviewer.org/github/gabrielleclav/friendsTV-project-DS/blob/main/Code/data-eda/eda-1.ipynb)***


## Modeling Process
I coded five different models for the multiclass classification: Random Forest, K-Nearest Neighbors, Ada Boost, Näive Bayes, and Logistic Regression. Out of all these models, the Näive Bayes and Logistic Regression one were the best models. They scored the highest on the testing set and did well with predictions. Even though the ada boost did best with not overfitting the training set, it did one of the worst jobs at predicting (KNN was bad also). I chose to do a logistic regression model because I wanted to see which words had a major importance on predicting a certain character and give me insights on these words for each character. I also did a binary classification model for just Rachel and Ross and for Monica and Chandler. The accracy scores for the binary classification did significantly better than the multiclassification models, which is not surprising since it only has two classes to predict compared to six classes. 


## Streamlit App Process
I wanted to be able to display my work onto the web for people to go through it, especially if they do not know much about python and coding in general. Using the python library streamlit, I was able to make a web app for this project. I first started with a very general app, with just an intro, a make predictions page. Then I wanted to make it more interactive with the user and added an exploratory analysis page, and two make predictions pages that takes in some text from the user and prints out the model's prediction. In the final product, a user can watch some scenes from friends (from youtube), they can interact with the graphs (with some graphs, you can specify which graph you want to see or how many elements you want to see), and with the binary classification model, they can choose which couple they want the predictions to come from. I deployed my app using Heroku, so I had to set up a few files for this: requriements.txt, setup.sh, and Procfile. These files contain everything in order to run the app on Heroku. Within the setup.sh file, I added a theme section so I can customize the theme of the web application. You can visit this [web application](https://friends-tv-show.herokuapp.com/).


## Conclusion 
This project was a really fun project to do. I love natural langauge processing and machine learning, so I put both together for this project. I realized with the modeling process that it is definitely difficult to have perfect models, since predicting from a language is not the easiest. I also realized that modeling a multiclassification is difficult to work with and harder to get better results. Being said that, I learned a lot from this project and no matter how much I wanted my models to do better, it did better than the baseline model and I am happy with the final result. I hope you enjoy exploring this project and the web application!  