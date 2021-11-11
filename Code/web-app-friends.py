import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
#import plotly.express as px
import streamlit as st
import pickle 

#Functions for the web-app

def plotly_bar(data, color, graph_title, x_axis_title='Character', y_axis_title='Count'):
    '''
    This function is to plot a bar graph using plotly.express bar function. 
    Arguments: data, color, graph_title, x_axis_title, y_axis_title
    It uses px.bar(data, color) and then uses .update_layout to modify the titles then 
    displays the graph. This does not take x and y -- be careful!
    '''
    fig = px.bar(data_frame=data, color=color)
    fig.update_layout(
        title= graph_title,
        xaxis_title= x_axis_title,
        yaxis_title= y_axis_title,
        legend_title="color",
        font=dict(
            family="Times New Roman, monospace",
            size=14,
            color="RebeccaPurple"
    ))
    fig.show()

def which_char(pred):
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
    


#Start the code for the web-app

st.set_page_config(
    page_title='Who are you more like from the TV Show Friends :)',
    page_icon= '🛋', #command control space
    initial_sidebar_state = 'expanded'
)

#will show up in all the pages because it is run before the individual pages
st.title('Friends, The TV Show')


#Adding a selct box -- making individual pages 
page = st.sidebar.selectbox(
    'Select a page:',
    ('About Friends',
    'About This Project', 
    'Making a Prediction: All Characters')
)
#Load in the dataset 
df = pd.read_csv("../Datasets/friends-modeling.csv")
#Individual pages 

#About Friends
if page == 'About Friends':
    #Contents of the about page
    st.write()
    st.subheader('About Friends :D')

    #Image with credits 
    st.image('../images/fountain.jpg',width=700)
    st.write('Credit to Google Images')

    st.write()
    st.write("""
    ### Summary of the Show:
    Friends is a 90s sitcom, based in Manhattan, NYC, where six friends go through life experiences 
    imaginable together, whether it was breakups, pregnancys, new jobs, love, and more. The six friends are:
    Rachel Green, Monica Geller, Phoebe Buffay, Chandler Bing, Joey Tribbiani, and Ross Geller. 
    
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
    st.write("""I chose to do this project because I 
    love the show Friends and I love NLP or 
    anything that is AI related!
    """)

    st.write(gh.plotly_bar(data = df['character'].value_counts().sort_values(ascending=False),
             color = df['character'].value_counts().sort_values(ascending=False).index,
             graph_title = "Number of Times Characters Have Appeared"))


#Making a character Prediction 
elif page == 'Making a Prediction: All Characters':
    #Contents of the Make a Prediction page
    st.subheader('Which Character are you like?')

    #Open up the two models 
    with open('logistic-regression.pkl', mode ='rb') as pickle_in:
        gs_l = pickle.load(pickle_in)
    
    with open('ada-boost.pkl', mode ='rb') as pickle_in_1:
        gs_a = pickle.load(pickle_in_1)
    

    #Get input from user 
    #Add default prediction less confusing
    user_text = st.text_input(
        'Please enter some text: ', 
        value='Pivot, pivot, PIVOT!' ,
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

