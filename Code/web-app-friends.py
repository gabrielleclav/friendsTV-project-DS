import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import pickle 
from graphing import bar_streamlit

#Function(s) for the web-app
    

def which_char(pred):
    '''
    Takes a prediction from one of the models and checks who it predicted. Then it outputs onto the screen.
    Argument: prediction
    '''
    if pred == 'Rachel Green':
        return 'Extraverted, energetic and playful like Rachel :)'
    elif pred == 'Joey Tribbiani':
        return 'Fun and spontaneous like Joey :D' 
    elif pred == 'Ross Geller':
        return 'Intellectual and shy like Ross :)'
    elif pred == 'Monica Geller':
        return 'VERY organized, and caring, and judging like Monica :)'
    elif pred == 'Phoebe Buffay':
        return 'Imaginative and original like Phoebe :D (make another song like Smelly Cat please)'
    #The last character is Chandler Bing
    return 'Sarcastic and innovative like Chandler :D' 
    
#Load in the dataset 
df = pd.read_csv("../Datasets/friends-modeling.csv")

#Start the code for the web-app

st.set_page_config(
    page_title='Who are you more like from the TV Show Friends :)',
    page_icon= '🛋', #command control space
    initial_sidebar_state = 'expanded'
)

#will show up in all the pages because it is run before the individual pages
st.title('''
        The One with Natural Language Processing
        ***
        ''')


#Adding a selct box -- making individual pages 
page = st.sidebar.selectbox(
    'Select a page:',
    ('About Friends',
    'About This Project',
    'Exploratory Analysis', 
    'Making a Prediction: All Characters')
)

#Individual pages 

#About Friends
if page == 'About Friends':
    #Contents of the about page
    st.write()
    st.subheader('About Friends :D')

    #Image with credits 
    st.image('../images/fountain.jpg',width=700)
    st.caption('Credit to Google Images')


    st.write(""" 
            ***
            """)

    st.write()

    st.write("""
    ### Summary of the Show:
    Friends is a 90s sitcom, based in Manhattan, NYC, where six friends go through life experiences 
    imaginable together, whether it was breakups, pregnancys, new jobs, love, and more. The six friends are:
    Phoebe Buffay, Chandler Bing, Rachel Green, Ross Geller, Monica Geller,  and Joey Tribbiani, respectively. 
    
    """)

    st.image('../images/all-friends-color.jpg')

    st.caption('Credit to Google Images')

    st.write(""" 
            ***
            """)

    #line break 
    st.write()

    option = st.radio('Who is your favorite character?',
                  ['Joey',
                   'Rachel',
                   'Ross',
                   'Phoebe', 
                   'Monica', 
                   'Chandler'])

    

#About the Project
elif page == 'About This Project':
    st.write("""
    #### Intro: 
    I chose to do this project because I 
    love the show Friends and I love NLP or 
    anything that is AI related! I loved binge watching Friends when I 
    was younger, so I decided to do an Natural Langauge Processing project using 
    their dialogues. I found a dataset with their transcripts in it. I was originally 
    web-scraping a website for it, and will definitely still work on it since there are 
    a bunch of different HTML tags used, making it a little bit more challenging.
    

    P.S. I have the Central Perk lego set 😀 
    *** 
    """)
    st.write(""" 
    #### Problem Statement:
    Through Natural Language Processing, people can give computers to understand text and spoken words. 
    This project is aimed to read in the Friends dataset from Enmory NLP's repository (Character Mining) with 
    the season, episode, character, and transcript columns, and build different models to see if each one can 
    correctly determine a character's dialogue.
    
    """)




elif page == 'Exploratory Analysis':
    st.subheader('EDA')
    st.write()

    st.write('''
            There was a lot of EDA and data cleaning. I will be showing some EDA I have done in this project! 
            I hope you enjoy. Note: you can hover over the graph to give you details about it! \n
            \n
            ''')

    st.write() 

    #colors = ['royalblue' if i == max(df['character'].value_counts()) else 'slategray' for i in df['character'].value_counts()]
    st.plotly_chart(bar_streamlit(data = df['character'].value_counts().sort_values(ascending=False),
             color = df['character'].value_counts().sort_values(ascending=False).index,
             graph_title = "Number of Times Characters Have Appeared"))

    st.write("""
        In this graph, it is displaying how many times each character had said something throughout the whole season. 

        ***
            """)
    
    #For another graph showing per season 
    st.write('''
            #### Which season do you want to see which character has the most lines?
            ''')

    #Giving the user an option to see any season they want 
    opt_s = st.selectbox('Select a Season:',['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08', 's09', 's10'])

    #Doing a little groupby to show the seasons
    by_season = df.groupby('season')['character'].value_counts()

    #Plotting and display
    st.plotly_chart(bar_streamlit(data = by_season[opt_s],
                                color = by_season[opt_s].index,
                                graph_title = f"Count of lines in Season {opt_s} per Character"
                                )
    )
    st.write('''
            These set of graphs are just the show the amount of lines each character had each season.
            
             *** 
             ''')
        

#Making a character Prediction 
elif page == 'Making a Prediction: All Characters':
    #Contents of the Make a Prediction page
    st.subheader('Which Character are you like?')

    #Adding an image for decoration 
    st.image('../images/all-shakes.jpg', width=700)
    st.caption('Credit to Google Images')
    st.write(' *** ')

    #Open up the two models 
    with open('logistic-regression.pkl', mode ='rb') as pickle_in:
        gs_l = pickle.load(pickle_in)
    
    with open('ada-boost.pkl', mode ='rb') as pickle_in_1:
        gs_a = pickle.load(pickle_in_1)
    

    #Get input from user 
    #Add default prediction less confusing
    user_text = st.text_input(
        'Please enter some text: ', 
        value='Pivot, pivot, PIVOT!',
        )

    #Make the predictions
    pred_l = gs_l.predict([user_text])[0]
    pred_a = gs_a.predict([user_text])[0]

    #Pass into the function 
    answer_l = which_char(pred_l)
    answer_a = which_char(pred_a)

    #use st.write to write a message out to the user 
    st.write('From logistic regression: ', answer_l)
    st.write()
    st.write('From ada boost: ', answer_a)
    st.write()
    st.write(''' *** ''')

