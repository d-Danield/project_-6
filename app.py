import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
data = pd.read_csv('vehicles_us.csv')

# Apply consistent styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2E3440;
        color: #D8DEE9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.header("🚗 Car Sales Data Analysis for Budget Cars")
st.write("Analyzing used car sales data to explore pricing trends, conditions, and more for budget-conscious buyers.")

# Add an image
st.image("image.jpg", caption="Comprehensive Car Sales Analysis", use_container_width=True)

# Sidebar filters
st.sidebar.header("Filter Options")
filter_price = st.sidebar.checkbox("Show only cars priced up to $15,000")
min_price, max_price = st.sidebar.slider(
    "Select Price Range ($):",
    min_value=0, max_value=int(data['price'].max()), value=(0, 15000)
)

# Apply filters
if filter_price:
    filtered_data = data[(data['price'] >= min_price) & (data['price'] <= max_price)]
else:
    filtered_data = data.copy()

selected_condition = st.sidebar.multiselect(
    "Select Conditions:",
    options=filtered_data['condition'].unique(),
    default=filtered_data['condition'].unique()
)
filtered_data = filtered_data[filtered_data['condition'].isin(selected_condition)]

# Display dataset summary
st.subheader("📊 Dataset Overview")
st.write("Below is a subset of the data with 500 cars:")
st.write(filtered_data.head(501))

# Plot 1: Price distribution in a dataset
st.subheader("Price Distribution Shows Which Price Range is More Popular")
fig_hist = px.histogram(filtered_data, x='price', title=" Distribution of Cars by Price")
st.plotly_chart(fig_hist)

# Plot 2: Average price by condition
st.subheader("💰 Average Price by Condition")
avg_price = filtered_data.groupby('condition')['price'].mean().reset_index()
fig_avg_price = px.bar(
    avg_price,
    x='condition',
    y='price',
    title="Average Price by Condition",
    labels={'condition': 'Condition', 'price': 'Average Price ($)'},
    color='condition',
    text='price'
)
fig_avg_price.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig_avg_price.update_layout(xaxis=dict(title="Condition"), yaxis=dict(title="Average Price ($)"))
st.plotly_chart(fig_avg_price)


# Plot 3: Box Plot of Model Year by Condition
st.subheader("📦 Model Year Distribution by Condition")
fig_box = px.box(
    filtered_data,
    x='condition',  
    y='model_year',  
    title='Model Year Distribution by Condition',
    labels={'condition': 'Condition', 'model_year': 'Model Year'},
    color='condition',
)
st.plotly_chart(fig_box)

# Key Takeaways
st.subheader("📌 Key Takeaways")
st.write("""
- Cars in 'new' or 'like new' condition are generally more expensive, as expected.
- Older cars are more common in lower price ranges but may still be in good condition.
- Use the filters to explore data further and make data-driven decisions.
""")

# Footer
st.write("Made with ❤️ by Daniel Davidson")
