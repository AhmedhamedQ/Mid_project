import pandas as pd
import streamlit as st
import plotly.express as px 
import plotly.figure_factory as ff

st.set_page_config(layout='wide' , page_icon='🏙️' , page_title='Real state')


st.markdown('<h1 style="text-align: center; color : Yellow;">charts page</h1>', unsafe_allow_html=True)
df = pd.read_csv('real_state.csv')

tab1 , tab2 = st.tabs(['Nomerical' , 'Catigorical'])

with tab1 :
    col , col1,col2 = st.columns([4,1,4])
    with col :
        st.subheader('Data describtev')
        st.dataframe(df.describe())
    with col2 :
        st.subheader('Coorlition between columns')
        st.plotly_chart(px.imshow(df[['bed','bath','house_size','price']].corr()) , use_container_width=True)
    st.plotly_chart(px.scatter(df , x = 'bath' , y = 'bed' , color='house_size' , ) , use_container_width=True)
    
    col3 , col4 , col5 = st.columns([2,0.5,2])
    with col3 :
        
        st.subheader('Count plot for bedrooms ')  
        st.plotly_chart(px.histogram(df, x = 'bed' ,color_discrete_sequence=px.colors.qualitative.Alphabet ) , use_container_width=True)
    with col5 :
        st.subheader('Count plot for bathrooms ')
        st.plotly_chart(px.histogram(df , x='bath' ,color_discrete_sequence=px.colors.qualitative.Bold) , use_container_width=True)  

        
        
with tab2 :
    st.subheader('Count plot for cities')
    st.plotly_chart(px.histogram(df, x = 'city' ,color = 'state' , color_discrete_sequence=px.colors.qualitative.Antique ) , use_container_width=True)
    st.subheader('Count plot for states')
    st.plotly_chart(px.histogram(df , x = 'state'))
