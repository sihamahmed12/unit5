import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
title = st.title("Siham's Dashboard")
Data = pd.read_csvs("supermarket.csv")

st.supheader("Lowest 5 performing areas") 
Data.sort_values(["store_area"], 
axis=0,
ascending=[True], 
inplace = True)
st.dataframe(Data[["store_id","store_area"]].head(n=5))


st.supheader("Top 10 performing stores") 
Data.sort_values(["store_area"], 
axis=0,
ascending=[False], 
inplace = True)
st.dataframe(Data[["store_id","store_area"]].head(n=10))