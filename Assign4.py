import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
st.title("Students Performance")
st.header("Education")
st.text("Dataset")
st.set_option('deprecation.showPyplotGlobalUse', False)
data=pd.read_csv('/home/gopika/Dataset.csv')
st.dataframe(data)
st.header("math score of female students")
math=data[['Math score','gender']]
result = math.loc[math['gender'] == 'female']
st.dataframe(result)
st.subheader("Displot")
sns.displot(data)
st.pyplot()
st.subheader("Jointplot")
sns.jointplot(x='reading score',y='writing score',data=data,kind='hex')
st.pyplot()
st.balloons()
