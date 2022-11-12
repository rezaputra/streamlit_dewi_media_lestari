# Import library
import pandas as pd
import streamlit as st


# Set page info
st.set_page_config(page_title="Dewi Media Lestari", page_icon=":chart_with_upwards_trend:", layout="wide")

# Header and subheader
st.header("Welcome Dewi Media Lestari")
st.subheader("One Step Solution for You Promotional Needs")


# Upload dataset csv only
st.text("Please input your dataset below:")
uploaded_file = st.file_uploader("Choose a file", type=["csv"], help="Only csv files allowed")
if uploaded_file is not None:
    dataFrame = pd.read_csv(uploaded_file)

    # Initialization session state
    if 'dataFrame' not in st.session_state:
        st.session_state['dataFrame'] = dataFrame


    
if 'dataFrame' not in st.session_state:
    st.write('Data is empty, Please upload dataset')
else:
    df = st.session_state['dataFrame']
    st.write(st.session_state['dataFrame'])

    st.markdown("#### Basic Data Analysis")

    # Get header from dataset just numeric only
    s = (df.dtypes != "object")
    object_cols = list(s[s].index)

    # Remove id
    object_cols.remove("id")


    #### 
    # col1,col2 = st.columns(2)

    # with col1:
    #     option1 = st.selectbox("Select independent variable" ,object_cols, index=1)

    # with col2:
    #     option2 = st.selectbox("Select dependent variable" ,object_cols, index=2)
    ####

    # Select variable
    options = st.multiselect("Select variable", object_cols, help="Please select your independent and dependent variable")

    # Show chart
    if options != []:
        st.line_chart(df[options].head(50))