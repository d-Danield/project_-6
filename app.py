import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv') 

# App Header
st.header("Car Sales Data Analysis for Budget Cars")

#  Image
st.image("image.jpg", caption="Car Sales Analysis", use_column_width=True)

# Sidebar checkbox to filter data by price range
st.sidebar.subheader("Filters")
filter_price = st.sidebar.checkbox("Show only cars priced up to $15,000")

if filter_price:
    filtered_data = data[(data['price'] > 0) & (data['price'] <= 15000)]
else:
    filtered_data = data.copy()

# Display dataset summary
st.subheader("Dataset Overview")
st.write(filtered_data.head(15))

# Plot 1: Histogram of Price
st.subheader("Price Distribution")
fig_hist = px.histogram(filtered_data, x='price', title="Price Distribution of Cars")
st.plotly_chart(fig_hist)

# Plot 2: Box Plot of Model Year by Condition
st.subheader("Comparison of Model Year by Condition")
fig_box = px.box(
    filtered_data,
    x='condition',  
    y='model_year',  
    title='Comparison of Model Year by Condition (0-15k$)',
    labels={'condition': 'Condition', 'model_year': 'Model Year'},
    color='condition',
)
st.plotly_chart(fig_box)
