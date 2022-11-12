import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


st.set_page_config(page_title="Dewi Media Lestari", page_icon=":chart_with_upwards_trend:", layout="wide")

with st.sidebar:
    st.markdown(" **Data Preparation** _is_ the process of preparing raw data so that it is suitable for further processing and analysis. Key steps include **cleaning, encoding, and scaling** the raw data into a form suitable for **_machine learning_** algorithms and then exploring and visualizing the data.")



@st.cache
def cleanData(data):
    df = data
    df = df.drop(['id', 'customers', 'year_order'], axis=1)

    #  fill in column dp if value null with 0
    df['down_payment'] = df['down_payment'].fillna(0)

    # change value column dp with 1 if value greater than 0
    df.loc[df['down_payment'] > 0 , 'down_payment'] = 1

    # change value column payment_type with 1 if value greater than 0
    df.loc[df['payment_type'] > 0 , 'payment_type'] = 1

    # remove row if data in column price equal to 0
    df.drop(df[df['price'] == 0].index, inplace=True)

    # fill column region with YOGYAKARTA if value is -
    df.loc[df['region'] == "-" , 'region'] = "YOGYAKARTA"

    # change column price data type
    df = df.astype({'down_payment': 'int64'})

    # drop duplicate data
    df = df.drop_duplicates()
                
    return df



@st.cache
def encodeData(data):
    df = pd.get_dummies(data)

    return df




@st.cache
def scaleData(data):
    scaler = StandardScaler()
    scaler.fit(data)
    scaled = pd.DataFrame(scaler.transform(data), columns=data.columns)

    return scaled




if 'dataFrame' not in st.session_state:
    st.subheader('Empty data')
    st.text("Please upload dataset at homepage")
else:
    with st.empty():
        df = st.session_state['dataFrame']
        cleanedData = cleanData(df)
        encodedData = encodeData(cleanedData)
    


    # Show data info
    nullValue = df.isna().values.sum()

    st.markdown("### Dataset Info")
    st.write(df)
    st.write("Total attributes:", df.shape[1])
    st.write("Total record:", len(df))
    # st.write("Total elements:", df.size)
    st.write("Total duplicate data:", df.duplicated(keep=False).sum())
    st.write("Total Null or NA values:", nullValue)
    # st.write("Attribute have Null or NA values:", df.isnull().any())


    # st.markdown("### Checking Null or NA Value")
    # nullValue = df.isna().values.sum()

    # st.write(df.isna())
    # st.write("The number of empty values (Null or NA) is:", nullValue)


    # Show categorical data
    st.markdown("### Categorical Attribute")
    s = (df.dtypes == "object")
    object_cols = list(s[s].index)
    st.write(df[object_cols].head(5))
    st.write("Total categorical attributes:", len(object_cols))

    


    # Clean data
    st.markdown("### 1. Data Cleaning")
    cleaned = st.button("Clean", help='Clean the dataset from Null and Na values')
        
    if cleaned:

        if 'cleanedData' not in st.session_state:
            st.session_state['cleanedData'] = cleanedData
    
    if 'cleanedData' in st.session_state:
        with st.expander("Cleaning result"):
            dfCleaned = st.session_state['cleanedData']
            st.write(dfCleaned)

            nullValue = dfCleaned.isna().values.sum()

            st.write("Total attributes:", dfCleaned.shape[1])
            st.write("Total record:", len(dfCleaned))
            # st.write("Total elements:", dfCleaned.size)
            st.write("Total duplicate data:", dfCleaned.duplicated(keep=False).sum())
            st.write("Null or NA values:", nullValue)




    # Encode data
    st.markdown("### 2. Data Encoding")
    convert = st.button("Encode", help='Clean the dataset from Null and Na values')

    if convert:
       if 'encodedData' not in st.session_state:
        st.session_state['encodedData'] = encodedData 
    
    if 'encodedData' in st.session_state:
        with st.expander("See result"):
            dfEncoded = st.session_state['encodedData']
            st.write(dfEncoded)
            st.write("Total attributes:", dfEncoded.shape[1])
            st.write("Total record:", len(dfEncoded))






    