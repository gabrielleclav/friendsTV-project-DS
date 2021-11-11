import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st
import pickle 

st.set_page_config(
    page_title='Who are you more like from the TV Show Friends :)',
    page_icon= '🛋', #command control space
    initial_sidebar_state = 'expanded'
)

#will show up in all the pages because it is run before the individual pages
st.title('Movie Ratings: Was It Positive or Negative')


#Adding a selct box -- making individual pages 
page = st.sidebar.selectbox(
    'Select a page:',
    ('About', 
     'Making a Prediction: Random Forest', 
    'Making a Prediction: K-Nerest Neighbors',
    'Making a Prediction: Logistic Regression',
    'Making a Prediction: Näive Bayes',
    'Making a Prediction: Ada Boost')
)
#Individual pages 
if page == 'About':
    #Contents of the about page
    st.subheader('About this Project')
    st.write('This project is aimed to making a prediction if the rating from a person was positive or negative.')

elif page == 'Making a Prediction':
    #Contents of the Make a Prediction page
    st.subheader('You Can Make a Prediction!')
    with open('reviews.pkl', mode ='rb') as pickle_in:
        gs = pickle.load(pickle_in)

    #Get input from user 
    #Add default prediction less confusing
    user_text = st.text_input(
        'Please enter some text: ', 
        value='Wow, you really did not like the movie :o',
        )

    #Make the prediction 
    prediction = gs.predict([user_text])[0]

    #use st.write to write a message out to the user 
    if prediction == 'negative':
        st.write(f"Wow, you really did not like the movie :o")
    else:
        st.write(f"The movie must be great! Thank you for the positive review :) ")
