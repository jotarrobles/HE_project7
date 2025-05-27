import streamlit as st
import pandas as pd
import heaan_stat

st.title("Encrypted Patient Statistics Analysis")

# Load the dataset
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
#uploaded_file = "./heart_sample.csv" # Uncomment this line to use a sample file directly
if uploaded_file:
    df = pd.read_csv(uploaded_file, )
    df.insert(0, 'id', range(1, len(df) + 1))  # Add an ID column
    st.subheader("Loading Dataframe...")
    if not df.empty:
        st.subheader("Dataframe loaded successfully!")
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        categorical_df = df.select_dtypes(include=['object', 'category', 'bool']) 
        for col in categorical_df.columns:
            numeric_df[col] = categorical_df[col].astype('category')
        # Convert categorical columns to 'category' dtype
        # numeric_df["Gender"]= df["Gender"].astype('category')
        # numeric_df["Status"] = df["Heart Disease Status"].astype('category')
        st.write(numeric_df.dtypes)
        # Set context for HEAAN
        st.subheader("Initializing encryption...")
        
        # Initialize Heaan context
        context = heaan_stat.Context(
            key_dir_path='./keys',
            generate_keys=False,  # To use existing keys, set it to False or omit this
        )
    # Encrypt the DFrame
    from heaan_stat import HEFrame
    he_df = HEFrame(context, numeric_df, encrypt_columns=True)
    st.subheader("Dataframe encrypted successfully!")
    st.write(he_df.info())

# User selection for analysis
    # Choose analysis type
    st.subheader("Select Analysis Type")
    analysis_type = st.selectbox(
        "Choose the type of analysis",
        ["Average", "Sum", "Count", "Standard Deviation"]
    )
    # Choose column for analysis
    st.subheader("Select Column for Analysis")
    numeric_columns = []
    for col in he_df.columns:
        if he_df[col].dtype == 'numeric':
            numeric_columns.append(col)
    numeric_columns.remove('id')  # Remove ID column from selection
    column_name = st.selectbox(
        "Choose the column for analysis",
        ['All'] + numeric_columns
    )
    # Choose grouping category column
    st.subheader("Select Grouping Column (optional)")
    category_columns = []
    for col in he_df.columns:
        if he_df[col].dtype == 'category':
            category_columns.append(col)
    group_by_column = st.selectbox(
        "Choose the column to group by (optional)",
        [None] + category_columns
    )

# Add a button to perform analysis
if st.button("Perform Analysis"):
    temp = he_df

    # Perform analysis
    st.subheader("Performing Analysis...")
    st.write(f"Analysis Type: {analysis_type}")
    st.write(f"Column for Analysis: {column_name}")
    
    GROUP_FLAG = False
    ALL_FLAG = False
    if column_name == "All":
        column_name = numeric_columns
    if group_by_column:
        # Perform grouped analysis
        temp = he_df.groupby(group_by_column)
        GROUP_FLAG = True
        st.write(f"Grouping by: {group_by_column}")

    # Perform selected analysis
    if analysis_type.lower() == "average": 
        result = temp.mean()
    elif analysis_type.lower() == "sum":
        result = temp.sum()
    elif analysis_type.lower() == "count":
        result = temp.count()
    elif analysis_type.lower() == "standard deviation":
        result = temp.std()
    else:
        st.error("Invalid analysis type selected.")
        st.stop()
    
    if GROUP_FLAG:
        st.write(result.decrypt(inplace = False).to_frame()[column_name])
    else:
        st.write(result.decrypt(inplace = False).to_series()[column_name])

    if st.button("Plot"):
        st.subheader("Plotting Results")
        st.write("This may take a while ...")
        if GROUP_FLAG:
            st.bar_chart(result.decrypt(inplace = False ).to_frame()[column_name])
        else:
            st.bar_chart(result.decrypt(inplace = False).to_series()[column_name])


