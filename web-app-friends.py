import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px
import streamlit as st
import pickle 
from Code.graphing import bar_streamlit


#Function(s) for the web-app ---------------------------------------------------------------------
    

def which_char(pred, couple_ed):
    '''
    Takes a prediction from one of the models and checks who it predicted. It checks to see if 
    the prediction if from the couples page(True) or the character page(False), since there will 
    be different strings returned. Then it outputs onto the screen.
    Argument: prediction, couple_ed 
    '''
    if pred == 'Rachel Green':
        if couple_ed == False:
            return 'Extraverted, energetic and playful like Rachel :)'
        return 'Like Rachel'

    elif pred == 'Joey Tribbiani':
        return 'Fun and spontaneous like Joey :D' 

    elif pred == 'Ross Geller':
        if couple_ed == False:
            return 'Intellectual and shy like Ross :)'
        return 'Like Ross'

    elif pred == 'Monica Geller':
        if couple_ed == False:
            return 'VERY organized, and caring, and judging like Monica :)'
        return 'Like Monica'

    elif pred == 'Phoebe Buffay':
        return 'Imaginative and original like Phoebe :D (make another song like Smelly Cat please)'

    #The last character is Chandler Bing
    if couple_ed == False:
        return 'Sarcastic and innovative like Chandler :D' 
    return 'Like Chandler'
     
    
#Load in the dataset -------------------------------------------------------------
friends = pd.read_csv("Datasets/friends-modeling.csv")
common_words = pd.read_csv('Datasets/common-words.csv')
phoebe = pd.read_csv('Datasets/phoebe-word-importance.csv')
joey = pd.read_csv('Datasets/joey-word-importance.csv')
ross = pd.read_csv('Datasets/ross-word-importance.csv')
rachel = pd.read_csv('Datasets/rachel-word-importance.csv')
chan = pd.read_csv('Datasets/chandler-word-importance.csv')
monica = pd.read_csv('Datasets/monica-word-importance.csv')


#Start the code for the web-app -----------------------------------------------------

st.set_page_config(
    page_title='NLP: Friends TV Project :)',
    page_icon= '🛋', #command control space
    initial_sidebar_state = 'auto',
    #layout= 'wide'
)

#will show up in all the pages because it is run before the individual pages
st.title('''
        The One with Natural Language Processing
        ***
        ''')


#Adding a selct box -- making individual pages -----------------------------------------------------
page = st.sidebar.selectbox(
    'Select a page:',
    ('About Friends',
    'About This Project',
    'Exploratory Analysis', 
    'Making a Prediction: All Characters',
    'Making a Prediction: Couples Edition')
)

#Individual pages 

#About Friends -----------------------------------------------------------------
if page == 'About Friends':
    #Contents of the about page
    st.write()
    st.subheader('About Friends 🛋️')

    #Image with credits 
    st.image('images/fountain.jpg',width=700)
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

    st.image('images/all-friends-color.jpg')

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

    #Writing something with their favorite Character
    st.write('Hmm.. Are you like ', option, '?')


    st.write(""" 
    ***

    #### Some Funny Friends Scenes
    In my opinion, these are my favorite Friends scences and wanted to share!

    """)

    st.video('https://www.youtube.com/watch?v=8w3wmQAMoxQ')

    st.video('https://www.youtube.com/watch?v=gyKmICnNRhs')

    st.video('https://www.youtube.com/watch?v=t68chqjlDC8')

    st.video('https://www.youtube.com/watch?v=N_X9fPauWfI')

    

#About the Project ------------------------------------------------------------------------
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
    Here is the github repository: [github](https://github.com/gabrielleclav/friendsTV-project-DS)
    

    P.S. I have the Central Perk lego set 😀 
    *** 
    """)
    st.write(""" 
    #### Problem Statement:
    Through Natural Language Processing, people can give computers to understand text and spoken words. 
    This project is aimed to read in the Friends dataset from Enmory NLP's repository (Character Mining) with 
    the season, episode, character, and transcript columns, and build different models to see if each one can 
    correctly determine a character's dialogue.
    
    ***
    """)

    st.write("""
    #### Modeling:

    I coded five different models for the multiclass classification: Random Forest, K-Nearest Neighbors, Ada Boost, Näive
    Bayes, and Logistic Regression. Out of all these models, the Logistic Regression one was the best model. It scored the highest 
    on the testing set and did well with predictions. Even though the ada boost did best with not overfitting the training set, it 
    did one of the worst jobs at predicting (KNN was bad also). In the Make a Prediction: All Characters page, it will make predictions
    from the logistic regression model and the ada boost model to display the differences in the models. As for the 
    Make a Predictions: Couples Edition page, I only display predictions from a logistic regression model. 
    Note: Obviously, these models are not perfect, and do not always make the right predictions, however, they do make a lot 
    of correct predictions. 
    
    """)


#EDA page ------------------------------------------------------------------------------------------
elif page == 'Exploratory Analysis':
    st.subheader('EDA')
    st.write()

    st.write('''
            There was a lot of EDA and data cleaning. I will be showing some EDA I have done in this project! 
            I hope you enjoy. Note: you can hover over the graph to give you details about it! \n
            \n
            ''')

    st.write() 

    
    st.plotly_chart(bar_streamlit(data = friends['character'].value_counts().sort_values(ascending=False),
             color = friends['character'].value_counts().sort_values(ascending=False).index,
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
    opt_s = st.selectbox('Select a Season:',['s01', 's02', 's03', 's04', 
    's05', 's06', 's07', 's08', 's09', 's10'])

    #Doing a little groupby to show the seasons
    by_season = friends.groupby('season')['character'].value_counts()

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

    #Doing a most common words used amongst all the characters in a graph 
    res = num = st.slider("Select how many results you want to see: ", 5,50)

    st.plotly_chart(bar_streamlit(data = common_words.head(res),
              x= common_words['word'].head(res),
              y= common_words['count'].head(res),
              color = common_words['count'].head(res),
             graph_title = f'Top {res} Most Common Words',
             x_axis_title = 'Common Words'))
    
    #Displaying all the word importance dataframes on the page 
    st.write('''
    This graphs displays the most common words starting at the top 4 to the top 50! 

    ***
    #### Word Importance

    When I did the logistic modeling, I checked the coefficients of the each character class for all the words that were
    in the datasets. Here are some tables showing the coefficients for each character. 

    ''')
    opt_char = st.selectbox('Select a Season:',['Phoebe', 'Joey', 'Rachel', 'Ross', 
    'Monica', 'Chandler'])

    if opt_char == 'Phoebe':
        #Phoebe's dataframe
        st.dataframe(phoebe.set_index('Unnamed: 0').head(10))

    elif opt_char == 'Joey':
        #Joey's dataframe
        st.dataframe(joey.set_index('Unnamed: 0').head(10))
    elif opt_char == 'Rachel':
        #Rachel's dataframe
        st.dataframe(rachel.set_index('Unnamed: 0').head(10))
    elif opt_char == 'Ross':
        #Ross' dataframe
        st.dataframe(ross.set_index('Unnamed: 0').head(10))
    elif opt_char == 'Monica':
        #Monica's dataframe
        st.dataframe(monica.set_index('Unnamed: 0').head(10))
    else:
        #Chandler's daatframe
        st.dataframe(chan.set_index('Unnamed: 0').head(10))




#Making a character Prediction ------------------------------------------------------------------------------
elif page == 'Making a Prediction: All Characters':
    #Contents of the Make a Prediction page
    st.subheader('Which Character are you like?')

    #Adding an image for decoration 
    st.image('images/all-shakes.jpg', width=700)
    st.caption('Credit to Google Images')
    st.write(' *** ')

    #Open up the two models 
    with open('Code/logistic-regression.pkl', mode ='rb') as pickle_in:
        gs_l = pickle.load(pickle_in)
    
    with open('Code/ada-boost.pkl', mode ='rb') as pickle_in_1:
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
    answer_l = which_char(pred_l, False)
    answer_a = which_char(pred_a, False)

    #use st.write to write a message out to the user 
    st.write('From logistic regression: ', answer_l)
    st.write()
    st.write('From ada boost: ', answer_a)
    st.write()
    st.write(''' *** ''')



#Making a character Prediction  ---------------------------------------------------------------------
elif page == 'Making a Prediction: Couples Edition':
    #Contents of the Make a Prediction page
    st.subheader('Who are you like in a relationship?')

    #Adding an image for decoration 
    st.image('images/monica-and-chandler.jpg', width=700)
    #st.caption('Credit to Google Images')
    st.write(' *** ')

    #Open up the two models -- the Ross and Rachel and the Monica and Chandler
    with open('Code/log-reg-rachross.pkl', mode ='rb') as pickle_in:
        gs_rr = pickle.load(pickle_in)
    
    with open('Code/log-reg-monchan.pkl', mode ='rb') as pickle_in_1:
        gs_cm = pickle.load(pickle_in_1)
    

    #Get input from user 
    #Add default prediction less confusing
    
    opt_couple = st.radio('Choose a couple: ',
                  ['Rachel and Ross',
                   'Monica and Chandler', ])

    user_text = st.text_input(
        'Please enter some text: ', 
        value='We were on a break!',
        )

    #Make the predictions
    if opt_couple == 'Rachel and Ross':
        preds = gs_rr.predict([user_text])[0]
    else:
        preds = gs_cm.predict([user_text])[0]

    #Pass into the function 
    result = which_char(preds, True)
    #answer_cm = which_char(pred_cm, True)

    #use st.write to write a message out to the user 
    st.write('You are like ', result, 'in a relationship.')
    st.write()
    #st.write('Monica or Chandler? ', answer_cm)
    st.write()
    st.write(''' *** ''')

