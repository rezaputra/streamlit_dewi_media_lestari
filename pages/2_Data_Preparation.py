import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


st.set_page_config(page_title="Dewi Media Lestari", page_icon=":chart_with_upwards_trend:", layout="wide")




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




@st.cache
def downloadDf(data):
    csv = data.to_csv().encode('utf-8')

    return csv





if 'dataFrame' not in st.session_state:
    st.subheader('Empty data')
    st.text("Please upload dataset at homepage")
else:
    # Initialization
    with st.empty():
        df = st.session_state['dataFrame']
        cleanedData = cleanData(df)
        encodedData = encodeData(cleanedData)
        scaledData = scaleData(encodedData)
        fileCsv = downloadDf(scaledData)
        perc = [0.20, 0.40, 0.60, 0.80]
        inc = ['object', 'float', 'int']
    


    with st.sidebar:
        st.markdown(" **Data Preparation** _is_ the process of preparing raw data so that it is suitable for further processing and analysis. Key steps include **cleaning, encoding, and scaling** the raw data into a form suitable for **_machine learning_** algorithms and then exploring and visualizing the data.")




    # Show data frame description
    st.markdown("#### Dataset Description")
    st.caption("A data set (or dataset) is a collection of data. In the case of tabular data, a data set corresponds to one or more database tables, where every column of a table represents a particular variable, and each row corresponds to a given record of the data set in question. The data set lists values for each of the variables, such as for example height and weight of an object, for each member of the data set. Data sets can also consist of a collection of documents or files (Snijders C et al, 2012).")
    
    tabDataInfo,tabDataCategorical,tabDataDetail = st.tabs(['🗃 Dataset', '🔠 Categorical Attributes', 'ℹ Details'])
        
    with tabDataInfo:
        st.write(df)

    with tabDataCategorical:
        colCat1, colCat2 = st.columns([3,1])
        with colCat1:
            s = (df.dtypes == "object")
            object_cols = list(s[s].index)
            st.write(df[object_cols])
        with colCat2:
            st.markdown("##### Meaning")
            st.caption('An attribute where the values correspond to discrete categories. For example, state is a categorical attribute with discrete values (CA, NY, MA, etc.). Categorical attributes are either non-ordered (nominal) like state, gender, etc., or ordered (ordinal) such as high, medium, or low temperatures.')

    with tabDataDetail:
        colDetailDf1, colDetailDf2 = st.columns([3,1])
        with colDetailDf1:            
            st.write(df.describe(percentiles = perc, include = inc))
        with colDetailDf2:
            st.markdown("##### Description")
            st.caption("Statistical description of dataframe was returned with the respective passed percentiles. For the columns with strings, NaN was returned for numeric operations.")
            st.write("Total attributes:", df.shape[1])
            st.write("Total record:", len(df))
            st.write("Total elements:", df.size)
            st.write("Total duplicate:", df.duplicated(keep=False).sum())
            nullValue = df.isnull().values.sum()
            st.write("Total Null or NA values:", nullValue)
            # st.write("Attribute have Null or NA values:", df.isnull().any())
            st.write("Total categorical attributes:", len(object_cols))



    # st.markdown("### Checking Null or NA Value")
    # nullValue = df.isna().values.sum()

    # st.write(df.isna())
    # st.write("The number of empty values (Null or NA) is:", nullValue)


    # Show categorical data
    
    


    # Clean data
    st.markdown("#### Step 1 Data Cleaning")
    clean = st.button("Clean", help='Clean the dataset from Null and Na values')
        
    if clean:

        if 'cleanedData' not in st.session_state:
            st.session_state['cleanedData'] = cleanedData
    
    if 'cleanedData' in st.session_state:
        with st.expander("Cleaning result"):
            tabCleanResult, TabCleanDetail = st.tabs(['🗃 Result', 'ℹ Details'])

            with tabCleanResult:
                dfCleaned = st.session_state['cleanedData']
                st.write(dfCleaned)

            with TabCleanDetail:
                colCleanDetails1, colCleanDetails2 = st.columns([3,1])
                with colCleanDetails1:
                    st.write(dfCleaned.describe(percentiles = perc, include = inc))

                with colCleanDetails2:
                    st.markdown("##### Recaps")
                    nullValue = dfCleaned.isna().values.sum()
                    st.write("Total attributes:", dfCleaned.shape[1])
                    st.write("Total record:", len(dfCleaned))
                    st.write("Total elements:", dfCleaned.size)
                    st.write("Total duplicate data:", dfCleaned.duplicated(keep=False).sum())
                    st.write("Total Null or NA values:", nullValue)




    # Encode data
    st.markdown("#### Step 2 Data Encoding")
    convert = st.button("Encode", help='Encode data from categorical values')

    if 'cleanedData' in st.session_state and convert:
       if 'encodedData' not in st.session_state:
        st.session_state['encodedData'] = encodedData
    
    if 'encodedData' in st.session_state:
        with st.expander("Encoding result"):
            tabEncodeResult, tabEncodeDetails = st.tabs(['🗃 Result', 'ℹ Details'])
            with tabEncodeResult:        
                dfEncoded = st.session_state['encodedData']
                st.write(dfEncoded)
            with tabEncodeDetails:
                colEncodeDetails1, colEncodeDetails2 = st.columns([3,1])
                with colEncodeDetails1:
                    st.write(dfEncoded.describe(percentiles = perc, include = inc))
                with colEncodeDetails2:
                    st.markdown("##### Recaps")
                    st.write("Total attributes:", dfEncoded.shape[1])
                    st.write("Total record:", len(dfEncoded))
                    st.write("Total elements:", dfEncoded.size)




    
    # Scale Data
    st.markdown("#### Step 3 Data Scaling")
    scale = st.button("Scale", help='Scale data frame till standard deviation equal 1')

    if 'cleanedData' in st.session_state and 'encodedData' in st.session_state and scale:
       if 'scaledData' not in st.session_state:
        st.session_state['scaledData'] = scaledData 
    
    if 'scaledData' in st.session_state:
        with st.expander("Scaling result"):
            tabScaleResult, tabScaleDetails = st.tabs(['🗃 Result', 'ℹ Details'])
            with tabScaleResult:
                dfScaled = st.session_state['scaledData']
                st.write(dfScaled)
            with tabScaleDetails:
                colScaleDetails1, colScaleDetails2 = st.columns([3,1])
                with colScaleDetails1:
                    st.write(dfScaled.describe(percentiles = perc, include = inc))
                with colScaleDetails2:
                    st.markdown("##### Recaps")
                    st.write("Total attributes:", dfScaled.shape[1])
                    st.write("Total record:", len(dfScaled))
                    st.write("Total elements:", dfScaled.size)

                    st.download_button(
                        label="Download data as CSV",
                        data=fileCsv,
                        file_name='ready_df.csv',
                        mime='text/csv'
                    )






    