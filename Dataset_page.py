import pandas as pd
import streamlit as st

st.set_page_config(layout='wide' , page_icon='🏙️' , page_title='Real state')

df = pd.read_csv('real_state.csv')
tab1 , tab2 = st.tabs(['Dataset' , 'Dataset filter'])
with tab1 :
    st.markdown('<h1 style="text-align: center; color : red;">Dataset page</h1>', unsafe_allow_html=True)
    col1 , col2 , col3 = st.columns([1,4,1])
    with col2 :
        st.dataframe(df)
with tab2 :
    st.markdown('<h1 style="text-align: center; color : red;">Filtering data as you want</h1>', unsafe_allow_html=True)
    filter_ = st.selectbox('Select type of filter' , ['Price' ,'Count of bedrooms and bathrooms' , 'State and city', 'Price & count of bed and bath'])
    if filter_ == 'Price' :
        amount_min = st.selectbox('Select your minimum amount', [1000 , 100000 , 200000 , 300000 , 400000,500000,600000,700000,800000,900000,100000])
        amount_max = st.selectbox('Select your maximum amount' , [100000 , 200000 , 300000 , 400000,500000,600000,700000,800000,900000,100000 , 1200000])
        col11 , col22 , col33 = st.columns([1,4,1])
        with col22:
            num = df[df['price']>amount_min][df['price']<amount_max+1].shape[0]
            st.write(f'available: {num}')
            st.dataframe(df[df['price']>amount_min][df['price']<amount_max+1])
    elif filter_ =='Count of bedrooms and bathrooms' :
        count_bed = st.selectbox('Select count of bedrooms' , [2,3,4,5])
        count_bath = st.selectbox('Select count of bathrooms' , [1,2,3,4])
        col12 , col13 , col14 = st.columns([1,4,1])
        with col13:
            num = df[df['bed']==count_bed][df['bath']==count_bath].shape[0]
            st.write(f'available : {num}')
            st.dataframe(df[df['bed']==count_bed][df['bath']==count_bath])
    elif filter_ == 'State and city' :
        s = [i for i in df['state'].unique()]
        state = st.selectbox('Select state name :' , s)
        c = [i for i in df[df['state']==state]['city'].unique()]
        city = st.selectbox('select city name :' , c  )
        col12 , col13 , col14 = st.columns([1,4,1])
        with col13:
            num = df[df['state']==state][df['city']==city].shape[0]
            st.write(f'available : {num}')
            st.dataframe(df[df['state']==state][df['city']==city])
    else :
        col1 , col2 , col3 = st.columns([1,1,1])
        with col1 :
            amount_min = st.selectbox('Select your minimum amount', [1000 , 100000 , 200000 , 300000 , 400000,500000,600000,700000,800000,900000,100000])
        with col2 :    
            amount_max = st.selectbox('Select your maximum amount' , [100000 , 200000 , 300000 , 400000,500000,600000,700000,800000,900000,100000 , 1200000])
        with col3 :
            count_bed = st.selectbox('Select count of bedrooms' , [2,3,4,5])
        
        col12 , col13 , col14 = st.columns([2,0.2,3])
        with col12 :
            count_bath = st.selectbox('Select count of bathrooms' , [1,2,3,4])
        with col14:
            num = df[df['price']>amount_min][df['price']<amount_max+1][df['bed']==count_bed][df['bath']==count_bath].shape[0]
            st.write(f'available : {num}')
            st.dataframe(df[df['price']>amount_min][df['price']<amount_max+1][df['bed']==count_bed][df['bath']==count_bath])
        
