'''
This Python Script is for making graphs for EDA and the Modeling Sections different libraries-- focusing mainly on plotly. 
Other libraries used will be matplotlib.pyplot and seaborn. 

By: Gabrielle Clavell

'''

#import the libraries needed 
import numpy as np 
import pandas as pd 

#graphing libraries 
import matplotlib.pyplot as plt
import plotly.express as px


def plotly_bar(data, color, graph_title, x_axis_title='Character', y_axis_title='Count', x=None, y=None):
    '''
    This function is to plot a bar graph using plotly.express bar function. 
    Arguments: data, color, graph_title, x_axis_title, y_axis_title
    It uses px.bar(data, color) and then uses .update_layout to modify the titles then 
    displays the graph.
    '''
    fig = px.bar(data_frame=data, color=color, x=x, y=y)
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


#For streamlit graphs
def bar_streamlit(data, color, graph_title, x_axis_title='Character', y_axis_title='Count', x=None, y=None):
    '''
    This function is to plot a bar graph using plotly.express bar function ONLY for Streamlit use. 
    Arguments: data, color, graph_title, x_axis_title, y_axis_title
    It uses px.bar(data, color) and then uses .update_layout to modify the titles then 
    returns the figure so it can be then plotted by Streamlit. This does not take x and y -- be careful!
    '''
    fig = px.bar(data_frame=data, color=color, x=x, y=y)
    fig.update_layout(
        title= graph_title,
        xaxis_title= x_axis_title,
        yaxis_title= y_axis_title,
        legend_title="color",
        font=dict(
            family="Times New Roman, monospace",
            size=14,
            color="palevioletred"
    ))
    return fig 


    
    
