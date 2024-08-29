import streamlit as st
#import matplotlib as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def Print():
    df = pd.read_csv("loan_approval_dataset.csv")
    pd.set_option('display.max_columns',None)#print all the columns
    # view first few rows of the dataset
    #st.write("### Head of the DataFrame")
    #st.write(df.head())
    return df
def Plot():
    #outlier detection
    df = Print()
    # Remove all whitespaces from column names
    df.columns = df.columns.str.replace(' ', '')
    # Plotting box plots for all numerical variables
    st.write("### Box Plots for All Numerical Variables")

    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        st.write(f"#### Box Plot of {column}")
    
    # Create a figure
        fig, ax = plt.subplots()
    
    # Create the box plot
        sns.boxplot(df[column], ax=ax)
    
    # Display the plot in Streamlit
        st.pyplot(fig)

def Univ_analysis(): 
    df = Print()   
        # Plotting univariate analysis for all categorical variables
    st.write("### Univariate Analysis for Categorical Variables")

    for column in df.select_dtypes(include=['object', 'category']).columns:
        st.write(f"#### Bar Chart of {column}")
        
        # Create a figure
        fig, ax = plt.subplots()
        
        # Create the bar plot
        sns.countplot(x=df[column], ax=ax)
        
        # Rotate x labels for better readability if there are many categories
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        
        # Display the plot in Streamlit
        st.pyplot(fig)