import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Title and texts
st.title("Retail Business Dashboard")
st.subheader("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")

#Entering monthly sales box
age = st.number_input("Enter Monthly Sales Target(in USD):",
                      min_value=0,
                      max_value=50000,
                      value=25


#selection box for choosing region 
option = st.selectbox("Select Region:",
                      ["North", "South", "West"])

#submit bottom 
if st.button("Submit"):
    st.write("Button clicked!")
