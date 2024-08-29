import streamlit as st
import matplotlib.pyplot as plt
from predict_page import show_predict_page
from explore_page import Print, Plot, Univ_analysis

df = Print()
with st.sidebar:
    # Ask the user if they want to explore the data or run the model
    st.title("Do you want to explore the data or run the model?")
    action = st.radio("""Please, Choose""", ('','Explore Data', 'Predict Loan Approval'))
st.title("Welcome to Loan Approval System")
st.write("### This system leverages advanced data analysis and machine learning techniques to streamline and enhance the loan approval process, ensuring accurate, fair, and efficient decisions.")
if action == 'Explore Data':
    # Ask the user to input the number of rows to display
    num_rows = st.number_input("Enter the number of rows to display:", min_value=1, max_value=len(df), value=5)
    
    # Display the head of the DataFrame based on user input
    # st.write(f"### Showing the first {num_rows} row(s) of the DataFrame")
    st.write(df.head(num_rows))
    st.write(f"### Unique features in the the data")
    st.write(df.nunique())
    st.write(f"### Summary of the dataset")
    st.write(df.describe())
    Plot()
    Univ_analysis()

elif action == 'Predict Loan Approval':
    # For demonstration purposes, we'll just display a message
    #st.write("### Running the model...")
    # Insert your model code here
    # For example: model_output = my_model.predict(input_data)
    # st.write(model_output)
    show_predict_page()
    #st.write("Model has been run successfully!")
